import copy
from exceptions import *
from game import Game
import random

# Make ID_RANGE this much larger for release
ID_RANGE = 1000


class CountrySystem:

    def __init__(self, country_data):
        self._country_data = country_data
        self._games = {}

    # ========================================
    #   Public functions
    # ========================================

    # NOTE: id is stored as a string. This reduces the need for
    # type conversions
    def new_game(self, given, asked_for):
        new_id = str(self._generate_new_id())
        country_data_copy = copy.deepcopy(self._country_data)
        new_game = Game(new_id, country_data_copy, given, asked_for)

        self._games[new_id] = new_game
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
