# extracts plaintext for the front page of hackernews

import pickle
import requests
from newspaper import Article

def get_top_hn_links():
    top = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()
    parsed_articles = []
    top = top[:30]
    for i, item in enumerate(top):
        print("{}/{}".format(i, len(top)))
        try:
            iurl = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(item)
            md = requests.get(iurl).json()
            url = md['url']
            title = md['title']
            print("have {}".format(title))
            article = Article(url)
            article.download()
            article.parse()
            if len(article.text) < 100:
                continue
            paragraphs = article.text.split("\n\n")
            parsed_article = {"title": title, "text": article.text, "paragraphs": paragraphs}
            parsed_articles.append(parsed_article)
        except Exception as e:
            print(e)
    return parsed_articles

def save(parsed_articles):
    with open("/tmp/parsed_articles.pickle", "wb") as f:
        pickle.dump(parsed_articles, f)

if __name__ == '__main__':
    parsed_articles = get_top_hn_links()
    save(parsed_articles)



