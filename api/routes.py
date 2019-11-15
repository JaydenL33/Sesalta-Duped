from arg_fetcher import get_arg
from country_system import CountrySystem
from exceptions import *
from flask import Flask, jsonify, request
import json
from setup import firebase_session
from flask_cors import CORS

application = Flask(__name__)
CORS(application)
application.config["DEBUG"] = True

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


# Returns the id of a new game of Sesalta
# Params:
# given: the given game mode for each question (not yet needed)
# asked_for: the answer mode for each question (not yet needed)
@application.route("/api/country/new_game/", methods=['GET'])
def new_game():
    args = request.args

    given = get_arg(args, "given", required=False)
    asked_for = get_arg(args, "given", required=False)
    country_data = get_firebase_data('countryData')     # list of jsons

    new_game = country_system.new_game(country_data, given, asked_for)
    print(new_game.id, type(new_game.id))
    return new_game.id
    # return json.dumps(new_game.id)


# Returns a list of jsons for random distinct countries
# that have not been asked about in the given game
# Params:
# id: the game ID. Raises ParameterNotFoundError if not given
# amount: the number of countries requested. Default = 1
@application.route("/api/country/random/")
def random_countries():
    args = request.args

    id = get_arg(args, "id", required=True)
    if "amount" in args:
        amount = int(get_arg(args, "amount", required=False))
    else:
        amount = 1
    return json.dumps(country_system.random_countries(id, amount))


# Takes the answer given in a game.
# Returns: string "1" if answer was correct. Otherwise string "0"
# Handles score updates for the question
# Params:
# id: the game ID
# expected: the NAME_LONG of the correct answer(e.g. "Australia")
# observed: the NAME_LONG of the given answer(e.g. "Canada")
@application.route("/api/country/check/")
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
@application.route("/api/country/results/")
def get_results():
    args = request.args
    id = get_arg(args, "id", required=True)

    return json.dumps(country_system.get_results(id))


# NOTE: The functions used by this route are not complete.
# Names can't be updated yet since users don't exist. Raycole will add this.
#
# Will update the user's public name IF it is valid (3 letters, not profane).
# Returns "1" if update is successful, otherwise "0"
# Params:
# name: the desired public name
# (probably needs a user id included as well)
@application.route("/api/user/update/")
def update_name():
    args = request.args
    name = get_arg(args, "name", required=True)

    bad_words = get_firebase_data('badWords')       # list of strings

    # TODO: finish country_system.update_name()
    name_was_updated = country_system.update_name(name, bad_words)
    if name_was_updated:
        return SUCCESS
    else:
        return FAILURE
    return country_system.update_name(name, bad_words)

# Helper function (should probs be moved to another file)


def get_firebase_data(path):
    path = path.strip("/")
    return firebase_session.child(path).get()



# tested and working, just need to uncomment out the args stuff and delete the hardcoded name
# just need to json.parse in the frontend
@application.route("/api/getPlayersScoreboard/",  methods=['GET'])
def get_players_scoreboard():
    # args = request.args
    # name = get_arg(args, "user", required=True)

    name = "prasadsuniquename"
    data = extract_games_and_score_for_user(name)
    return json.dumps(data)


@application.route("/api/getGlobalLeaderboard/",  methods=['GET'])
def get_global_scoreboard():
    all_users_data = firebase_session.child("users" + "/").get()
    users_names = list(all_users_data.keys())
    all_users_with_games_and_scores = {}
    for users_name in users_names:
        all_users_with_games_and_scores[users_name] = extract_games_and_score_for_user(users_name)
        
    return json.dumps(all_users_with_games_and_scores)


def extract_games_and_score_for_user(name):
    user_data = firebase_session.child("users/" + name).get()
    game_count = user_data['gameIDs']['GameCount']
    if game_count == 0:
        return {}
    else:
        games_played = user_data['gameIDs']['GamesPlayed']
        game_id_list = list(games_played.keys())
        game_number_and_score = {}

        for game_id in game_id_list:
            game_data = firebase_session.child("games" + "/" + games_played[game_id]).get()
            game_number_and_score[game_id] = calculateModeScoreAndDate(game_data)
            
        # game_number_and_score_sorted = sorted(game_number_and_score.items(), key=lambda kv: kv[1], reverse=True)
        return game_number_and_score

def calculateModeScoreAndDate(game_data):
    data = {}
    print(game_data)
    data["Mode"] = game_data['mode']
    data["Date"] = 0
    data["Score"] = 0
    for question in game_data['questions']:
        data["Score"] += question['points']
    return data









# tested and working, just need to change  methods=['GET'] to  methods=['POST'] and uncomment player and score
# returns string "done" once db has finished updating
# can refactor but going to sleep now
# @application.route("/api/pushPlayerAndScoreToLeaderboard/",  methods=['GET'])
# def push_player_and_score_to_leaderboard():

#     player = "raydai"
#     score = 250

#     # player = request.form.get('player')
#     # score = request.form.get('score')

#     playerData = firebase_session.child("userLeaderboard" + "/" + player).get()

#     if playerData == None:
#         firebase_session.child("userLeaderboard" + "/" + player).update(
#             {"GameCount": 1, "GamesPlayed": {"Game1": int(score)}})
#         return "done"

#     this_game_count = playerData["GameCount"] + 1

#     firebase_session.child("userLeaderboard" + "/" +
#                            player).update({"GameCount": int(this_game_count)})
#     this_game = "Game" + str(this_game_count)

#     currentScores = playerData["GamesPlayed"]
#     keysList = list(currentScores.keys())

#     if len(keysList) >= 5:
#         data = extractGameNumberAndLowestScore(currentScores)
#         if data["score"] <= score:
#             firebase_session.child("userLeaderboard" + "/" +
#                                    player + "/GamesPlayed/" + data["game"]).delete()
#             firebase_session.child(
#                 "userLeaderboard" + "/" + player + "/GamesPlayed").update({this_game: int(score)})
#     else:
#         firebase_session.child(
#             "userLeaderboard" + "/" + player + "/GamesPlayed").update({this_game: int(score)})

#     return "done"


# def extractGameNumberAndLowestScore(currentScores):
#     currentScoresSorted = sorted(currentScores.items(), key=lambda kv: kv[1])
#     return {"game": currentScoresSorted[0][0], "score": currentScoresSorted[0][1]}
