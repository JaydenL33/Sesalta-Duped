import copy
from exceptions import *
from setup import firebase_session
import firebase_routes
from game import Game
import random

# Make ID_RANGE this much larger for release
ID_RANGE = 1000
NAME_LENGTH = 3
ALLOWED_NAME_CHARS = "qwertyuiopasdfghjklzxcvbnm"


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
        id = firebase_routes.new_game_id()
        new_game = Game(id, country_data, given, asked_for)
        return new_game

    def random_countries(self, id, amount):
        game = self._get_game(id)
        random_countries = game.choose_random_countries(amount)
        return random_countries

    # Takes the answer given in a game.
    # Returns true if answer was correct - otherwise False
    # Handles score updates for the question
    # Params:
    # id: the game ID
    # expected: the name of the correct answer (e.g. "Australia")
    # observed: the name of the given answer (e.g. "Canada")
    def check_answer(self, id, expected, observed):
        game = self._get_game(id)
        return game.check_answer(expected, observed)

    # Returns a list of the results for a game
    def get_results(self, id):
        game = self._get_game(id)
        return game.get_results()

    # add a parameter for user id if needed
    def update_name(self, new_name, bad_words):
        is_allowed = True

        if len(new_name) != NAME_LENGTH:
            is_allowed = False

        for char in new_name:
            if char.lower() not in ALLOWED_NAME_CHARS:
                is_allowed = False

        if new_name.lower() in bad_words:
            is_allowed = False

        if is_allowed:
            # TODO: update the user's name
            pass

        return is_allowed

        # ========================================
        #   Private functions
        # ========================================

        # ISSUE: Currently, this function will hang when too many games are in
        # progress. We will need to implement a way to remove the oldest/completed
        # games.

    def _generate_new_id(self):
        id = str(random.randrange(ID_RANGE))
        while id in self._games:
            id = str(random.randrange(ID_RANGE))
        return id

    def _get_game(self, id):
        if id in self._games:
            return self._games[id]
        else:
            raise GameNotFoundError(id, self._games)
