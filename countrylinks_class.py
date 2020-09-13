import requests


class CountryLinks:

    def __init__(self, url):
        self.i = 0
        self.url = url
        self.resp = requests.get(self.url)
        self.data = self.resp.json()

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.data):
            raise StopIteration
        country_name = self.data[self.i]['name']['official'].replace(' ', '_')
        line = f'{country_name}: https://wikipedia.org/wiki/{country_name}'
        self.i += 1
        return line
