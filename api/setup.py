from cache import Cache
import json
from firebase_admin import credentials, db
import firebase_admin
import subprocess

subprocess.call(['./env.sh'])  # produce the firebase_key.json from shell env var
# with open("./firebase_key.json", 'r') as fin:
#     print(fin.read())
# Authenticate a credential with the service account
cred = credentials.Certificate("./firebase_key.json")
firebase_admin.initialize_app(
    cred, options={'databaseURL': 'https://geodudes-8f12a.firebaseio.com', })

firebase_session = db.reference()  # This.

country_data = firebase_session.child('countryData').get()

cache = Cache(country_data=country_data)
