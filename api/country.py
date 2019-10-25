class Country:

    def __init__(self, name, capital, img_url):
        self._name = name
        self._capital = capital
        self._img_url = img_url

    @property
    def name(self):
        return self._name

    @property
    def code(self):
        return self._code

    @property
    def capital(self):
        return self._capital

    @property
    def img_url(self):
        return self._img_url

    def to_dict(self):
        properties = {
            "name": self._name,
            "capital": self._capital,
            "img_url": self._img_url
        }
        return properties
