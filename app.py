from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Official documentation links for each CDP
CDP_DOCS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://docs.lytics.com/",
    "zeotap": "https://docs.zeotap.com/home/en-us/"
}

def fetch_and_search_docs(query, url):
    """
    Fetches the documentation webpage and searches for relevant content.
    Uses a User-Agent header to avoid bot detection.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an error for 4xx or 5xx status codes

        soup = BeautifulSoup(response.text, "html.parser")

        # Searching for the query in multiple HTML elements
        matches = [tag.get_text() for tag in soup.find_all(["p", "div", "span"]) if query.lower() in tag.get_text().lower()]

        if matches:
            return matches[:3]  # Return up to 3 relevant matches
        else:
            return ["No relevant information found. Please check the official docs."]
    except requests.exceptions.RequestException as e:
        return [f"Error fetching documentation: {str(e)}"]

@app.route("/ask", methods=["POST"])
def ask_question():
    """
    Handles incoming POST requests to search CDP documentation.
    """
    data = request.json
    query = data.get("query", "").strip()

    if not query:
        return jsonify({"error": "Query cannot be empty!"}), 400

    results = {cdp: fetch_and_search_docs(query, url) for cdp, url in CDP_DOCS.items()}

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
