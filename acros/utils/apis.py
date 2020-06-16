import requests
from bs4 import BeautifulSoup


def fetch_wikipedia_summary(title: str):
    r = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/" + title)
    r.raise_for_status()
    data = r.json()
    print(data)

    r2 = requests.get("https://en.wikipedia.org/api/rest_v1/page/media-list/" + title)
    r2.raise_for_status()
    image_data = r2.json()["items"]
    if len(image_data) > 0:
        image_title = image_data[0]["title"]
        image_caption = image_data[0]["caption"]["text"] if "caption" in image_data else None
    else:
        image_title = image_caption = None
    return (
        data["extract"], data["extract_html"], data["timestamp"],
        data["thumbnail"]["source"] if "thumbnail" in data else None,
        image_title, image_caption
    )


def get_website_title(url: str) -> str:
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find("title")
    return title.text
