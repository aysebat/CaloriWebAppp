from selectorlib import Extractor
import requests


class Temperature:
    """Represent a temperature value extracted from the timeanddate.com/weather webpage"""

    headers = {
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }
    base_url = "https://www.timeanddate.com/weather/"
    yml_path = 'temperature.yaml'

    def __init__(self, country, city):
        """if there is a space between the country or city
        replace those with _ """
        self.country = country.replace(" ", "-")
        self.city = city.replace(" ", "-")

    def _build_url(self):
        """Contruct the url with given country and city name and
        return the url"""
        url = self.base_url + self.country + "/" + self.city
        return url

    def _scrape(self):
        """Extracting a value as intructed by the yml file and
        return a dictionary"""
        url = self._build_url()
        r = requests.get(url, headers=self.headers)
        extractor = Extractor.from_yaml_file(self.yml_path)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        """Cleans the output of the _scrapes"""
        scrapped_output = self._scrape()
        clean_output = float(scrapped_output['temp'].replace("\xa0°C", "").strip())
        return clean_output


if __name__ == "__main__":
    temperature = Temperature(country="usa", city="san francisco")
    print(temperature.get())
