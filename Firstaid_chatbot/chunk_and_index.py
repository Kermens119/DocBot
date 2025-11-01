import json, os
from tqdm import tqdm
import tiktoken
import chromadb
from sentence_transformers import SentenceTransformer

# ---- Paths ----
pages_path = "data/first_aid_2025_pages.jsonl"
chroma_path = "data/chroma_local"
os.makedirs(chroma_path, exist_ok=True)

# ---- Load local embedding model ----
print("🧠 Loading local model (this can take ~30 s first time)...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# ---- Tokenizer for chunk sizes ----
enc = tiktoken.get_encoding("cl100k_base")

def chunk_text(text, max_tokens=800, overlap=150):
    tokens = enc.encode(text)
    chunks, start = [], 0
    while start < len(tokens):
        end = start + max_tokens
        chunk = enc.decode(tokens[start:end])
        chunks.append(chunk)
        start += max_tokens - overlap
    return chunks

# ---- Read pages ----
print("📖 Reading book pages...")
pages = []
with open(pages_path, "r", encoding="utf-8") as f:
    for line in f:
        pages.append(json.loads(line))

# ---- Chunk pages ----
print("✂️ Chunking pages into smaller pieces...")
docs, ids, metas, count = [], [], [], 0
for p in tqdm(pages):
    page_num, text = p["page"], p["text"]
    for chunk in chunk_text(text):
        docs.append(chunk)
        metas.append({"page": page_num})
        ids.append(f"fa2025_{count}")
        count += 1

print(f"✅ Created {len(docs)} chunks from {len(pages)} pages.")

# ---- Create Chroma collection ----
chroma_client = chromadb.PersistentClient(path=chroma_path)
collection = chroma_client.get_or_create_collection("first_aid_2025_local")

# ---- Generate embeddings locally ----
print("⚙️ Creating and saving embeddings (no API required)...")
batch_size = 64
for i in tqdm(range(0, len(docs), batch_size)):
    batch_docs = docs[i:i + batch_size]
    vectors = model.encode(batch_docs).tolist()
    collection.add(documents=batch_docs,
                   embeddings=vectors,
                   metadatas=metas[i:i + batch_size],
                   ids=ids[i:i + batch_size])

print("✅ Local AI memory library built successfully in /data/chroma_local/")
