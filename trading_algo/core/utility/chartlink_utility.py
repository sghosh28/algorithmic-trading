import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


def chartlink_utility(_filter):
    """
    This function is used to get the list of stocks according to the filter from
    chartlink
    """
    scan_clause = _filter.scan_clause
    url = _filter.url
    post_url = _filter.post_url

    data = {
    'scan_clause': scan_clause,
    }

    with requests.Session() as s:
        r = s.get(url)
        soup = bs(r.content, 'lxml')
        s.headers['X-CSRF-TOKEN'] = soup.select_one('[name=csrf-token]')['content']
        r = s.post(post_url, data=data).json()
        #print(r.json())
        print(r['data'])
        # df = pd.DataFrame(r['data'])
        # print(df)
        return r['data']