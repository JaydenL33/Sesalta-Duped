import collections
import copy

MAX_GAMES = 1000


class Cache:

    def __init__(self, country_data=None, bad_words=None):
        self._country_data = country_data
        self._games = collections.OrderedDict()
        self._bad_words = bad_words

    def get_country_data(self):
        return copy.deepcopy(self._country_data)

    def set_country_data(self, country_data):
        # Deepcopy used in case original string is altered later
        self._country_data = copy.deepcopy(country_data)

    def get_country_by_index(self, country_index):
        return self._country_data[country_index]

    def add_game_data(self, game_id, game_data):
        if type(game_data) != dict:
            raise TypeError
        self._games[game_id] = game_data
        self._delete_games_if_max_exceeded(MAX_GAMES)

    def get_game_by_id(self, game_id):
        if game_id in self._games:
            return self._games[game_id]
        else:
            return None

    def _delete_games_if_max_exceeded(self, max_games):
        print(
            f"There are {len(self._games)} cached games (reducing to {MAX_GAMES})")
        while len(self._games) > max_games:
            self._delete_oldest_game(self._games)

    def _delete_oldest_game(self, ordered_dict):
        ordered_dict.popitem(last=False)

    def get_bad_words(self):
        return copy.deepcopy(self._bad_words)

    def set_bad_words(self, bad_words):
        # Deepcopy used in case original string is altered later
        self._bad_words = copy.deepcopy(bad_words)
