from country_generator import CountryGenerator
import json
from country_system import CountrySystem

country_data_file = "country_data.json"

with open(country_data_file, "r", encoding="utf-8") as file:
    json_str = str(file.read())

country_data = json.loads(json_str)

country_system = CountrySystem(country_data)
