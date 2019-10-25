import os
import pytest
import sys

# sys.path.append() must run before system.System is imported
sys.path.append(os.getcwd())

# Use 4 countries for more predictable tests with randomness
country1 = {
    "name": "Australia",
    "capital": "Canberra"
}

country2 = {
    "name": "Belgium",
    "capital": "Brussels"
}

country3 = {
    "name": "Canada",
    "capital": "Ottawa"
}

country4 = {
    "name": "Denmark",
    "capital": "Copenhagen"
}

countries = [country1,
             country2,
             country3,
             country4]
country_names = [country["name"] for country in countries]
country_capitals = [country["capital"] for country in countries]

@pytest.fixture
def system_fixture():
    # system.System MUST be imported after sys.path.append() code runs
    # to allow pythonpath to update
    from system import System

    system = System(countries)
    return system


class TestRandomCountry:

    def test_random_country(self, system_fixture):
        country = system_fixture.random_country()
        assert country in countries

    def test_random_country_name(self, system_fixture):
        country = system_fixture.random_country()
        country_name = system_fixture.format_country(country, "name")
        assert country_name in country_names

    def test_random_country_capital(self, system_fixture):
        country = system_fixture.random_country()
        capital = system_fixture.format_country(country, "capital")
        assert capital in country_capitals

    def test_random_countries_including(self, system_fixture):
        chosen_country = country1
        country_list = system_fixture.random_countries_including(country1, 4)
        assert len(country_list) == 4
        assert len(country_list) == len(set([str(country) for country in country_list]))
        for country in country_list:
            assert country in countries
