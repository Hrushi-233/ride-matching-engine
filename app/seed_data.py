import json
import os

from app.database import SessionLocal, Base, engine
from app.models import Ride

Base.metadata.create_all(bind=engine)

db = SessionLocal()

# Clear existing data
db.query(Ride).delete()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(BASE_DIR, "data", "sample_rides.json")

with open(DATA_FILE, "r", encoding="utf-8") as file:
    rides = json.load(file)

for ride in rides:
    db.add(Ride(**ride))

db.commit()
db.close()

print(f"{len(rides)} sample rides inserted successfully!")