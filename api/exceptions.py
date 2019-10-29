class FormatNotFoundError(Exception):
    def __init__(self):
        super()


class CountryNotFoundError(Exception):
    def __init__(self, country=None):
        super()
        print(f"Could not find {'(' + country + ')' if country else ''} in country list")


class ParameterNotFoundError(Exception):
    def __init__(self, param=None, args=None):
        super()
        print(f"Could not find parameter {'(' + param + ')' if param else ''} in parameters {args}")


class GameNotFoundError(Exception):
    def __init__(self, game, games):
        super()
        print(
            f"Could not find game {game if game else ''} in games {games.keys() if games else ''}")
