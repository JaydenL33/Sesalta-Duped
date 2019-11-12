from country_generator import CountryGenerator
from country_system import CountrySystem
from firebase import firebase
import json

fb = firebase.FirebaseApplication(
    'https://geodudes-8f12a.firebaseio.com/', None)
country_data = fb.get('/countryData', None)

country_system = CountrySystem(country_data)
