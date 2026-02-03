class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        # Only allow setting if _hometown doesn't exist yet (immutable)
        if not hasattr(self, "_hometown"):
            if isinstance(value, str) and len(value) > 0:
                self._hometown = value

    def concerts(self):
        # Filter Concert.all for this band's instances
        results = [c for c in Concert.all if c.band == self]
        return results if results else None

    def venues(self):
        # Get a unique list of venues from this band's concerts
        band_concerts = self.concerts()
        if not band_concerts:
            return None
        return list(set([c.venue for c in band_concerts]))

    def play_in_venue(self, venue, date):
        # Create and return a new concert instance
        return Concert(date, self, venue)

    def all_introductions(self):
        # Collect introductions from all concerts for this band
        band_concerts = self.concerts()
        if not band_concerts:
            return None
        return [c.introduction() for c in band_concerts]


class Concert:
    all = []  # Single source of truth for all instances

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        Concert.all.append(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value

    def hometown_show(self):
        # Check if venue city matches band hometown
        return self.venue.city == self.band.hometown

    def introduction(self):
        # Return the specific string format required
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value

    def concerts(self):
        # Filter Concert.all for this venue's instances
        results = [c for c in Concert.all if c.venue == self]
        return results if results else None

    def bands(self):
        # Get a unique list of bands from this venue's concerts
        venue_concerts = self.concerts()
        if not venue_concerts:
            return None
        return list(set([c.band for c in venue_concerts]))