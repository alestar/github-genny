# GitHub Repository Documentation Generator

This Python application clones or crawls a GitHub repository, collects code files, and uses an LLM (OpenAI or Groq-compatible) to automatically generate **project documentation** in Markdown format.

It supports generating:
- **A single combined `.md` file** containing all file documentation with a table of contents
- (Optionally) One `.md` file per source file

---

## ✨ Features

- Clone public GitHub repositories locally
- Recursively crawl for target file types (`.py`, `.java`, `.txt` by default)
- Use OpenAI or Groq API for generating natural-language documentation
- Output a **single combined Markdown document** with clickable table of contents
- Configurable via **CLI arguments** (repository URL, output file name, file types, model)

---

## 📦 Requirements

Python 3.9+ and the following dependencies:

```txt
GitPython>=3.1.0
requests>=2.28.0
openai>=1.0.0
urllib3>=2.0.0
tiktoken>=0.7.0
```
### Install them with:

```
pip install -r requirements.txt
```
---

## 🔑 API Keys

```
export OPENAI_API_KEY="your-openai-api-key"

export GROQ_API_KEY="your-groq-api-key"
```
. Groq API (Free for devs — blazing fast GPT-3.5 / Mixtral / LLaMA)
✨ Highlights:
Access to LLaMA 3, Mixtral, and Gemma

Super fast (via custom hardware)

Generous free tier, no credit card required

🔗 Sign Up:
https://console.groq.com/

🔌 Models Available:
- llama3-8b-8192
- llama3-70b-8192 ( ✅ closest to GPT-4 quality)
-  mixtral-8x7b-32768
---

## 🚀 Usage
Interactive Mode
Run without parameters — the app will prompt for the repo URL:

```
python main.py https://github.com/user/repo -o MyDocs.md 

```

---

## 📂 Output
The generated documentation file will be placed inside a docs/ directory:

Example structure:
```
docs/
└── owner-repo.docs.md      # Single combined documentation file
```
The .md file includes:

 - Repository title

 - Table of Contents

 - One section per source file with LLM-generated explanations

## 🛠 Example

```
python main.py https://github.com/alestar/anagramAPI.git --output doc_test.md
```

This will:

- Clone repo "https://github.com/alestar/anagramAPI.git"

- Scan for  files (ending in .java in this case)

- Use the llama3-70b-8192 model on Groq to generate documentation

- Save everything into docs/doc_test.m

##  ⚠️ Notes
- Large files may exceed the LLM context limit. For now, the script attempts to send the file as-is (you can add chunking if needed).

- Private repositories require authentication (not implemented in the default flow).

- API usage may incur costs depending on your LLM provider.