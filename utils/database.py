import sqlite3

def initialize_database():
    connection = sqlite3.connect('concerts.db')
    cursor = connection.cursor()

    # Run schema.sql to create tables
    with open('db/schema.sql', 'r') as schema_file:
        cursor.executescript(schema_file.read())

    # Run seed.sql to populate initial data
    with open('db/seed.sql', 'r') as seed_file:
        cursor.executescript(seed_file.read())

    connection.commit()
    connection.close()
