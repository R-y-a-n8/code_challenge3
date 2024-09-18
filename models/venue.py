import sqlite3

class Venue:
    @staticmethod
    def get_all():
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM venues")
        venues = cursor.fetchall()
        conn.close()
        return venues
