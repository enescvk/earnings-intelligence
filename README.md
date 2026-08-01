# Earnings Intelligence

An AI-powered earnings analysis platform that transforms corporate earnings call transcripts into professional investment research reports using a local Large Language Model (LLM).

## Overview

Earnings calls contain valuable insights about a company's financial performance, strategy, risks, and future outlook. However, reading hundreds of pages of transcripts every quarter is time-consuming.

This project aims to automate that process by leveraging a local LLM to generate structured investment research reports from earnings call transcripts.

The long-term vision is to build an intelligent financial research assistant capable of summarizing earnings calls, comparing historical reports, analyzing management sentiment, and identifying changes across quarters.

---

## Current Features (Version 1)

- Analyze earnings call transcripts using a local LLM (Ollama)
- Generate structured investment research reports
- Professional Markdown report formatting
- Deterministic output through prompt engineering
- Automatic report export

Current report sections include:

- Executive Summary
- Financial Highlights
- Positive Developments
- Negative Developments
- Risks
- Opportunities
- Management Guidance
- Key Quotes
- Management Confidence

---

## Current Pipeline

```text
Transcript (.txt)
        ↓
Prompt Builder
        ↓
Local LLM (Ollama)
        ↓
AI Report
        ↓
Markdown Report (.md)
```

---

## Tech Stack

- Python
- Ollama
- Gemma 4 (12B)
- Markdown
- Git

Future versions may incorporate:

- LangChain / LlamaIndex
- Vector Databases
- Embeddings
- Retrieval-Augmented Generation (RAG)
- FastAPI
- React
- Docker

---

## Project Structure

```text
earnings-intelligence/

├── reports/           # Generated investment reports
├── transcripts/       # Earnings call transcripts
├── src/
│   ├── llm.py
│   ├── prompt_builder.py
│   ├── report_writer.py
│   └── ...
├── main.py
└── README.md
```

---

## Example Output

The application generates reports similar to:

```text
# Executive Summary

...

# Financial Highlights

...

# Positive Developments

...

# Risks

...

# Management Confidence

Confidence Score: 9/10
```

Reports are automatically saved as:

```text
reports/NVDA_Q1_2027.md
```

---

## Roadmap

### Version 1
- [x] Local LLM integration
- [x] Prompt engineering
- [x] Structured report generation
- [x] Markdown report export
- [ ] Automatic metadata extraction
- [ ] Multi-company testing

### Version 2
- Historical earnings comparison
- Change detection across quarters
- Structured JSON outputs
- Improved financial metric extraction

### Version 3
- Retrieval-Augmented Generation (RAG)
- Vector database integration
- Industry and peer comparison
- Web interface

---

## Lessons Learned

Throughout development, the project has emphasized practical AI engineering principles, including:

- Prompt engineering through iterative experimentation
- Deterministic generation with temperature tuning
- Long-context prompting
- Modular software design
- Understanding the limitations of single-prompt architectures

---

## Goals

The ultimate objective is to build an AI-powered earnings intelligence platform capable of answering questions such as:

- What changed since last quarter?
- How has management sentiment evolved?
- What are the company's biggest risks and opportunities?
- How does this quarter compare with competitors?

---

## Author

Built by **Enes C.**

This project is being developed as a hands-on exploration of modern AI engineering, local LLMs, and financial intelligence applications.