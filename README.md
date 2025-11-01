# DocBot
# 🩺 DocBot — USMLE AI Study Assistant  

DocBot is an AI-powered study assistant built for medical students preparing for the **USMLE Step 1** exam.  
It runs locally using **FastAPI**, **ChromaDB**, and a **Sentence Transformer model** to retrieve and summarize knowledge from **First Aid for the USMLE Step 1 (2025)**.

---

## ⚙️ Features
- 🧠 **Offline Mode** — Works locally without OpenAI  
- 💬 **Interactive Chat API** (FastAPI `/chat` endpoint)  
- 📚 **Knowledge Base** from First Aid 2025 (865 pages indexed)  
- ⚡ **Smart Summarizer** — Returns concise, context-rich answers  
- 🔒 **Private Data Handling** — No external servers required  

---

## 🧩 Tech Stack
| Component | Purpose |
|------------|----------|
| **Python** | Core language |
| **FastAPI** | Web framework for the backend |
| **ChromaDB** | Vector database for embeddings |
| **SentenceTransformers** | Local embedding model |
| **OpenAI API (optional)** | For enhanced summarization when available |

---

## 🚀 Getting Started
1. Clone the repo  
   ```bash
   git clone https://github.com/YOUR_USERNAME/DocBot-USMLE.git
   cd DocBot-USMLE
