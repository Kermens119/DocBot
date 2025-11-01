from fastapi import FastAPI
from pydantic import BaseModel
import chromadb
from sentence_transformers import SentenceTransformer
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Initialize local vector database (memory)
chroma_client = chromadb.PersistentClient(path="data/chroma_local")
collection = chroma_client.get_or_create_collection("first_aid_2025_local")

# Load local embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Optional OpenAI key if you want GPT to help with phrasing (not required for offline)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) if os.getenv("OPENAI_API_KEY") else None

# Request structure
class ChatRequest(BaseModel):
    question: str
    k: int = 3  # number of chunks to retrieve

@app.post("/chat")
def chat(req: ChatRequest):
    # Step 1: Turn question into an embedding
    question_vec = model.encode(req.question).tolist()

    # Step 2: Search in local Chroma memory
    results = collection.query(
        query_embeddings=[question_vec],
        n_results=req.k
    )

    docs = results["documents"][0]
    metas = results["metadatas"][0]

    # Step 3: Combine top chunks
    context = "\n\n---\n\n".join([f"(Page {m['page']}) {d}" for d, m in zip(docs, metas)])

    # 🧠 Smart Answer Logic — Local + Optional OpenAI
    try:
        # Try OpenAI first (if available)
        if client:
            prompt = f"Answer this question using the following text:\n\n{context}\n\nQuestion: {req.question}"
            resp = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful medical tutor using First Aid 2025."},
                    {"role": "user", "content": prompt}
                ]
            )
            answer = resp.choices[0].message.content
        else:
            raise Exception("No OpenAI client active")

    except Exception as e:
        # ⚙️ Local summarizer fallback (free + offline)
        cleaned_context = context.replace("\n", " ").replace("  ", " ").strip()

        # Get first 800 characters only to keep it short
        trimmed = cleaned_context[:800] + "..." if len(cleaned_context) > 800 else cleaned_context

        # Rough summarization by keeping first few sentences
        sentences = trimmed.split(".")
        summary = ". ".join(sentences[:4]) + "."

        answer = f"🧠 Based on First Aid 2025, here’s what I found:\n\n{summary}"

    return {"question": req.question, "answer": answer, "sources": metas}
