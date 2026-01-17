# Automated Resume Personalization & Application Pipeline

## 🚀 Overview

This project is a **production-grade, end-to-end automated resume and cover letter generation system** designed to eliminate the manual, repetitive, and error-prone process of tailoring resumes for every job application.

At its core, the system takes:

* A **Master Resume / Profile** (canonical source of truth)
* A **Job Description**

And produces:

* A **tailored, ATS-optimized resume**
* A **concise, role-specific cover letter**
* A **LaTeX-rendered PDF** ready for submission
* An **ATS compatibility score with keyword-level explainability**

The project demonstrates advanced skills across **backend engineering, ML/NLP systems, LLM orchestration, retrieval-augmented generation (RAG), and document automation**.

---

## 🎯 Problem Statement

Applying to modern software roles requires:

* Frequent resume rewrites
* Keyword alignment for ATS systems
* Custom phrasing for each job description
* Manual LaTeX / formatting edits

This project automates the entire pipeline while preserving **accuracy, relevance, and human-quality output**.

---

## 🧠 High-Level Architecture

```
                ┌───────────────────────────┐
                │   React / Next.js UI       │   (Optional)
                │  - Resume Preview          │
                │  - ATS Score Visualization │
                └─────────────┬─────────────┘
                              │ POST /generate
                              ▼
┌─────────────────────────────────────────────────────┐
│                    FastAPI Backend                   │
│                                                      │
│  API Layer                                           │
│  └── /generate → Orchestration Entry Point           │
│                                                      │
│  Application Pipeline                                │
│  ├── RAG Snippet Selection                            │
│  ├── ATS Semantic Scoring                             │
│  ├── Resume & Cover Letter Generation (LLM)           │
│  ├── LaTeX Rendering                                  │
│  └── PDF Export                                       │
│                                                      │
│  Persistence                                         │
│  ├── PostgreSQL                                      │
│  ├── SQLAlchemy ORM                                  │
│  └── pgvector / FAISS                                │
└─────────────────────────────────────────────────────┘
```

---

## 📂 Project Structure

```
backend/
├── app/
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── llm.py
│   │       ├── profiles.py
│   │       ├── snippets.py
│   │       └── users.py
│   │
│   ├── models/             # SQLAlchemy models & schemas
│   │   ├── db_models.py
│   │   └── schemas.py
│   │
│   ├── pipelines/          # Orchestration layer
│   │   └── application_pipeline.py
│   │
│   ├── services/           # Core business logic
│   │   ├── ats/             # ATS scoring subsystem
│   │   │   ├── ats_scorer.py
│   │   │   ├── semantic_scorer.py
│   │   │   ├── keyword_extractor.py
│   │   │   ├── hybrid_scorer.py
│   │   │   └── rewrite_advisor.py
│   │   │
│   │   ├── llm/             # LLM orchestration
│   │   │   ├── llm_client.py
│   │   │   ├── prompt_templates.py
│   │   │   └── resume_generator.py
│   │   │
│   │   ├── rag/             # Retrieval-Augmented Generation
│   │   │   ├── embedding_client.py
│   │   │   ├── vector_store.py
│   │   │   ├── vector_search.py
│   │   │   ├── rag_selector.py
│   │   │   └── snippetizer.py
│   │   │
│   │   ├── latex/           # LaTeX rendering
│   │   │   ├── resume_renderer.py
│   │   │   ├── cover_letter_renderer.py
│   │   │   ├── latex_renderer.py
│   │   │   ├── latex_utils.py
│   │   │   └── template_loader.py
│   │   │
│   │   └── pdf_generator.py
│   │
│   ├── utils/
│   │   ├── retry.py        # Exponential backoff
│   │   └── security.py
│   │
│   ├── config.py
│   ├── db.py
│   └── main.py             # FastAPI app entry
│
├── alembic/                # Database migrations
├── templates/latex/        # LaTeX templates
│   └── cover_letter.tex
└── generated/              # Output PDFs
```

---

## 🔄 End-to-End Pipeline Flow

### 1️⃣ Profile Ingestion

* Master profile stored as canonical JSON
* Includes all skills, projects, experience, education

### 2️⃣ Snippetization

* Profile decomposed into atomic resume snippets
* Each snippet embedded using transformer-based embeddings

### 3️⃣ Vector Search (RAG)

* Job description embedded
* Top-K most relevant snippets retrieved
* Optional semantic re-ranking

### 4️⃣ ATS Semantic Scoring

* Keyword overlap analysis
* Semantic similarity scoring
* Hybrid ATS score computation
* Keyword explainability provided

### 5️⃣ LLM Resume Generation

* Controlled prompt templates
* JSON-structured outputs
* Resume bullets + cover letter generated

### 6️⃣ LaTeX Rendering

* Resume & cover letter mapped to LaTeX templates
* PDF generated via deterministic compilation

### 7️⃣ API Response

```json
{
  "ats_score": 82,
  "keywords_matched": ["Python", "NLP", "RAG"],
  "bullets": ["..."],
  "latex": "...",
  "pdf_url": "/files/resume.pdf"
}
```

---

## 🧪 Robustness & Engineering Principles

* **Retry-safe LLM calls** with exponential backoff
* **Clear error boundaries** via pipeline exceptions
* **No business logic in API routes**
* **Async-first design** for scalability
* **Deterministic LaTeX rendering**

---

## 🧰 Technologies & Skills Demonstrated

### Languages

* Python
* SQL
* LaTeX

### Frameworks & Libraries

* FastAPI
* SQLAlchemy
* Alembic
* pgvector / FAISS
* Pydantic
* OpenAI / LLM APIs

### ML / NLP Skills

* Retrieval-Augmented Generation (RAG)
* Sentence embeddings
* Semantic similarity
* Hybrid scoring systems
* Prompt engineering
* ATS optimization strategies

### Software Engineering Skills

* Clean architecture
* Async pipelines
* API design
* Orchestration layers
* Retry & fault tolerance
* Database schema design

---

## 📈 Future Enhancements

* React / Next.js UI with live preview
* ATS score visualization dashboard
* Multi-job batch processing
* Resume quality evaluation metrics
* Dockerized deployment
* CI/CD pipeline
* Auto-apply integrations (LinkedIn / Indeed)
* Multilingual resume generation

---

## 🏁 Final Remarks

This project is intentionally **over-engineered** for robustness, clarity, and scalability. It reflects real-world production systems that combine **ML intelligence with strong backend foundations**.

It is suitable for:

* Senior-level portfolio demonstration
* Interview deep-dives
* Startup MVP foundation
* Research into ATS-aware document generation

---

**Author:** Bhav Soks
**Focus:** ML Systems, Backend Engineering, LLM Applications
