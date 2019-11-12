from country_generator import CountryGenerator
from country_system import CountrySystem
import firebase_admin
from firebase_admin import credentials, db
import json

# Authenticate a credential with the service account
cred = credentials.Certificate("./firebase_key.json")
firebase_admin.initialize_app(
    cred, options={'databaseURL': 'https://geodudes-8f12a.firebaseio.com', })

firebase_session = db.reference()  # This.

country_data = firebase_session.child('countryData').get()
# print(country_data)

country_system = CountrySystem(country_data)
