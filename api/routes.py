from exceptions import *
from flask import Flask, jsonify, request
import json
import random
from setup import system

app = Flask(__name__)
app.config["DEBUG"] = True

"""

Proposed API format:
    api / v<version> / <subject> / <request> / <format> / ?<key>=<value & ...

Example usage:
    /api/v1/countries/random_countries_including/capital/?country=Canada&amount=4
    ^ returns a json list of the capital cities of 4 countries, including Canada.
    This can be used to generate multiple choice answers.

"""

# Returns a random country as json
# Same as calling random_country_formatted("json")
@app.route("/api/v1/countries/random_country/")
def random_country():
    return random_country_formatted("json")


# Returns a property of a random country
# Properties: "name", "capital", "json"
@app.route("/api/v1/countries/random_country/<format>/")
def random_country_formatted(format):
    format = format.lower()
    selection = system.random_country()
    return system.format_country(selection, format)

# Include parameters:
# "country" (country name) and
# "amount" (number of countries including the given one). Default = 4
@app.route("/api/v1/countries/random_countries_including/<format>/")
def random_countries_including_formatted(format):
    args = request.args
    return_str = args

    try:
        chosen_country = args["country"]
    except KeyError:
        raise CountryNotFoundError()

    try:
        amount = int(args["amount"])
    except (TypeError, ValueError, KeyError):
        amount = 4

    countries = system.random_countries_including(chosen_country, amount)
    return json.dumps(system.format_countries(countries, format))
