# Cold Email Generator 📧

A FastAPI-based application that leverages RAG (Retrieval Augmented Generation) and semantic search to automatically generate personalized cold emails for job applications by analyzing job postings and intelligently matching them with your portfolio.

## 🌟 Features

- **URL-based Job Analysis**: Simply paste a job posting URL to extract key information
- **Smart Information Extraction**: Automatically extracts:
  - Job Role
  - Job Description
  - Required Experience
  - Required Qualifications
  - Required Skills
- **Intelligent Portfolio Matching**: Uses semantic search and RAG to match your most relevant portfolio projects with job requirements
- **AI-Powered Email Generation**: Creates personalized cold emails using advanced language models
- **Modern Web Interface**: Clean, responsive UI with easy copy-paste functionality

## 🛠️ Tech Stack

### Backend Framework
- **FastAPI**: Modern, fast web framework for building APIs with Python
- **Python 3.11+**: Core programming language

### AI/ML Components
- **LangChain**: Framework for developing applications powered by language models
- **Groq LLM**: High-performance language model for text generation
- **RAG (Retrieval Augmented Generation)**: Architecture that combines retrieval-based and generative AI
- **Semantic Search**: Advanced text similarity search for portfolio matching

### Vector Database
- **ChromaDB**: Embedded vector database for:
  - Storing portfolio embeddings
  - Semantic similarity search
  - Efficient retrieval of relevant portfolio examples

### Frontend
- **HTML/Jinja2**: Template engine for dynamic content
- **Tailwind CSS**: Utility-first CSS framework for modern UI
- **JavaScript**: Client-side interactivity and form handling

### Data Processing
- **Pandas**: Data manipulation and analysis
- **JSON**: Data formatting and structure
- **WebBaseLoader (LangChain)**: Intelligent web scraping for job postings

### Development Tools
- **dotenv**: Environment variable management
- **uvicorn**: ASGI server for FastAPI
- **Git**: Version control

## 📋 Prerequisites

- Python 3.11 or higher
- Virtual environment (recommended)
- Groq API key
- Internet connection for job URL scraping

## 🚀 Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd Cold-Email-Generator
```

2. **Create and activate virtual environment**
```bash
python -m venv myenv
# On Windows
myenv\Scripts\activate
# On Unix or MacOS
source myenv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory:
```env
GROQ_API_KEY=your_groq_api_key
USER_AGENT=your_user_agent_string
```

## 📂 Project Structure

```
Cold-Email-Generator/
├── app/
│   ├── main.py          # FastAPI application
│   ├── static/          # Static files
│   ├── templates/       # HTML templates
│   └── assets/         # Project assets
├── vector_db/          # ChromaDB storage
├── .env               # Environment variables
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## 🎯 Usage

1. **Start the server**
```bash
uvicorn app.main:app --reload
```

2. **Access the application**
- Open your browser and go to `http://localhost:8000`
- Paste a job posting URL
- Click "Generate Email"
- Review the extracted information and generated email
- Copy the email using the "Copy to Clipboard" button

## 💡 How It Works

1. **Job Information Extraction**
   - Scrapes job posting URL using WebBaseLoader
   - Uses LLM to extract structured information
   - Formats data in JSON format

2. **Portfolio Matching (RAG Implementation)**
   - Analyzes job requirements using semantic search
   - Queries ChromaDB vector database for relevant portfolio projects
   - Uses similarity matching to find best portfolio examples
   - Implements RAG architecture to enhance relevance

3. **Email Generation**
   - Utilizes Groq LLM for natural language generation
   - Incorporates retrieved portfolio examples
   - Creates personalized, context-aware emails
   - Maintains professional tone and structure

## 🔍 Technical Implementation

### RAG Architecture
- **Retrieval**: Uses ChromaDB's semantic search to find relevant portfolio examples
- **Augmentation**: Enhances LLM prompts with retrieved portfolio information
- **Generation**: Creates personalized emails using augmented context

### Vector Database Implementation
- Portfolio projects are stored as embeddings in ChromaDB
- Semantic similarity search for matching job skills
- Efficient retrieval of relevant examples

### LLM Integration
- Uses Groq's LLM for both information extraction and email generation
- Custom prompts for different tasks
- Temperature control for appropriate creativity levels

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is meant to assist in creating cold emails but should not be used as a complete replacement for personal touch in job applications. Always review and modify generated emails before sending.

## 🔗 Contact

For any queries or suggestions, please open an issue in the repository.