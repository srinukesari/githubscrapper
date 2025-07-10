import requests
from urllib.parse import urlparse
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from utils import utils,keywordcounter
from collections import Counter
from openai import OpenAI
import os


app = FastAPI()

# Allow React frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def convert_to_raw_url(github_url: str) -> str:
    """
    Converts a GitHub file URL to the raw content URL.
    """
    if "github.com" not in github_url or "/blob/" not in github_url:
        raise ValueError("URL must be a GitHub file link containing '/blob/'")

    parts = github_url.replace("https://github.com/", "").split("/blob/")
    repo_part = parts[0]  # user/repo
    file_part = parts[1]  # branch/path/to/file.py

    raw_url = f"https://raw.githubusercontent.com/{repo_part}/{file_part}"
    return raw_url


def count_loc(content: str) -> dict:
    code, comments, blank = 0, 0, 0
    for line in content.splitlines():
        stripped = line.strip()
        if not stripped:
            blank += 1
        elif stripped.startswith(("#", "//", "/*", "*", "--")):
            comments += 1
        else:
            code += 1
    return {"code": code, "comments": comments, "blank": blank}

@app.get("/scrape")
def fetch_github_file(url: str) -> JSONResponse:
    """
    Fetches the raw content of a file from GitHub and returns analytics.
    """
    try:
        raw_url = convert_to_raw_url(url)
        filename = raw_url.split("/")[-1]
        if not filename:
            raise ValueError("Invalid URL: Unable to extract filename.")

        language = utils.detect_language_from_extension(filename)

        response = requests.get(raw_url)
        response.raise_for_status()
        content = response.text

        

        keyword_freq = keywordcounter.count_keywords(content, language)
        loc_summary = count_loc(content)

        smells = []
        if language.lower() == "python":
            smells = utils.analyze_python_code_smells(content)
        elif language.lower() == "go":
            smells = utils.analyze_go_code_smells(content)
        elif language.lower() == "java":
            smells = utils.analyze_java_code_smells(content)
        elif language.lower() == "c" or language.lower() == "c++":
            smells = utils.analyze_c_code_smells(content)
        else:
            smells = utils.analyze_with_openai(content, language, client)


        return JSONResponse(content={
            "raw_url": raw_url,
            "content": content,
            "language": language,
            "analytics": {
                "keywordFrequency": keyword_freq,
                "linesOfCode": loc_summary,
                "smells": smells,
            }
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    github_file_url = input("Enter GitHub file URL: ").strip()
    try:
        content = fetch_github_file(github_file_url)
        print("\n--- FILE CONTENT START ---\n")
        print(content)
        print("\n--- FILE CONTENT END ---\n")
    except Exception as e:
        print(f"Error: {e}")
