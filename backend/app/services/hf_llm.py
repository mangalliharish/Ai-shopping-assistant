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

        response = client.chat_completion(
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )

        return response.choices[0].message["content"]

    except Exception as e:
        print("HF ERROR:", str(e))
        return "Something went wrong with AI 😔"