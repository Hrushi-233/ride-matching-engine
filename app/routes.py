from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Ride
from app.schemas import RideCreate, MatchRequest
from app.matching_engine import calculate_match_score

router = APIRouter()
 

# Health Check

@router.get("/health")
def health():
    return {
        "status": "Running",
        "database": "Connected",
        "service": "GoTogetherRides AI Ride Matching Engine"
    }


# Get All Rides

@router.get("/rides")
def get_rides(db: Session = Depends(get_db)):
    return db.query(Ride).all()


# Add New Ride

@router.post("/rides")
def add_ride(ride: RideCreate, db: Session = Depends(get_db)):

    new_ride = Ride(**ride.model_dump())

    db.add(new_ride)
    db.commit()
    db.refresh(new_ride)

    return {
        "message": "Ride added successfully",
        "ride": new_ride
    }


# AI Ride Matching

@router.post("/match")
def match_rides(request: MatchRequest, db: Session = Depends(get_db)):

    rides = db.query(Ride).all()

    results = []

    for ride in rides:

        # Destination is mandatory
        if ride.destination.lower() != request.destination.lower():
            continue

        # Calculate score and explanation
        score, breakdown = calculate_match_score(request, ride)

        # Ignore weak matches
        if score < 50:
            continue

        results.append({

            "ride_id": ride.id,
            "driver_name": ride.driver_name,

            "pickup": ride.pickup,
            "destination": ride.destination,

            "departure_time": ride.departure_time,

            "available_seats": ride.available_seats,

            "price": ride.price,

            "score": score,

            "breakdown": breakdown

        })

    # Highest score first
    results.sort(key=lambda x: x["score"], reverse=True)

    return {
        "total_matches": len(results),
        "matches": results
    }