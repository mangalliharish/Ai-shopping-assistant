from transformers import pipeline

# ✅ Load lightweight model
generator = pipeline(
    "text-generation",
    model="gpt2",
    max_new_tokens=120
)


# 🎯 Smart reason generator (rule-based boost)
def generate_reason(query):
    query = query.lower()

    if "gaming" in query:
        return "Great for gaming 🎮"
    elif "camera" in query:
        return "Excellent camera 📸"
    elif "battery" in query:
        return "Long battery life 🔋"
    elif "performance" in query:
        return "Fast performance ⚡"
    elif "display" in query:
        return "Great display quality 🖥️"
    else:
        return "Best value for money 💰"


def generate_ai_response(query, products):
    if not products:
        return "No good products found."

    # 🎯 Take top 3 products only
    top_products = products[:3]

    recommendations = []

    for i, product in enumerate(top_products[:2]):  # ✅ Only top 2
        reason = generate_reason(query)

        recommendations.append(
            f"{i+1}. {product['title']} - {reason}"
        )

    return "\n".join(recommendations)