from fastapi import FastAPI

klu = FastAPI(
    title="AI Tutor",
    description="AI Tutor PBL Project",
    version="1.0.0"
)

# Home API
@klu.get("/")
def home():
    return {"message": "WELCOME TO AI TUTOR PROJECT"}


# Demo API
@klu.get("/demo")
def demo():
    return {"message": "KL UNIVERSITY"}


# Ask Question API
@klu.get("/askquestion")
def ask():
    return {
        "message": "What is LLM?",
        "answer": "LLM is Large Language Model"
    }