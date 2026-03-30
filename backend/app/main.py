from fastapi import FastAPI
from pydantic import BaseModel

from backend.app.services.hf_llm import generate_ai_response
from backend.app.services.web_search import search_products_online

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI Shopping Assistant is running 🚀"}

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        # 🔍 Get products
        products = search_products_online(req.message)

        # 🤖 AI response
        reply = generate_ai_response(req.message, products)

        return {"response": reply}

    except Exception as e:
        return {"response": f"Error: {str(e)}"}