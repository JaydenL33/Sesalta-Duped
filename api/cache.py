import collections
import copy

MAX_GAMES = 1000


class Cache:

    def __init__(self, country_data=None, bad_words=None):
        self._country_data = country_data
        self._games = collections.OrderedDict()
        self._bad_words = bad_words

    def get_country_data_copy(self):
        return copy.deepcopy(self._country_data)

    def get_country_by_index(self, country_index):
        return self._country_data[country_index]

    def add_game_data(self, game_id, game_data):
        if type(game_data) != dict:
            raise TypeError
        self._games[game_id] = game_data
        self._delete_games_if_max_exceeded(MAX_GAMES, NUM_GAMES_TO_DELETE)

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
