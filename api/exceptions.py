class FormatNotFoundError(Exception):
    def __init__(self):
        super()


class CountryNotFoundError(Exception):
    def __init__(self, country=None):
        super()
        print(f"Could not find '{country}' in country list")
