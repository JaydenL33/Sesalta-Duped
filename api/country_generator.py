import random


class CountryGenerator:

    def __init__(self, countries=[]):
        self._countries = countries

    def add_country(self, country):
        self._countries.append(country)

    def all_country_dicts(self):
        country_dicts = []

        for country in self._countries:
            country_dicts.append(country.to_dict())

        return country_dicts

    def random_country(self):
        selection = random.choice(self._countries)
        return selection.to_dict()

    def random_other_options(country, amount):
        countries = {country.to_dict()}

        while len(countries) < amount:
            selection = random_country()
            countries.add(selection.to_dict())

    # def random_nearby_country(country):
    #     random_country = random.choice(self._countries)
    #     print(
    #         f"A random country is being generated! NOT a random nearby country: {random_country.name}")
    #     return random_country

    # Returns a country object given the country's name
    # Returns None if country is not found. Maybe change to an exception
    def _country_from_name(name):
        for country in countries:
            if country.name == name:
                return country
        return None
