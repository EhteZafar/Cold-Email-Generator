# Cold Email Generator 📧

A FastAPI-based application that automatically generates personalized cold emails for job applications by analyzing job postings and matching them with your portfolio.

## 🌟 Features

- **URL-based Job Analysis**: Simply paste a job posting URL to extract key information
- **Smart Information Extraction**: Automatically extracts:
  - Job Role
  - Job Description
  - Required Experience
  - Required Qualifications
  - Required Skills
- **Portfolio Matching**: Automatically matches your relevant portfolio projects with job requirements
- **Email Generation**: Creates personalized cold emails using AI
- **Modern Web Interface**: Clean, responsive UI with easy copy-paste functionality

## 🛠️ Tech Stack

- **Backend**: FastAPI, Python 3.11
- **AI/ML**: LangChain, Groq LLM
- **Vector Database**: ChromaDB
- **Frontend**: HTML, Tailwind CSS
- **Data Parsing**: Pandas
- **Web Scraping**: LangChain WebBaseLoader

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
```

## 📂 Project Structure

Cold-Email-Generator/
├── app/
│ ├── main.py # FastAPI application
│ ├── static/ # Static files
│ ├── templates/ # HTML templates
│ └── assets/ # Project assets
├── .env # Environment variables
├── requirements.txt # Project dependencies
└── README.md # Project documentation


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
   - Scrapes job posting URL
   - Extracts key information using AI
   - Structures data in JSON format

2. **Portfolio Matching**
   - Analyzes job requirements
   - Matches with relevant portfolio projects
   - Selects most relevant examples

3. **Email Generation**
   - Creates personalized email using extracted information
   - Includes relevant portfolio links
   - Maintains professional tone

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is meant to assist in creating cold emails but should not be used as a complete replacement for personal touch in job applications. Always review and modify generated emails before sending.

## 🔗 Contact

For any queries or suggestions, please open an issue in the repository.