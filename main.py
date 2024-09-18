import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.database import initialize_database
from models.band import Band
from models.venue import Venue
from models.concert import Concert

# Initialize the database
initialize_database()

# Test methods
bands = Band.get_all()
venues = Venue.get_all()

print("All bands:", bands)
print("All venues:", venues)

# Get concerts for a band
band_concerts = Band.concerts(1)
print("Concerts for Band 1:", band_concerts)

# Get the band with the most performances
top_band = Band.most_performances()
print("Band with most performances:", top_band)
