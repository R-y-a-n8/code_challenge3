import sqlite3

class Band:
    @staticmethod
    def get_all():
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bands")
        bands = cursor.fetchall()
        conn.close()
        return bands

    @staticmethod
    def concerts(band_id):
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM concerts WHERE band_id = ?", (band_id,))
        concerts = cursor.fetchall()
        conn.close()
        return concerts

    @staticmethod
    def most_performances():
        conn = sqlite3.connect('concerts.db')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT bands.name, COUNT(concerts.id) AS concert_count
        FROM concerts
        JOIN bands ON concerts.band_id = bands.id
        GROUP BY concerts.band_id
        ORDER BY concert_count DESC
        LIMIT 1
        ''')
        top_band = cursor.fetchone()
        conn.close()
        return top_band
