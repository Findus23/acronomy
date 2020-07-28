from typing import Tuple, Optional

import requests
from bs4 import BeautifulSoup

from acros.utils.html import clean_html, string_to_bool


class NotFoundError(FileNotFoundError):
    """Request could not be found in API"""
    pass


class WikipediaAPISummary:
    urlbase = "https://en.wikipedia.org/api/rest_v1/page/summary/"

    def __init__(self, title: str):
        r = requests.get(self.urlbase + title)
        try:
            r.raise_for_status()
        except requests.HTTPError:
            raise NotFoundError("Wikipedia API returns error")
        self.data = r.json()

    @property
    def title(self) -> str:
        return self.data["title"]

    @property
    def extract(self) -> str:
        return self.data["extract"]

    @property
    def extract_html(self) -> str:
        return self.data["extract_html"]

    @property
    def description(self) -> str:
        if "description" in self.data:
            return self.data["description"]

    @property
    def timestamp(self) -> str:
        return self.data["timestamp"]

    @property
    def image(self) -> Optional[str]:
        if "originalimage" in self.data:
            return self.data["originalimage"]["source"]


def get_website_title(url: str) -> str:
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, features="html.parser")
    title = soup.find("title")
    return title.text


class WikipediaImageAPIObject:
    def __init__(self, filename: str):
        self.filename = filename
        print(self.api_url)
        r = requests.get(self.api_url)
        r.raise_for_status()
        self.data = r.json()
        self.image_obj = list(self.data["query"]["pages"].values())[0]
        if "imageinfo" not in self.image_obj:
            raise NotFoundError()

    @classmethod
    def from_url(cls, url: str):
        return cls(url.split("/")[-1])

    @property
    def api_url(self):
        return "https://commons.wikimedia.org/w/api.php" \
               "?action=query" \
               "&format=json" \
               f"&titles=File:{self.filename}" \
               "&prop=imageinfo" \
               "&iiprop=extmetadata|size|url|timestamp" \
               "&iiurlwidth=500"

    @property
    def pageid(self) -> int:
        return self.image_obj["pageid"]

    @property
    def imageinfo(self):
        return self.image_obj["imageinfo"][0]

    @property
    def timestamp(self) -> str:
        return self.imageinfo["timestamp"]

    @property
    def thumb_size(self) -> Tuple[int, int]:
        return self.imageinfo["thumbwidth"], self.imageinfo["thumbheight"]

    @property
    def url(self) -> str:
        return self.imageinfo["url"]

    @property
    def thumburl(self) -> str:
        return self.imageinfo["thumburl"]

    @property
    def extmetadata(self):
        return self.imageinfo["extmetadata"]

    @property
    def image_description(self) -> str:
        return clean_html(self.extmetadata["ImageDescription"]["value"])

    @property
    def credit(self) -> Optional[str]:
        if "Credit" in self.extmetadata:
            return clean_html(self.extmetadata["Credit"]["value"])

    @property
    def artist(self) -> Optional[str]:
        if "Artist" in self.extmetadata:
            return clean_html(self.extmetadata["Artist"]["value"])

    @property
    def license_short_name(self) -> str:
        return self.extmetadata["LicenseShortName"]["value"]

    @property
    def license_url(self) -> Optional[str]:
        if "LicenseUrl" in self.extmetadata:
            return self.extmetadata["LicenseUrl"]["value"]

    @property
    def attribution_required(self) -> bool:
        return string_to_bool(self.extmetadata["AttributionRequired"]["value"])

    @property
    def copyrighted(self) -> bool:
        return string_to_bool(self.extmetadata["Copyrighted"]["value"])

    @property
    def attribution(self) -> Optional[str]:
        if "Attribution" in self.extmetadata:
            return self.extmetadata["Attribution"]["value"]
