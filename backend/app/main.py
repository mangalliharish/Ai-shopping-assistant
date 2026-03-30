from fastapi import FastAPI
from pydantic import BaseModel
from services.hf_llm import generate_response

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Shopping Assistant is running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    reply = generate_response(req.message)
    return {"response": reply}