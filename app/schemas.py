from pydantic import BaseModel


class RideCreate(BaseModel):
    driver_name: str
    pickup: str
    destination: str
    departure_time: str
    available_seats: int
    price: float
    gender_preference: str


class RideResponse(RideCreate):
    id: int

    class Config:
        from_attributes = True


class MatchRequest(BaseModel):
    pickup: str
    destination: str
    departure_time: str
    gender_preference: str


class MatchResult(BaseModel):
    ride_id: int
    driver_name: str
    score: float