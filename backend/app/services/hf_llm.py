import os
from huggingface_hub import InferenceClient

# ✅ Use stable model (works on free tier)
client = InferenceClient(
    model="google/flan-t5-large",
    token=os.getenv("HUGGINGFACE_API_KEY")
)

def generate_ai_response(query, products):
    try:
        if not products:
            return "No good products found 😔"

        # Take top 3 products
        top_products = products[:3]

        product_text = ""
        for p in top_products:
            title = p.get("title", "No title")
            price = p.get("price", "No price")
            product_text += f"- {title} ({price})\n"

        prompt = f"""
You are an AI shopping assistant.

User query: {query}

Top products:
{product_text}

Give a short and helpful recommendation in 2-3 lines.
"""

        # ✅ Simple and stable text generation
        response = client.text_generation(
            prompt,
            max_new_tokens=150,
            temperature=0.7
        )

        return response

    except Exception as e:
        print("HF ERROR:", str(e))
        return f"AI Error: {str(e)}"