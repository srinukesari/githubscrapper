from radon.complexity import cc_visit,cc_rank
from radon.metrics import mi_visit, mi_rank
import re
from utils.ranks import cc_rank as rankcc, mi_rank as rankmi
import json

def detect_language_from_extension(filename: str) -> str:
    ext = filename.split(".")[-1].lower()
    mapping = {
        # Python
        "py": "Python",
        "pyw": "Python",
        "pyc": "Python Bytecode",

        # JavaScript / TypeScript
        "js": "JavaScript",
        "jsx": "JavaScript React",
        "mjs": "JavaScript Module",
        "cjs": "JavaScript CommonJS",
        "ts": "TypeScript",
        "tsx": "TypeScript React",

        # Java
        "java": "Java",
        "jar": "Java Archive",

        # Go
        "go": "Go",

        # C / C++
        "c": "C",
        "h": "C/C++ Header",
        "hh": "C++ Header",
        "hpp": "C++ Header",
        "cc": "C++",
        "cpp": "C++",
        "cxx": "C++",
        "ino": "Arduino (C++)",

        # C#
        "cs": "C#",
        "csx": "C# Script",

        # Ruby
        "rb": "Ruby",
        "rbw": "Ruby",

        # PHP
        "php": "PHP",
        "php4": "PHP",
        "php5": "PHP",
        "phtml": "PHP",
        "inc": "PHP Include",

        # Shell scripting
        "sh": "Shell",
        "bash": "Shell",
        "zsh": "Shell",
        "ksh": "Shell",

        # HTML / CSS / Web
        "html": "HTML",
        "htm": "HTML",
        "xhtml": "XHTML",
        "css": "CSS",
        "scss": "Sass",
        "sass": "Sass",
        "less": "Less",

        # JSON / YAML / XML
        "json": "JSON",
        "yaml": "YAML",
        "yml": "YAML",
        "xml": "XML",

        # SQL
        "sql": "SQL",
        "psql": "PostgreSQL SQL",

        # Kotlin
        "kt": "Kotlin",
        "kts": "Kotlin Script",

        # Swift
        "swift": "Swift",

        # Scala
        "scala": "Scala",
        "sc": "Scala Script",

        # Dart
        "dart": "Dart",

        # R
        "r": "R",
        "rmd": "R Markdown",

        # Perl
        "pl": "Perl",
        "pm": "Perl Module",

        # Lua
        "lua": "Lua",

        # Groovy
        "groovy": "Groovy",
        "gradle": "Groovy",

        # MATLAB
        "m": "MATLAB/Octave",

        # Objective-C
        "m": "Objective-C",
        "mm": "Objective-C++",

        # Visual Basic
        "vb": "Visual Basic",
        "vbs": "VBScript",

        # JSON5
        "json5": "JSON5",

        # Markdown
        "md": "Markdown",

        # Dockerfile (no extension, but common filename)
        # "Dockerfile": "Dockerfile"  # can't map by extension here

        # Others
        "bat": "Batch",
        "ps1": "PowerShell",
        "coffee": "CoffeeScript",
        "erl": "Erlang",
        "ex": "Elixir",
        "exs": "Elixir Script",
        "hs": "Haskell",
        "clj": "Clojure",
        "cljs": "ClojureScript",
        "fs": "F#",
        "fsx": "F# Script",
    }

    return mapping.get(ext, "Unknown")

def analyze_python_code_smells(code: str):
    complexity_results = cc_visit(code)
    functions = []
    for func in complexity_results:
        functions.append({
            "name": func.name,
            "complexity": func.complexity,
            "rank": cc_rank(func.complexity)
        })

    # Maintainability Index
    mi_score = mi_visit(code, False)  # returns float
    mi_score_rounded = round(mi_score, 2)
    mi_score_rank = mi_rank(mi_score)

    return {
        "functions": functions,
        "maintainability_index": {
            "score": mi_score_rounded,
            "rank": mi_score_rank
        }
    }


def analyze_java_code_smells(code: str):
    function_pattern = r"(public|private|protected)?\s*(static)?\s*\w+\s+(\w+)\s*\([^)]*\)\s*{"
    functions = re.findall(function_pattern, code)
    
    complexity_keywords = ["if", "for", "while", "case", "catch", "throw", "&&", "||", "?:"]
    total_complexity = sum(code.count(k) for k in complexity_keywords)

    function_list = []
    avg_complexity = total_complexity / len(functions) if functions else 0
    for _, _, name in functions:
        function_list.append({
            "name": name,
            "complexity": round(avg_complexity),
            "rank": rankcc(round(avg_complexity))
        })

    return {
        "functions": function_list,
        "maintainability_index": {
            "score": round(100 - avg_complexity * 2.5, 2),  # heuristic
            "rank": rankmi(100 - avg_complexity * 2.5)
        }
    }


def analyze_go_code_smells(code: str):
    # Matches Go functions like: func Name(...) ... {
    function_pattern = r"func\s+(\w+)\s*\(.*?\)[^{]*{"
    functions = re.findall(function_pattern, code, re.DOTALL)

    complexity_keywords = ["if", "for", "switch", "case", "go ", "select", "&&", "||"]
    total_complexity = sum(code.count(k) for k in complexity_keywords)

    function_list = []
    avg_complexity = total_complexity / len(functions) if functions else 0
    for name in functions:
        function_list.append({
            "name": name,
            "complexity": round(avg_complexity),
            "rank": rankcc(round(avg_complexity))
        })

    maintainability_score = max(0, 100 - avg_complexity * 2.5)
    return {
        "functions": function_list,
        "maintainability_index": {
            "score": round(maintainability_score, 2),
            "rank": rankmi(maintainability_score)
        }
    }


def analyze_c_code_smells(code: str):
    function_pattern = r"\b(?:int|void|char|float|double)\s+(\w+)\s*\([^)]*\)\s*{"
    functions = re.findall(function_pattern, code)

    complexity_keywords = ["if", "for", "while", "case", "&&", "||", "?:"]
    total_complexity = sum(code.count(k) for k in complexity_keywords)

    function_list = []
    avg_complexity = total_complexity / len(functions) if functions else 0
    for name in functions:
        function_list.append({
            "name": name,
            "complexity": round(avg_complexity),
            "rank": rankcc(round(avg_complexity))
        })

    return {
        "functions": function_list,
        "maintainability_index": {
            "score": round(100 - avg_complexity * 2.5, 2),
            "rank": rankmi(100 - avg_complexity * 2.5)
        }
    }



  # Use env var in production

def analyze_with_openai(code: str, language: str,client) -> dict:
    prompt = f"""
You are a software quality expert.

Analyze the following {language} code and:
1. Identify all function names.
2. Estimate each function's cyclomatic complexity (1–50).
3. Rank each function using this scale:
   A: 1-4, B: 5-9, C: 10-19, D: 20-29, E: 30-39, F: 40+
4. Estimate overall maintainability index from 0–100.
5. Rank maintainability index:
   A: 85+, B: 70–84, C: 55–69, D: 40–54, E: 25–39, F: <25

Return output strictly in the following JSON format:

{{
  "functions": [
    {{ "name": "funcName", "complexity": 3, "rank": "A" }}
  ],
  "maintainability_index": {{
    "score": 82.5,
    "rank": "B"
  }}
}}

Code:
{code}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=700
        )
        content = response.choices[0].message.content.strip()

        try:
            json_start = content.index('{')
            json_data = content[json_start:]
            return json.loads(json_data)
        except Exception as e:
            return {
                "functions": [],
                "maintainability_index": {
                    "score": 0,
                    "rank": "F"
                },
                "error": f"Failed to parse OpenAI response as JSON. Raw response:\n{content}"
            }

    except Exception as e:
        return {
            "functions": [],
            "maintainability_index": {
                "score": 0,
                "rank": "F"
            },
            "error": str(e)
        }
