from exceptions import *
from flask import Flask, jsonify
import random
from setup import system

app = Flask(__name__)
app.config["DEBUG"] = True

"""

Proposed API format:
    api / v<version> / <subject> / <request> / <format> /

"""


@app.route('/')
def hello_world():
    return 'Hello, World!'

# Returns a random country as json
# Same as random_country_formatted("json")
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
