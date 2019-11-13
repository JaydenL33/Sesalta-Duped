import firebase_routes
import random


class CountryGenerator:

    def __init__(self, countries=[]):
        if len(countries) >= 1 and type(countries[0]) != int:
            self._remaining_country_indices = [
                index for index, value in enumerate(countries)]
        else:
            self._remaining_country_indices = countries

    def random_country(self):
        selection = random.choice(self._remaining_country_indices)
        return firebase_routes.get_country_by_index(selection)

    def next_country(self):
        index = random.choice(self._remaining_country_indices)
        self._remaining_country_indices.remove(index)
        return firebase_routes.get_country_by_index(index)

    @property
    def remaining_countries(self):
        return self._remaining_country_indices
