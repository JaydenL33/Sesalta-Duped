import random


class CountryGenerator:

    def __init__(self, countries=[]):
        self._remaining_countries = countries

    def random_country(self):
        selection = random.choice(self._remaining_countries)
        return selection

    def next_country(self):
        selection = random.choice(self._remaining_countries)
        self._remaining_countries.remove(selection)
        return selection

    @property
    def remaining_countries(self):
        return self._remaining_countries
