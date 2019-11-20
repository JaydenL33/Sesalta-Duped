from country_generator import CountryGenerator
from exceptions import *
import firebase_routes
from question import Question

MAX_QUESTIONS = 3


class Game:

    def from_dict(id, game_data):
        # print(f"GAME DATA IS: {game_data}")
        country_data = game_data["remainingCountries"]
        given_mode = game_data["mode"].split("-")[0]
        asked_for_mode = game_data["mode"].split(">")[1]

        if "questions" in game_data:
            question_data = game_data["questions"]
            questions = [Question.from_dict(q) for q in question_data]
        else:
            questions = []

        return Game(id, country_data, given_mode, asked_for_mode, questions)

    def __init__(self, id, country_data, given, asked_for, questions=[]):
        self._id = id
        self._country_generator = CountryGenerator(country_data)
        self._given_mode = given
        self._asked_for_mode = asked_for
        self._questions = questions

        firebase_routes.update_game(self._id, self)

    def to_dict(self):
        mode = f"{str(self._given_mode)}->{str(self._asked_for_mode)}"
        questions = self.get_results()
        remaining_countries = self._country_generator.remaining_countries

        return {
            "mode": mode,
            "questions": questions,
            "remainingCountries": remaining_countries
        }

    def choose_random_countries(self, amount):
        if len(self._questions) >= MAX_QUESTIONS:
            raise MaxQuestionsReached(
                f"{len(self._questions)} questions already asked"
            )

        num_remaining = len(self._country_generator.remaining_countries)
        if amount > num_remaining:
            raise ValueError(
                f"Cannot choose {amount} countries with {num_remaining} remaining")

        random_countries = []
        while len(random_countries) < amount:
            random_countries.append(self._country_generator.next_country())

        self._new_question(random_countries)

        firebase_routes.update_game(self._id, self)
        return random_countries

    def _new_question(self, countries_used):
        country_names = [country["name"] for country in countries_used]

        if len(country_names) > 1:
            new_question = Question(country_names, len(
                self._questions), force_answers=True)
        else:
            new_question = Question(country_names, len(
                self._questions), force_answers=False)

        self._questions.append(new_question)

    def check_answer(self, expected, observed):
        # print(self._questions)
        question = self._questions[-1]

        result = question.check_answer(expected, observed)

        firebase_routes.update_game(self._id, self)
        return result

    def get_results(self):
        results = []
        for question in self._questions:
            results.append(question.to_dict())
        return results

    def get_start_time(self, format="datetime"):
        if len(self._questions) == 0:
            return None
        else:
            return self._questions[0].get_time_asked(format=format)

    def is_finished(self):
        # if self._is_finished:
        #     return True
        if len(self._questions) < MAX_QUESTIONS:
            return False
        else:
            for question in self._questions:
                if not question.is_finished:
                    return False
            return True

    def all_questions_correct(self):
        for question in self._questions:
            if not question.answered_correctly():
                return False
        return True

    def has_incorrect_guesses(self):
        for question in self._questions:
            if question.has_incorrect_guesses():
                return True
        return False

    def score(self):
        score = sum([question.points_scored() for question in self._questions])
        return score

    @property
    def id(self):
        return self._id
