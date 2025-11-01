import fitz  # PyMuPDF
import json
import os

# Path to your PDF file
pdf_path = "data/first_aid_2025.pdf"

# Where to save the extracted text
output_path = "data/first_aid_2025_pages.jsonl"

# Make sure the 'data' folder exists
os.makedirs("data", exist_ok=True)

# Open the PDF
doc = fitz.open(pdf_path)

# Go through each page one by one
with open(output_path, "w", encoding="utf-8") as f:
    for i, page in enumerate(doc):
        text = page.get_text("text").strip()  # Get the text from each page
        page_data = {
            "page": i + 1,
            "text": text
        }
        # Save each page as one line of JSON
        f.write(json.dumps(page_data, ensure_ascii=False) + "\n")

print(f"✅ Done! Saved text for {len(doc)} pages to {output_path}")