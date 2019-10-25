from country_generator import CountryGenerator
import json
from system import System

country_data_file = "country_data.json"

with open(country_data_file, "r", encoding="utf-8") as file:
    json_str = str(file.read())

country_data = json.loads(json_str)

system = System(country_data)
