"""
Scrapes temperature based on user input of their location from the web
"""
import requests
from selectorlib import Extractor


class Temperature:
    def __init__(self,country,city):
        self.country = country
        self.city = city

    def get(self):
        # Access the url
        url = f"https://www.timeanddate.com/weather/{self.country}/{self.city}"
        request = requests.get(url)
        content = request.text

        # Scrape web
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_result = extractor.extract(content)

        # Get only the temperature
        temp_result = raw_result['temp']

        # Replace non number values in the string
        result = temp_result.replace(' °C','')

        # Convert to float
        result = float(result)
        return result
    