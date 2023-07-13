from classes.concert import Concert

class Venue:
    def __init__(self, title, city):
        self.title = title
        self.city = city
        self._concerts = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception
        self._title = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception
        self._city = value

    @property
    def concerts(self):
        return self._concerts

    @property
    def bands(self):
        return [concert.band for concert in self._concerts]

    def add_concert(self, concert):
        self._concerts.append(concert)

    def concert_on(self, date):
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
