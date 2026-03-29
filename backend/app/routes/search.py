from fastapi import APIRouter
from app.services.hf_llm import generate_ai_response   # ✅ HuggingFace (not llm)
from app.services.web_search import search_products_online
from app.services.embeddings import create_embeddings
from sentence_transformers import SentenceTransformer
import numpy as np
import re
import urllib.parse

router = APIRouter()

# Load model (for future use)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load local data (fallback / future)
products, product_embeddings = create_embeddings()


# 🧠 Extract intent from query
def extract_intent(query: str):
    query = query.lower()

    intent = {
        "budget": None,
        "category": None
    }

    # 💰 Budget
    match = re.search(r'(\d+)', query)
    if match:
        intent["budget"] = int(match.group(1))

    # 📱 Category
    if "phone" in query:
        intent["category"] = "phone"
    elif "laptop" in query:
        intent["category"] = "laptop"

    return intent


# 🌐 Extract domain name
def get_domain(link):
    try:
        return urllib.parse.urlparse(link).netloc
    except:
        return "unknown"


# 🔍 Main Search API
@router.get("/search")
def search_products(query: str):
    intent = extract_intent(query)

    # 🌐 Get products from internet
    results = search_products_online(query)

    # 🤖 HuggingFace AI response
    ai_response = generate_ai_response(query, results)

    return {
        "ai_response": ai_response,
        "intent": intent,
        "results": results
    }