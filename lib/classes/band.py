from classes.concert import Concert

class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception
        self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception
        self._hometown = value

    @property
    def concerts(self):
        return self._concerts

    def play_in_venue(self, venue, date):
        concert = Concert(date, self, venue)
        self._concerts.append(concert)
        venue.add_concert(concert)
        return concert

    def all_introductions(self):
        return [concert.introduction() for concert in self._concerts]
