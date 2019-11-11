from exceptions import *
from flask import Flask, jsonify, request
import json
import random
from setup import country_system
from flask_cors import CORS
from firebase import firebase

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = True

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


# Helper function to extract the value of an arg from the given args.
# Params:
# args: all args
# param_name: the name of the argument to be returned
# required: determines whether an exception will be raised if the argument
# is not found.
def get_arg(args, param_name, required=False):
    if param_name in args:
        return args[param_name]
    elif required == True:
        raise ParameterNotFoundError(param_name, args)
    else:
        return None

# Returns the id of a new game of Sesalta
# Params:
# given: the given game mode for each question (not yet needed)
# asked_for: the answer mode for each question (not yet needed)
@app.route("/api/country/new_game/")
def new_game():
    args = request.args

    given = get_arg(args, "given", required=False)
    asked_for = get_arg(args, "given", required=False)

    new_game = country_system.new_game(given, asked_for)

    return new_game.id


# Returns a list of jsons for random distinct countries
# that have not been asked about in the given game
# Params:
# id: the game ID. Raises ParameterNotFoundError if not given
# amount: the number of countries requested. Default = 1
@app.route("/api/country/random/")
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
# expected: the NAME_LONG of the correct answer (e.g. "Australia")
# observed: the NAME_LONG of the given answer (e.g. "Canada")
@app.route("/api/country/check/")
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
def get_results():
    args = request.args

    id = get_arg(args, "id", required=True)
    return json.dumps(country_system.get_results(id))



# currently for testing to retrieve firebase data
@app.route("/api/firebase")
def get_firebase():
    fb = firebase.FirebaseApplication('https://geodudes-8f12a.firebaseio.com', None)
    result = fb.get('/', None)
    return result