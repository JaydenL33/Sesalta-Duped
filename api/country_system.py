from arg_fetcher import get_arg
import copy
from exceptions import *
import firebase_routes
from game import Game
import random
import trophy

# Make ID_RANGE this much larger for release
ID_RANGE = 1000
NAME_LENGTH = 3
ALLOWED_NAME_CHARS = "qwertyuiopasdfghjklzxcvbnm"

ALL_TROPHIES = [
    trophy.GameCompletedTrophy,
    trophy.AllQuestionsCorrectTrophy,
    trophy.NoWrongAnswersTrophy,
    trophy.BronzePointsTrophy
]


class CountrySystem:

    def __init__(self, country_data=None, users=None, games=None):
        self._country_data = country_data  # isn't used anymore
        self._users = users
        if games:
            self._games = games
        else:
            self._games = {}

    # ========================================
    #   Public functions
    # ========================================

    # NOTE: id is stored as a string. This reduces the need for
    # type conversions
    def new_game(self, country_data, given, asked_for):
        game_id = firebase_routes.new_game_id()
        new_game = Game(game_id, country_data, given, asked_for)
        firebase_routes.update_game(game_id, new_game)
        return new_game

    def random_countries(self, game_id, amount):
        game = self._get_game(game_id)
        random_countries = game.choose_random_countries(amount)
        firebase_routes.update_game(game_id, game)
        return random_countries

    # Takes the answer given in a game.
    # Returns true if answer was correct - otherwise False
    # Handles score updates for the question
    # Params:
    # id: the game ID
    # expected: the name of the correct answer (e.g. "Australia")
    # observed: the name of the given answer (e.g. "Canada")
    def check_answer(self, game_id, expected, observed):
        game = self._get_game(game_id)
        response = game.check_answer(expected, observed)
        firebase_routes.update_game(game_id, game)
        return response

    # Returns a list of the results for a game
    def get_results(self, id):
        game = self._get_game(id)
        return game.get_results()

    # add a parameter for user id if needed
    def update_name(self, new_name, old_name, email):
        bad_words = firebase_routes.get_bad_words()       # list of strings

        is_allowed = True

        if new_name is None or email is None or "@" not in email:
            is_allowed = False
        elif len(new_name) != NAME_LENGTH:
            is_allowed = False
        elif new_name.lower() in bad_words:
            is_allowed = False
        else:
            for char in new_name:
                if char.lower() not in ALLOWED_NAME_CHARS:
                    is_allowed = False

        if is_allowed:
            firebase_routes.update_name(
                new_name, old_name, email)

        return is_allowed

    def update_public_scores(name, state):
        return firebase_routes.update_public_scores(name, state)

    def get_trophies_for_game(self, user_id, game_id):
        game = self._get_game(game_id)

        user_data = firebase_routes.get_user_by_id(user_id)
        # print("user_data : ", user_data)

        existing_trophy_data = self._get_existing_trophy_data(user_data)
        existing_trophy_names = self._get_trophy_names(existing_trophy_data)
        new_trophy_data = self._get_new_trophy_data(game, existing_trophy_names)
        # print("\n\nNEW : ", new_trophy_data)

        if existing_trophy_data is None:
            all_earned_trophies = new_trophy_data
        else:
            all_earned_trophies = new_trophy_data + existing_trophy_data

        # Update firebase is the user is valid
        if user_data is not None:
            firebase_routes.update_trophies(
                user_id, all_earned_trophies)

        return new_trophy_data

    def _get_existing_trophy_data(self, user_data):
        if user_data is None:
            existing_trophy_data = None
        else:
            existing_trophy_data = get_arg(user_data, "trophies", required=False)
        return existing_trophy_data

    def _get_trophy_names(self, trophy_data):

        if trophy_data is None or trophy_data == []:
            trophy_names = []
        else:
            trophy_names = [trophy_record["name"]
                            for trophy_record in trophy_data]

        return trophy_names

    def _get_new_trophy_data(self, game, existing_trophy_names):
        new_trophy_data = []

        for trophy in ALL_TROPHIES:
            trophy_test = trophy(game)
            if (trophy_test.get_name() not in existing_trophy_names and
                    trophy_test.game_satisfies()):
                new_trophy_data.append(trophy_test.to_dict())

        return new_trophy_data

    # ========================================
    #   Private functions
    # ========================================

    def _get_game(self, id):
        game = firebase_routes.get_game_by_id(id)
        return game
        # raise GameNotFoundError(id, self._games)
