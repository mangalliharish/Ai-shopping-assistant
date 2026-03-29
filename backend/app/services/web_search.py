import requests

# 🔑 Replace with your real SerpAPI key
API_KEY = "64f15f50b88a830dd31089f27b3c85e6a786b78aabdd457dc0a19a6a949731b6"


def search_products_online(query: str):
    try:
        url = "https://serpapi.com/search.json"

        # 🔥 Improve query for better results
        improved_query = f"{query} buy online India price"

        results = []

        # =========================
        # 🔍 STEP 1: GOOGLE SHOPPING
        # =========================
        params = {
            "engine": "google_shopping",
            "q": improved_query,
            "api_key": API_KEY,
            "gl": "in",
            "hl": "en"
        }

        response = requests.get(url, params=params)
        data = response.json()

        # Debug (optional)
        print("DEBUG shopping_results:", data.get("shopping_results"))

        # ✅ If shopping results found
        if data.get("shopping_results"):

            for item in data["shopping_results"]:

                title = item.get("title")
                price = item.get("price", "N/A")
                link = item.get("product_link") or item.get("link")
                source = item.get("source", "unknown")
                thumbnail = item.get("thumbnail")

                # ❌ Skip invalid items
                if not title:
                    continue

                if link:
                    link_lower = link.lower()
                    if "youtube" in link_lower or "reddit" in link_lower:
                        continue

                results.append({
                    "title": title,
                    "price": price,
                    "source": source,
                    "link": link,
                    "thumbnail": thumbnail
                })

        # =========================
        # 🔍 STEP 2: FALLBACK SEARCH
        # =========================
        if len(results) == 0:

            params = {
                "engine": "google",
                "q": improved_query,
                "api_key": API_KEY,
                "gl": "in",
                "hl": "en"
            }

            response = requests.get(url, params=params)
            data = response.json()

            for item in data.get("organic_results", []):

                title = item.get("title")
                link = item.get("link")

                if not title or not link:
                    continue

                results.append({
                    "title": title,
                    "price": "Check site",
                    "source": item.get("source", "unknown"),
                    "link": link,
                    "thumbnail": None
                })

        # =========================
        # 🎯 RETURN TOP RESULTS
        # =========================
        return results[:5]

    except Exception as e:
        return [{
            "error": str(e)
        }]