# 📚 Research RAG System using Endee Vector Database

A Retrieval-Augmented Generation (RAG) pipeline for research paper question answering built with:

- 🧠 SentenceTransformers (MiniLM embeddings)
- ⚡ Endee Vector Database
- 📄 PDF ingestion & chunking
- 🔍 Semantic search over research papers

---

## 🚀 Overview

This project implements a full Retrieval-Augmented Generation (RAG) backend pipeline that allows users to:

1. Ingest research papers (PDFs)
2. Chunk and embed text using SentenceTransformers
3. Store embeddings in an Endee vector database
4. Perform semantic search over documents
5. Retrieve the most relevant text chunks for a query

The system forms the retrieval backbone for a research assistant.

---

## 🏗 Architecture
# 📚 Research RAG System using Endee Vector Database

A Retrieval-Augmented Generation (RAG) pipeline for research paper question answering built with:

- 🧠 SentenceTransformers (MiniLM embeddings)
- ⚡ Endee Vector Database
- 📄 PDF ingestion & chunking
- 🔍 Semantic search over research papers

---

## 🚀 Overview

This project implements a full Retrieval-Augmented Generation (RAG) backend pipeline that allows users to:

1. Ingest research papers (PDFs)
2. Chunk and embed text using SentenceTransformers
3. Store embeddings in an Endee vector database
4. Perform semantic search over documents
5. Retrieve the most relevant text chunks for a query

The system forms the retrieval backbone for a research assistant.

---

## 🏗 Architecture
# 📚 Research RAG System using Endee Vector Database

A Retrieval-Augmented Generation (RAG) pipeline for research paper question answering built with:

- 🧠 SentenceTransformers (MiniLM embeddings)
- ⚡ Endee Vector Database
- 📄 PDF ingestion & chunking
- 🔍 Semantic search over research papers

---

## 🚀 Overview

This project implements a full Retrieval-Augmented Generation (RAG) backend pipeline that allows users to:

1. Ingest research papers (PDFs)
2. Chunk and embed text using SentenceTransformers
3. Store embeddings in an Endee vector database
4. Perform semantic search over documents
5. Retrieve the most relevant text chunks for a query

The system forms the retrieval backbone for a research assistant.

---

## 🏗 Architecture

<img width="1920" height="1080" alt="Screenshot 2026-03-01 155003" src="https://github.com/user-attachments/assets/f963c141-cc92-4769-95f6-e461212c9206" />
<img width="1920" height="1080" alt="Screenshot 2026-03-01 155012" src="https://github.com/user-attachments/assets/a2adac6c-d3d9-47ea-b5da-aff9c441fa00" />
PDF → Text Extraction → Chunking → Embedding → Endee Vector DB
↑
Query → Embedding → Vector Search → Top-k Retrieval → Text Output
---

## 📂 Project Structure


research_rag/
│
├── ingest.py # PDF ingestion and vector storage
├── query.py # Semantic search interface
├── utils.py # PDF extraction utilities
├── init.py
│
reset_index.py # Script to reset vector index
requirements.txt
README.md
.gitignore


---

## ⚙️ Installation

### 1️⃣ Clone Repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Start Endee Server (Docker)
docker run -d -p 8080:8080 --name endee-server endeeio/endee-server:latest
📥 Ingest Research Papers

Place PDFs inside:

data/papers/

Then run:

python -m research_rag.ingest

This will:

Extract text

Chunk with overlap

Generate embeddings

Store vectors in Endee

Save metadata locally

🔎 Query the System
python -m research_rag.query

Example:

What is the main contribution of the paper?

The system will:

Embed your query

Perform vector similarity search

Retrieve top-k relevant chunks

Display source and text

🧠 Embedding Model

Model used:

sentence-transformers/all-MiniLM-L6-v2

Embedding dimension: 384

Fast and lightweight

Suitable for semantic search

📊 Vector Database Configuration

Index name: dash1

Dimension: 384

Similarity: Cosine

Precision: float32

🔥 Features

✔ PDF ingestion pipeline
✔ Safe overlapping chunking
✔ Vector embedding storage
✔ Semantic similarity search
✔ Local metadata alignment
✔ Interactive CLI query interface

🛠 Future Improvements

Add LLM-based answer synthesis

Add citation formatting

Build Streamlit web interface

Hybrid search (BM25 + vector)

Add evaluation metrics

📌 Use Cases

Research paper QA assistant

Literature survey automation

Academic knowledge retrieval

Semantic document search
