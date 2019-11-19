from setup import firebase_session
import json


def new_game_id():
    response = firebase_session.child('games').push({})
    return response.key


def get_game_by_id(game_id):
    return firebase_session.child(f"games/{game_id}").get()


def get_all_games():
    return firebase_session.child("games/").get()


def get_all_game_ids_for_user(user_id):
    return firebase_session.child(f"users/{user_id}/gameIDs/GamesPlayed").get()


def update_game(game_id, new_game_data):
    firebase_session.child(f"games/{game_id}").set(new_game_data)


def get_country_data():
    return firebase_session.child('countryData').get()


def get_country_by_index(country_index):
    return firebase_session.child(f'countryData/{country_index}').get()


def get_all_users():
    return firebase_session.child('users').get()


def get_user_by_id(id):
    return firebase_session.child("users/" + id).get()


def get_bad_words():
    return firebase_session.child('badWords').get()


def update_bad_words(words):
    return firebase_session.child('badWords').set(words)


def get_user_trophies(user_id):
    data = firebase_session.child(f"users/{user_id}/trophies").get()
    return data


def add_trophies(user_id, trophy):
    firebase_session.child(f"users/{user_id}/trophies").push(trophy)


def update_trophies(user_id, trophies):
    firebase_session.child(f"users/{user_id}/trophies").set(trophies)


def update_trophies_if_user_exists(user_id, trophies):
    user_data = get_user_by_id(user_id)

    if user_data is not None and trophies is not None:
        update_trophies(user_id, trophies)
        return True
    else:
        return False
