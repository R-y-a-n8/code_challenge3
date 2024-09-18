import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @classmethod
    def get_all(cls):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM concerts'
        concerts = cursor.execute(query).fetchall()

        connection.close()
        return [cls(*concert) for concert in concerts]

    @classmethod
    def find_by_id(cls, concert_id):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM concerts WHERE id = ?'
        concert = cursor.execute(query, (concert_id,)).fetchone()

        connection.close()
        return cls(*concert) if concert else None

    def band(self):
        from models.band import Band
        return Band.find_by_id(self.band_id)

    def venue(self):
        from models.venue import Venue
        return Venue.find_by_id(self.venue_id)

    def hometown_show(self):
        connection = sqlite3.connect('concerts.db')
        cursor = connection.cursor()

        query = '''
        SELECT bands.hometown, venues.city 
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        JOIN venues ON concerts.venue_id = venues.id
        WHERE concerts.id = ?
        '''

        hometown, city = cursor.execute(query, (self.id,)).fetchone()
        connection.close()

        return hometown == city

    def introduction(self):
        band = self.band()
        venue = self.venue()
        return f"Hello {venue.city}!!!!! We are {band.name} and we're from {band.hometown}"
