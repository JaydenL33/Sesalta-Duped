from country_generator import CountryGenerator
from question import Question


class Game:

    def __init__(self, id, country_data, given, asked_for):
        self._id = id
        self._country_generator = CountryGenerator(country_data)
        self._given_mode = given
        self._asked_for_mode = asked_for
        self._questions = []
        self._isFinished = False

    def choose_random_countries(self, amount):
        num_remaining = len(self._country_generator.remaining_countries)
        if amount > num_remaining:
            raise ValueError(f"Cannot choose {amount} countries with {num_remaining} remaining")

        random_countries = []
        while len(random_countries) < amount:
            random_countries.append(self._country_generator.next_country())

        self._new_question(random_countries)
        return random_countries

    def _new_question(self, countries_used):
        new_question = Question(countries_used)
        self._questions.append(new_question)

    def check_answer(self, expected, observed):
        question = self._questions[-1]
        return question.check_answer(expected, observed, key="name")

    # To be implemented
    def correct_answer_given(self, expected, observed):
        self._questions[-1].correct_answer()

    @property
    def id(self):
        return self._id