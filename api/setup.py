from country import Country
from country_generator import CountryGenerator

# Just a placeholder - add all countries from map_dump.json
countries = [
    Country("Australia", "Canberra", None),
    Country("Austria", "Vienna", None),
    Country("Solomon Islands", "Honiara", None),
    Country("Serbia", "Belgrade", None),
    Country("Sweden", "Stockholm", None),
    Country("Chad", "N'Djamena", None),
    Country("Indonesia", "Jakarta", None),
    Country("United Kingdom", "London", None)
]

country_gen = CountryGenerator(countries)
