import collections

MAX_GAMES = 2
NUM_GAMES_TO_DELETE = 1


class Cache:

    def __init__(self, country_data=None):
        self._country_data = country_data
        self._games = {}

    def get_country_data(self):
        return self._country_data

    def get_country_by_index(self, country_index):
        return self._country_data[country_index]

    def add_game_data(self, game_id, game_data):
        if type(game_data) != dict:
            raise TypeError
        self._games[game_id] = game_data
        # self._delete_games_if_max_exceeded(MAX_GAMES, NUM_GAMES_TO_DELETE)

    def get_game_by_id(self, game_id):
        if game_id in self._games:
            return self._games[game_id]
        else:
            return None

    # def _delete_games_if_max_exceeded(max_games, num_to_delete):
    #     print(f"\n games cached: {self._games}")
    #     printf(f"\n num games:{len(self._games)}")
    #     while len(self._games) >
