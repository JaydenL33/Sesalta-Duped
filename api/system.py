from country_generator import CountryGenerator
from exceptions import *


class System:

    def __init__(self, country_data):
        self._country_generator = CountryGenerator(country_data)

    def random_country(self):
        selection = self._country_generator.random_country()
        return selection

    def random_countries_including(self, country, amount):
        if amount > len(self._country_generator.all_countries()):
            raise ValueError(amount)
        if type(country) == str:
            country = self.country_from_name(country)
        return self._country_generator.random_countries_including(country, amount)

    # Returns the name, capital or json as specified
    def format_country(self, country_dict, format):
        formatted = None
        if format in ("name", "capital"):
            return country_dict[format]
        elif format in ("json", "", None):
            return country_dict
        else:
            raise FormatNotFoundError

    # Returns a list of names, capitals or dictionaries based on the format
    def format_countries(self, country_list, format):
        formatted_countries = [
            self.format_country(country_dict, format) for country_dict in country_list
        ]
        return formatted_countries

    # Returns a country dictionary given the country's name
    # Raises CountryNotFoundError if not found
    def country_from_name(self, name) -> dict:
        for country in self._country_generator.all_countries():
            if country["name"] == name:
                return country
        else:
            raise CountryNotFoundError(name)
