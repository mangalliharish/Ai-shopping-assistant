import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",  # ✅ IMPORTANT
    token=os.getenv("HUGGINGFACE_API_KEY")
)

def generate_ai_response(query, products):
    try:
        if not products:
            return "No good products found 😔"

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

Give a short helpful recommendation.
"""

        response = client.text_generation(
            prompt,
            max_new_tokens=200
        )

        return response

    except Exception as e:
        print("HF ERROR:", str(e))  # 🔥 THIS WILL SHOW REAL ERROR
        return "Something went wrong with AI 😔"