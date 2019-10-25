import random


class CountryGenerator:

    def __init__(self, countries=[]):
        self._countries = countries

    def add_country(self, country):
        self._countries.append(country)

    def all_countries(self) -> list:
        return self._countries

    def random_country(self):
        selection = random.choice(self._countries)
        return selection

    def random_countries_including(self, country, amount):
        countries = [country]

        while len(countries) < amount:
            selection = self.random_country()
            if selection not in countries:
                countries.append(selection)

        return countries

    # Returns a country object given the country's name
    # Returns None if country is not found. Maybe change to an exception
    def country_from_name(name) -> dict:
        for country in countries:
            if country["name"] == name:
                return country
        return None
