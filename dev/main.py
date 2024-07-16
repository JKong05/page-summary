import pandas as pd
from pynytimes import NYTAPI
import os
from dotenv import load_dotenv

load_dotenv()

def nytauth():
    api_key = os.getenv("API_KEY")
    nyt = NYTAPI(api_key, parse_dates=True)

    return nyt

def article_collect(nyt):
    articles = nyt.article_search(
        query="Pfizer", 
        results=40,
        options = {
            "body": [
                "Pfizer",
                "COVID"
            ],
            "headline": [
                "Pfizer",
                "COVID",
                "vaccine"
            ]
        })
    
    filtered_articles = []
    for article in articles:
        title = article.get("headline", {}).get("main", "")
        keywords = [keyword['value'] for keyword in article.get("keywords", [])]
        filtered_articles.append({
            "title": title,
            "keywords": keywords
        })

    articles_df = pd.DataFrame(filtered_articles)
    return articles_df

def main():
    nyt = nytauth()
    articles_df = article_collect(nyt)
    articles_df.to_csv('articles.csv', index=False)


if __name__ == "__main__":
    main()