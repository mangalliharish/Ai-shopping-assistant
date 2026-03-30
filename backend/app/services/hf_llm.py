import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    token=os.getenv("HUGGINGFACE_API_KEY")
)

def generate_ai_response(query, products):
    if not products:
        return "No good products found 😔"

    top_products = products[:3]

    product_text = ""
    for p in top_products:
        product_text += f"- {p['title']} ({p['price']})\n"

    prompt = f"""
You are an AI shopping assistant.

User query: {query}

Top products:
{product_text}

Give a short, helpful recommendation and explain which is best and why.
"""

    response = client.text_generation(
        prompt,
        max_new_tokens=200
    )

    return response