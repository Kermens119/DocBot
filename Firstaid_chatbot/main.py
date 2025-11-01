from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend working successfully!"}

@app.get("/about")
def about():
    return {"info": "This is the USMLE AI backend, built to help students study medical content interactively."}


import json

@app.get("/study/{subject}")
def study(subject: str):
    try:
        with open("study_data.json", "r") as file:
            data = json.load(file)
        if subject in data:
            return data[subject]
        else:
            return {"error": "Subject not found. Try Biochemistry or Microbiology."}
    except Exception as e:
        return {"error": str(e)}

