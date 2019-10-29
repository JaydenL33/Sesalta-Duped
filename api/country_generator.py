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

    def next_country(self):
        selection = random.choice(self._countries)
        self._countries.remove(selection)
        return selection
