from arg_fetcher import get_arg
from country_system import CountrySystem
from datetime import datetime
from exceptions import *
from flask import Flask, jsonify, request
import json
import firebase_routes
from flask_cors import CORS
from wrappers import timer

app = Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

SUCCESS = '1'
FAILURE = '0'

country_system = CountrySystem()

"""

Proposed API format:
    api / <subject> / <request> / ?<key>=<value> & ...

Example usage:

    /api/country/random/?amount=4&id=1234
    ^ Returns a json list of 4 countries not yet used in game number 1234.
    ^ This can be used to generate multiple choice answers.

    /api/country/check/?expected=australia&observed=canada&id=1234
    ^ Checks if the observed answer (Canada) matches the expected (Australia)
    ^ and returns "1" or "0". Game score will also be updated as needed.

"""

# NOTE: The functions used by this route are not complete.
# Names can't be updated yet since users don't exist. Raycole will add this.
# Prasad suggested using public name as a unique key. This isn't implemented yet.
#
# Will update the user's public name IF it is valid (3 letters, not profane).
# Returns "1" if update is successful, otherwise "0"
# Params:
# name: the desired public name
# Needs some kind of user id included as well

# Must give new name as param "name"
# Must give either "email". This is unique between users and is used for verification
# Give existing name as parm "old" if the user already has a public name
@app.route("/api/user/update_name/")
@timer
def update_user():
    args = request.args
    new_name = get_arg(args, "name", required=True)
    old_name = get_arg(args, "old", required=False)
    email = get_arg(args, "email", required=True)

    # TODO: finish country_system.update_name()
    name_was_updated = country_system.update_name(
        new_name, old_name, email)
    if name_was_updated:
        return SUCCESS
    else:
        return FAILURE


@app.route("/api/user/public/")
@timer
def update_public_scores():
    args = request.args
    name = get_arg(args, "name", required=True)
    requested_state = get_arg(args, "new", required=True)

    success_status = country_system.update_public_scores(name, requested_state)

    if success_status:
        return SUCCESS
    else:
        return FAILURE


# Don't use this!
# @app.route("/api/user/new/")
# @timer
# def new_user():
#     args = request.args
#
#     user_id = get_arg(args, "user_id", required=True)


# Returns the id of a new game of Sesalta
# Params:
# given: the given game mode for each question (not yet needed)
# asked_for: the answer mode for each question (not yet needed)
@app.route("/api/country/new_game/", methods=['GET'])
@timer
def new_game():
    args = request.args

    given = get_arg(args, "given", required=True)
    asked_for = get_arg(args, "asked_for", required=True)
    users_unique_name = get_arg(args, "users_unique_name", required=True)

    country_data = firebase_routes.get_country_data()     # list of jsons

    new_game = country_system.new_game(country_data, given, asked_for)

    # pass in the logged in players name or the string not_a_user

    # users_unique_name = get_arg(args, "users_unique_name", required=True)
    update_user_data(users_unique_name, new_game.id)

    print("NEW GAME ID:", new_game.id, type(new_game.id))
    return new_game.id


# Returns a list of jsons for random distinct countries
# that have not been asked about in the given game
# Params:
# id: the game ID. Raises ParameterNotFoundError if not given
# amount: the number of countries requested. Default = 1
@app.route("/api/country/random/")
@timer
def random_countries():
    args = request.args

    id = get_arg(args, "id", required=True)
    amount = int(get_arg(args, "amount", required=False, default=1))
    return json.dumps(country_system.random_countries(id, amount))


# Takes the answer given in a game.
# Returns: string "1" if answer was correct. Otherwise string "0"
# Handles score updates for the question
# Params:
# id: the game ID
# expected: the NAME_LONG of the correct answer(e.g. "Australia")
# observed: the NAME_LONG of the given answer(e.g. "Canada")
@app.route("/api/country/check/")
@timer
def check_country():
    args = request.args
    id = get_arg(args, "id", required=True)
    expected = get_arg(args, "expected", required=True)
    observed = get_arg(args, "observed", required=True)

    return str(country_system.check_answer(id, expected, observed))

# Returns a list containing a JSON for each question that has been asked.
# JSON contains keys:
# "question_num": an integer from 0-9 inclusive. Should be the same as that
# JSON's index in the list.
# "expected_answer": The NAME_LONG of the expected answer
# "observed_answers": The NAME_LONGs of the observed answers
# "points": the number of points scored for that question.
# "potential": the maximum number of points that could be scored in that question.
@app.route("/api/country/results/")
@timer
def get_results():
    args = request.args
    id = get_arg(args, "id", required=True)

    return json.dumps(country_system.get_results(id))


@app.route("/api/user/get_id/")
@timer
def get_id_from_email():
    args = request.args
    email = get_arg(args, "email", required=True)

    return firebase_routes.get_user_id_by_email(email)


# tested and working, just need to uncomment out the args stuff and delete the hardcoded name
# just need to json.parse in the frontend
@app.route("/api/getPlayersScoreboard/",  methods=['GET'])
@timer
def get_players_scoreboard():
    args = request.args
    name = get_arg(args, "name", required=True)
    data = extract_games_and_score_for_user(name)
    return json.dumps(data)


@app.route("/api/getGlobalLeaderboard/",  methods=['GET'])
@timer
def get_global_scoreboard():
    all_users_with_games_and_scores = retrieve_all_users_with_games_and_scores()
    return json.dumps(all_users_with_games_and_scores)


# This function also needs to be updated to handle user accounts/user IDs properly
# NOTE: This is /game/trophies, not /user/trophies
# Lists the new trophies a user earned in a game. Also updates DB to match.
# If this route is called twice for the same game, it will give a valid answer
# the first time but nothing the second time (since it only considers NEW trophies)
@app.route("/api/game/trophies/")
@timer
def get_game_trophies():
    args = request.args
    user_id = get_arg(args, "user", required=False)
    game_id = get_arg(args, "game", required=True)

    trophies = country_system.get_trophies_for_game(user_id, game_id)

    return json.dumps(trophies)

# This function also needs to be updated to handle user accounts/user IDs properly
# NOTE: This is /user/trophies, not /game/trophies
# Lists all of the trophies a user has earned
@app.route("/api/user/trophies/")
@timer
def get_user_trophies():
    args = request.args
    user_id = get_arg(args, "user", required=True)

    return json.dumps(firebase_routes.get_user_trophies(user_id), sort_keys=True)


@app.route("/api/getGlobalLeaderboardForParticularGameMode/",  methods=['GET'])
@timer
def get_global_board_for_game_mode():
    args = request.args
    game_id = get_arg(args, "game_id", required=True)
    game_data = firebase_routes.get_game_data_by_id(game_id)
    mode = game_data['mode']
    all_users_with_games_and_scores = retrieve_all_users_with_games_and_scores()
    filtered_games_and_scores = filter_games_by_mode(
        all_users_with_games_and_scores, mode)
    return json.dumps(filtered_games_and_scores)


@app.route("/api/rank_rival_and_distance_to_rival/", methods=['GET'])
def rankRivalAndDistanceToRival():
    args = request.args
    game_id = get_arg(args, "game_id", required=True)
    user_name = get_arg(args, "user_name", required=True)

    all_users_with_games_and_scores = retrieve_all_users_with_games_and_scores()
    all_games = firebase_routes.get_all_games()
    all_user_data = firebase_routes.get_all_users()

    mode_of_this_game = mode_string_to_id(all_games[game_id]["mode"])

    all_users_names = list(all_users_with_games_and_scores.keys())

    rank_list_of_relevant_game_data = []

    for users_name in all_users_names:
        games_played_by_user = all_users_with_games_and_scores[users_name]
        for gameName in games_played_by_user:
            game_data = all_users_with_games_and_scores[users_name][gameName]
            if game_data['Mode'] == mode_of_this_game:
                rank_list_of_relevant_game_data.append(
                    {"name": users_name, "score": game_data["Score"], "gameID":  all_user_data[users_name]["gameIDs"]["gamesPlayed"][gameName]})

    sorted_rank_list_of_relevant_game_data = sorted(
        rank_list_of_relevant_game_data, key=lambda k: k['score'], reverse=True)
    this_game_rank = 1
    this_game_score = 0
    for relevant_game_data in sorted_rank_list_of_relevant_game_data:
        if relevant_game_data["gameID"] == game_id:
            this_game_score = relevant_game_data["score"]
            break
        this_game_rank += 1

    your_highest_game_rank = 1
    for relevant_game_data in sorted_rank_list_of_relevant_game_data:
        if relevant_game_data["name"] == user_name:
            break
        your_highest_game_rank += 1

    print(sorted_rank_list_of_relevant_game_data)
    print(your_highest_game_rank)
    print(this_game_rank)
    string_to_return = "You placed Number " + str(this_game_rank) + " out of " + str(
        len(sorted_rank_list_of_relevant_game_data)) + " on the World leaderboard. "
    if your_highest_game_rank <= 10:
        print("dis")
        if your_highest_game_rank == this_game_rank:
            if this_game_rank == 1:
                string_to_return += "You are the global leader. Congratulations!"
            else:
                string_to_return += rival_finder(sorted_rank_list_of_relevant_game_data,
                                                 user_name, this_game_rank-2, this_game_score, "")
        else:
            if your_highest_game_rank == 1:
                string_to_return += "You still remain the global leader with a score of " + \
                    str(sorted_rank_list_of_relevant_game_data[0]
                        ["score"]) + ". Congratulations!"
            else:
                string_to_return += "You are still " + str(your_highest_game_rank) + " out of " + str(
                    len(sorted_rank_list_of_relevant_game_data)) + " on the World leaderboard. "
                string_to_return += rival_finder(sorted_rank_list_of_relevant_game_data,
                                                 user_name, your_highest_game_rank-2, this_game_score, "")
    else:
        print("make")
        string_to_return += "Try to aim for the top 10 next time!"

    return json.dumps({"rival_info": string_to_return})


# Helper functions - may be relocated


def retrieve_all_users_with_games_and_scores():
    all_users_data = firebase_routes.get_all_users()
    users_names = list(all_users_data.keys())
    all_users_with_games_and_scores = {}
    for users_name in users_names:
        all_users_with_games_and_scores[users_name] = extract_games_and_score_for_user(
            users_name)

    return all_users_with_games_and_scores


def extract_games_and_score_for_user(name):
    user_data = firebase_routes.get_user_by_id(name)
    game_count = user_data['gameIDs']['gameCount']

    if game_count == 0:
        return {}
    else:
        games_played = user_data['gameIDs']['gamesPlayed']
        game_number_and_score = {}

        for game_name, game_id in games_played.items():
            game_data = firebase_routes.get_game_data_by_id(game_id)
            game_number_and_score[game_name] = calculate_mode_score_and_date(
                game_data)

        return game_number_and_score


def calculate_mode_score_and_date(game_data):
    data = {}
    data["Mode"] = mode_string_to_id(game_data['mode'])
    data["Date"] = game_data['questions'][0]['time_asked']
    data["Score"] = 0
    for question in game_data['questions']:
        data["Score"] += question['points']
    return data


def filter_games_by_mode(all_users_with_games_and_scores, mode):
    name_list = list(all_users_with_games_and_scores.keys())
    filtered_games_and_scores_by_mode = {}
    for name in name_list:
        game_names = list(all_users_with_games_and_scores[name].keys())
        for game_name in game_names:
            if all_users_with_games_and_scores[name][game_name]["Mode"] == mode:
                if name not in filtered_games_and_scores_by_mode:
                    filtered_games_and_scores_by_mode[name] = {}
                if game_name not in filtered_games_and_scores_by_mode[name]:
                    filtered_games_and_scores_by_mode[name][game_name] = {}
                filtered_games_and_scores_by_mode[name][game_name] = all_users_with_games_and_scores[name][game_name]
    return filtered_games_and_scores_by_mode


def mode_string_to_id(mode_string):
    mode_map = {'Country->Map': 0, 'Map->Country': 1,
                'Capital->Country': 2, 'Country->Capital': 3, 'Flag->Country': 4}
    return mode_map[mode_string]


def update_user_data(user_name, new_game_id):
    if "not_a_user" == user_name:
        return
    user_data = firebase_routes.get_user_by_id(user_name)
    total_games_played = user_data["gameIDs"]["gameCount"] + 1
    game_number_string = "Game" + str(total_games_played)
    user_data["gameIDs"]["gameCount"] = total_games_played
    if "gamesPlayed" not in user_data["gameIDs"]:
        user_data["gameIDs"]["gamesPlayed"] = {}
    user_data["gameIDs"]["gamesPlayed"][game_number_string] = new_game_id

    firebase_routes.update_user(user_name, user_data)


def rival_finder(sorted_list, this_user_name, index, this_game_score, return_string):
    print(index)
    if sorted_list[index]["name"] == this_user_name:
        if index == 0:
            return_string = "You are still the global leader!"
        else:
            return_string = rival_finder(
                sorted_list, this_user_name, index-1, this_game_score, return_string)
    else:
        return_string = "Your Rival is World Number " + \
            str(index+1) + " " + sorted_list[index]["name"] + ". Defeat them by getting " + str(
                sorted_list[index]["score"]-this_game_score) + " more points."

    return return_string
