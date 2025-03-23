# app/main.py
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.document_loaders import WebBaseLoader
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

# Initialize ChromaDB
client = chromadb.PersistentClient('vector_db')
collection = client.get_or_create_collection('portfolio')

# Job information extraction prompt
job_extractor_prompt = PromptTemplate.from_template(
    """
    ### SCRAPPED TEXT FROM WEBSITE:
    {page_data}
    ### INSTRUCTIONS:
    Extract the following information from the job post webpage:
    - Job Role
    - Job Description
    - Job Experience
    - Job Qualifications
    - Job Skills
    Give me the information in a JSON format.
    Only return the JSON object, nothing else (No PREAMBLE)
    ### JSON OUTPUT (ONLY RETURN THIS JSON OBJECT, NOTHING ELSE):
    """
)

# Email generation prompt
email_prompt = PromptTemplate.from_template(
    """
    ### JOB DESCRIPTION:
    {job_description}
    
    ### CANDIDATE DETAILS:
    My name is Ehtesham Zafar, a skilled software developer with over two years of experience specializing in TypeScript, Java, Node.js, and cloud automation. I have a strong track record of developing scalable applications and optimizing cloud-based workflows. My expertise aligns well with the skills required for this role.

    ### INSTRUCTIONS:
    Craft a professional yet concise cold email to the hiring manager that:
    - Clearly expresses my enthusiasm for the role.
    - Highlights my **most relevant skills** and experience.
    - Shows how I can **add value to the company**.
    - Lists ONLY the most relevant portfolio links (maximum 4) that best match the job requirements:
      {links}
    - Avoids generic statements—make it **personalized and engaging**.
    - Keeps the tone **polite, enthusiastic, and professional**.
    - Focuses on the specific technologies and skills mentioned in the job description.

    Ensure the email **directly starts with the content**—no preamble or unnecessary introductions.
    Keep the portfolio links section brief and focused on the most relevant projects.

    ### EMAIL (NO PREAMBLE):
    """
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate_email")
async def generate_email(job_url: str = Form(...)):
    try:
        # 1. Load and extract job post content
        loader = WebBaseLoader(job_url)
        page_data = loader.load().pop().page_content
        
        # 2. Extract job information
        chain_extractor = job_extractor_prompt | llm
        job_info_response = chain_extractor.invoke(input={'page_data': page_data})
        
        # 3. Parse JSON response
        json_parser = JsonOutputParser()
        job_info = json_parser.parse(job_info_response.content)

        # 4. Get relevant portfolio links based on job skills
        job_skills = job_info.get('Job Skills', [])
        if not job_skills:
            return {"error": "No job skills found in the posting"}

        # Query for relevant portfolio links based on job skills
        links = collection.query(
            query_texts=job_skills,
            n_results=2  # Get top 2 matches per skill
        ).get('metadatas', [])

        # Flatten and get unique links, limiting to top 4 most relevant
        unique_links = list(set(link['links'].strip() for sublist in links for link in sublist))[:4]

        # 5. Generate email
        chain_email = email_prompt | llm
        email = chain_email.invoke(
            input={
                'job_description': job_info['Job Description'],
                'links': unique_links
            }
        )
        
        return {
            "job_info": job_info,
            "email": email.content
        }
    
    except Exception as e:
        return {"error": str(e)}