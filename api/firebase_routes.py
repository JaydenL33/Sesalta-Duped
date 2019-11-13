from setup import firebase_session


def new_game_id():
    response = firebase_session.child('games').push()
    return response.key


def get_game(game_id):
    return firebase_session.child(f"games/{game_id}").get()


def update_game(game_id, new_game_data):
    firebase_session.child(f"games/{game_id}").set(new_game_data)


def get_country_by_index(country_index):
    return firebase_session.child(f'countryData/{country_index}').get()