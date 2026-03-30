def generate_ai_response(query, products):
    if not products:
        return "No good products found 😔"

    top = products[:3]

    response = "🔥 Best Picks:\n\n"

    for p in top:
        title = p.get("title", "No title")
        price = p.get("price", "No price")

        response += f"👉 {title} ({price})\n"

    response += "\n💡 Why?\n"

    q = query.lower()

    if "gaming" in q:
        response += "Great for gaming 🎮"
    elif "camera" in q:
        response += "Excellent camera 📸"
    elif "battery" in q:
        response += "Long battery 🔋"
    elif "performance" in q:
        response += "Fast performance ⚡"
    else:
        response += "Best value for money 💰"

    return response