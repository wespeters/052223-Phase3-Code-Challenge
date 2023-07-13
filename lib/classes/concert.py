class Concert:
    def __init__(self, date, band, venue):
        from classes.band import Band
        from classes.venue import Venue

        self.date = date
        self.band = band
        self.venue = venue

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if not isinstance(date, str) or len(date) == 0:
            raise Exception
        self._date = date

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, band):
        from classes.band import Band
        if not isinstance(band, Band):
            raise Exception
        self._band = band

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, venue):
        from classes.venue import Venue
        if not isinstance(venue, Venue):
            raise Exception
        self._venue = venue

    def hometown_show(self):
        return self._band.hometown == self._venue.city

    def introduction(self):
        return f"Hello {self._venue.city}!!!!!, we are {self._band.name} and we're from {self._band.hometown}"
