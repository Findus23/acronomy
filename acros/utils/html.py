from bs4 import BeautifulSoup


def clean_html(html: str) -> str:
    return BeautifulSoup(html, "html.parser").text


def string_to_bool(string: str) -> bool:
    return string.lower() in ["true"]
