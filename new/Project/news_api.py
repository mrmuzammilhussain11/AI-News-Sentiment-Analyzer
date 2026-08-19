import requests
import pandas as pd

API_KEY = "cf7a14806954a0e7f609b9fe1a73038a"

def get_news(country="us"):

    url = f"https://gnews.io/api/v4/top-headlines?country={country}&lang=en&max=10&apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    articles = data.get("articles", [])

    news = []

    for article in articles:

        news.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "source": article.get("source", {}).get("name")
        })

    return pd.DataFrame(news)