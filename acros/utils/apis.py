import requests
from bs4 import BeautifulSoup


def fetch_wikipedia_summary(title: str):
    r = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/" + title)
    r.raise_for_status()
    data = r.json()
    print(data)
    return data["extract"], data["extract_html"], data["timestamp"], data["thumbnail"]["source"]


def get_website_title(url: str) -> str:
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find("title")
    return title.text
