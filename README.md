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
Create and activate a virtual environment

bash
Copy code
python -m venv venv
venv\Scripts\activate   # on Windows
source venv/bin/activate # on Mac/Linux
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the FastAPI server

bash
Copy code
uvicorn chat_with_ai:app --reload
Open your browser

arduino
Copy code
http://127.0.0.1:8000/docs
🧪 Example Query
json
Copy code
{
  "question": "What are the essential amino acids?"
}
Response:

less
Copy code
🧠 Based on First Aid 2025, here’s what I found:
Essential amino acids are those the body cannot synthesize...
🧩 Future Plans
Add GPT-based summarization (auto-switch when online)

Create web UI for student chat

Host on Cloudways for team study access

👨‍💻 Author
Jackson Ewald
Founder, Logic Leap Tech

Building intelligent systems to empower medical and law enforcement professionals.

yaml
Copy code

---

Once you commit that, your GitHub will look **professional and product-ready** — even investors or collaborators can instantly understand what DocBot does.

---

Would you like me to make a `requirements.txt` file next (so your repo automatically installs everything needed when someone clones it)?




