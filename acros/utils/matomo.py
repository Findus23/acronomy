from datetime import date

import requests

from acronomy.settings import MATOMO_API_KEY


def fetch_matomo_pages():
    url = "https://matomo.lw1.at/index.php" \
          "?period=range" \
          "&date=2010-01-01," + str(date.today()) + \
          "&filter_limit=-1" \
          "&flat=1" \
          "&format=JSON" \
          "&idSite=29" \
          "&method=Actions.getPageUrls" \
          "&module=API" \
          f"&token_auth={MATOMO_API_KEY}"
    print(url)
    r = requests.get(url)
    return r.json()
