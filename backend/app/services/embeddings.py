from sentence_transformers import SentenceTransformer
import json

# Load model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def load_products():
    with open("app/products.json") as f:
        return json.load(f)

def create_embeddings():
    products = load_products()

    texts = [
        product["name"] + " " + product["description"]
        for product in products
    ]

    embeddings = model.encode(texts)

    return products, embeddings