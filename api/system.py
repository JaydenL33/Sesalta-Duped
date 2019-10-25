from country_generator import CountryGenerator


class System:

    def __init__(self, country_data):
        self._country_generator = CountryGenerator(country_data)

    def random_country(self):
        selection = self._country_generator.random_country()
        return selection

    def random_countries_including(self, country, amount):
        if type(country) == str:
            country = self.country_from_name(country)
        return self._country_generator.random_countries_including(country, amount)

    def format_country(self, country_dict, format):
        formatted = None
        if format in ("name", "capital"):
            return country_dict[format]
        elif format in ("json", "", None):
            return country_dict
        else:
            raise FormatNotFoundError
