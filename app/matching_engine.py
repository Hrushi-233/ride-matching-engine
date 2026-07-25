from datetime import datetime
from app.models import Ride

# Nearby pickup locations
NEARBY_LOCATIONS = {
    "ghatkesar": ["uppal", "nagole", "boduppal"],
    "uppal": ["ghatkesar", "nagole", "boduppal"],
    "nagole": ["uppal", "ghatkesar", "lb nagar"],
    "lb nagar": ["nagole", "dilsukhnagar"],
    "dilsukhnagar": ["lb nagar"],
    "kukatpally": ["ameerpet", "miyapur"],
    "ameerpet": ["kukatpally", "madhapur"],
    "miyapur": ["kukatpally"],
}


def time_difference(request_time, ride_time):
    t1 = datetime.strptime(request_time, "%I:%M %p")
    t2 = datetime.strptime(ride_time, "%I:%M %p")
    return abs((t1 - t2).total_seconds()) / 60


def calculate_match_score(request, ride: Ride):

    breakdown = {
        "pickup": 0,
        "destination": 0,
        "time": 0,
        "preference": 0,
        "seats": 0
    }

    # Pickup Similarity
    if request.pickup.lower() == ride.pickup.lower():
        breakdown["pickup"] = 30

    elif ride.pickup.lower() in NEARBY_LOCATIONS.get(request.pickup.lower(), []):
        breakdown["pickup"] = 20

    # Destination
    if request.destination.lower() == ride.destination.lower():
        breakdown["destination"] = 30

    # Time
    diff = time_difference(request.departure_time, ride.departure_time)

    if diff <= 15:
        breakdown["time"] = 20
    elif diff <= 30:
        breakdown["time"] = 15
    elif diff <= 60:
        breakdown["time"] = 10

    # Preference
    if (
        request.gender_preference.lower() == "any"
        or ride.gender_preference.lower() == request.gender_preference.lower()
    ):
        breakdown["preference"] = 10

    # Seats
    if ride.available_seats > 0:
        breakdown["seats"] = 10

    score = sum(breakdown.values())

    return score, breakdown