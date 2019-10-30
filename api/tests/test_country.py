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
    from country_system import CountrySystem

    system_fixture = CountrySystem(countries)
    return system_fixture


class TestRandomCountry:

    def test_random_country(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id
        country = system_fixture.random_countries(id, 1)[0]
        assert country in countries

    def test_random_countries_separate(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id
        random_countries = []

        for i in countries:
            random_country = system_fixture.random_countries(id, 1)
            assert random_country not in random_countries
            random_countries.append(random_country)

    def test_random_countries_together(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id
        random_countries = system_fixture.random_countries(id, 4)
        for index, country in enumerate(random_countries[:-1]):
            assert country not in random_countries[index + 1:]


class TestCheckAnswer:

    def testCorrectSingleAnswer(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id

        answer = system_fixture.random_countries(id, 1)[0]
        answer_name = answer["name"]
        assert system_fixture.check_answer(id, answer_name, answer_name) == 1

    def testCorrectWithMultipleAnswers(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id

        answer = system_fixture.random_countries(id, 4)[2]
        answer_name = answer["name"]
        assert system_fixture.check_answer(id, answer_name, answer_name) == 1

    def testIncorrectSingleAnswer(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id

        answer = system_fixture.random_countries(id, 1)[0]
        answer_name = answer["name"]
        assert system_fixture.check_answer(id, answer_name, "Zimbabwe") == 0

    def testIncorrectMultipleAnswer(self, system_fixture):
        game = system_fixture.new_game(None, None)
        id = game.id

        options = system_fixture.random_countries(id, 3)
        expected_answer_name = (options[0])["name"]
        given_answer_name = (options[1])["name"]
        assert system_fixture.check_answer(id, expected_answer_name, given_answer_name) == 0
