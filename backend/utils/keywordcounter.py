from collections import Counter
import re

LANGUAGE_KEYWORDS = {
    "python": [
        "def", "return", "if", "else", "elif", "for", "while", "try", "except", "import",
        "from", "as", "class", "with", "lambda", "yield", "async", "await", "pass", "raise"
    ],
    "javascript": [
        "function", "return", "if", "else", "for", "while", "let", "const", "var", "try",
        "catch", "import", "from", "export", "class", "async", "await", "new", "this"
    ],
    "typescript": [
        "function", "return", "if", "else", "for", "while", "let", "const", "var", "try",
        "catch", "import", "from", "export", "class", "async", "await", "new", "this",
        "interface", "type", "enum", "implements", "readonly"
    ],
    "go": [
        "func", "return", "if", "else", "for", "range", "switch", "case", "select", "go",
        "defer", "package", "import", "var", "const", "type", "struct", "interface"
    ],
    "java": [
        "public", "private", "protected", "class", "interface", "extends", "implements",
        "static", "final", "void", "return", "if", "else", "switch", "case", "while",
        "for", "try", "catch", "import", "package", "this", "new", "throw", "throws"
    ],
    "c": [
        "int", "char", "float", "double", "void", "return", "if", "else", "for", "while",
        "switch", "case", "break", "continue", "struct", "typedef", "include", "define"
    ],
    "c++": [
        "int", "float", "double", "void", "return", "if", "else", "for", "while", "switch",
        "case", "break", "continue", "class", "struct", "public", "private", "protected",
        "template", "typename", "include", "define", "namespace", "using", "new", "delete"
    ],
    "c#": [
        "using", "namespace", "public", "private", "protected", "internal", "static", "class",
        "interface", "return", "void", "int", "string", "float", "double", "if", "else",
        "switch", "case", "for", "while", "try", "catch", "new", "this", "async", "await"
    ]
}

def count_keywords(content: str, language: str) -> dict:
    language = language.lower()
    keywords = LANGUAGE_KEYWORDS.get(language, [])
    tokens = re.findall(r"\b\w+\b", content)
    counts = Counter(token for token in tokens if token in keywords)
    return dict(counts)
