import urllib.request
from urllib import parse

class BaseScraper:

    url = ""
    headers = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def __init__(self, url):
        self.url = url

    def get_HTML_data(self):
        req = urllib.request.Request(self.url, headers = self.headers)
        response = urllib.request.urlopen(req)
        return response
