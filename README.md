# 🚀 GitHub File Scraper

A full-stack web application that fetches and analyzes the content of any GitHub file URL. Built using **FastAPI** for the backend and **React + Vite** for the frontend. It leverages the **OpenAI API** to detect code smells and provide intelligent insights.

---

## ✨ Features

- 🔗 Paste a GitHub file URL and get raw code content.
- 📊 Displays analytics like:
  - Keyword frequency
  - Lines of code summary
  - Code smells (via OpenAI)
- 🌐 Full-stack architecture
- 🔐 OpenAI API key managed via environment variables

---

## 🧱 Tech Stack

| Layer         | Technology              |
|---------------|--------------------------|
| Frontend      | React + Vite + MUI       |
| Backend       | FastAPI (Python)         |
| AI Code Smells| OpenAI API (GPT-3.5)     |
| Communication | REST API with CORS       |
| Deployment    | (Optional) Railway, Netlify |

---

## ⚙️ Setup Instructions - Backend

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/github-file-scraper.git
cd github-file-scraper
```

### 2. Backend Setup (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. export openAI API KEY
```bash
export OPENAI_API_KEY=your_openai_api_key_here
```

### 4. start the server
```bash
uvicorn main:app --reload
```

## Frontend

### 1. enter the folder
```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Run the server
```bash
npm run dev
```





