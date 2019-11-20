from setup import cache
from game import Game
import json
from setup import firebase_session
from wrappers import timer


# @timer
def new_game_id():
    response = firebase_session.child('games').push({})
    return response.key


# @timer
def get_game_data_by_id(game_id):
    cached_game_data = cache.get_game_by_id(game_id)

    if cached_game_data is None:
        return firebase_session.child(f"games/{game_id}").get()
    else:
        return cached_game_data


# @timer
def get_game_by_id(game_id):
    cached_game = Game.from_dict(game_id, cache.get_game_by_id(game_id))

    if cached_game is None:
        return Game.from_dict(game_id, firebase_session.child(f"games/{game_id}").get())
    else:
        return cached_game


# @timer
def get_all_games():
    return firebase_session.child("games/").get()


# @timer
def get_all_game_ids_for_user(user_id):
    return firebase_session.child(f"users/{user_id}/gameIDs/GamesPlayed").get()


# @timer
def update_game(game_id, game):
    game_data = game.to_dict()
    cache.add_game_data(game_id, game_data)
    firebase_session.child(f"games/{game_id}").set(game_data)


# @timer
def get_country_data():
    return firebase_session.child('countryData').get()


# @timer
def get_country_by_index(country_index):
    return cache.get_country_by_index(country_index)
    return firebase_session.child(f'countryData/{country_index}').get()


# @timer
def get_all_users():
    return firebase_session.child('users').get()


# @timer
def get_user_by_id(user_id):
    if user_id is None:
        return None
    else:
        return firebase_session.child("users/" + user_id).get()


# @timer
def update_user(user_id, user_data):
    return firebase_session.child("users" + "/" + user_id).update(user_data)


# @timer
def get_bad_words():
    return firebase_session.child('badWords').get()


# @timer
def update_bad_words(words):
    return firebase_session.child('badWords').set(words)


# @timer
def get_user_trophies(user_id):
    data = firebase_session.child(f"users/{user_id}/trophies").get()
    return data


# @timer
def add_trophies(user_id, trophy):
    firebase_session.child(f"users/{user_id}/trophies").push(trophy)


# @timer
def update_trophies(user_id, trophies):
    firebase_session.child(f"users/{user_id}/trophies").set(trophies)


# @timer
def update_trophies_if_user_exists(user_id, trophies):
    user_data = get_user_by_id(user_id)

    if user_data is not None and trophies is not None:
        update_trophies(user_id, trophies)
        return True
    else:
        return False
