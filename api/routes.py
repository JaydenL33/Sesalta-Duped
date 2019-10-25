from flask import Flask, jsonify
from setup import country_gen

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/api/v1/countries/random')
def random_country():
    selection = country_gen.random_country()
    return (selection)
