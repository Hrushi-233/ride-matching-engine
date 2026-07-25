# GoTogetherRides AI Ride Matching Engine

## System Architecture

### Objective

The AI Ride Matching Engine recommends the most suitable ride to a user based on:

- Pickup Location
- Destination
- Departure Time
- Seat Availability
- Gender Preference

The recommendation engine assigns a weighted score to each available ride and returns the highest-ranked matches.

---

## High-Level Architecture

+-------------+
|    User     |
+-------------+
       |
       | HTTP Request
       v
+-------------------------+
| HTML Frontend (UI)      |
+-------------------------+
       |
       | POST /match
       v
+-------------------------+
| FastAPI REST API        |
+-------------------------+
       |
       v
+-------------------------+
| Ride Matching Engine    |
| (matching.py)           |
+-------------------------+
       |
       v
+-------------------------+
| SQLite Database         |
| rides.db                |
+-------------------------+
       |
       v
+-------------------------+
| Ranked Ride Results     |
+-------------------------+
       |
       v
+-------------+
| User Screen |
+-------------+

---

## Components

### Frontend

- HTML
- CSS
- JavaScript
- Sends ride search requests.

### Backend

- FastAPI
- REST APIs
- Handles request validation.

### Matching Engine

Responsible for:

- Pickup similarity
- Destination matching
- Departure time matching
- Seat availability
- Gender preference
- Weighted score calculation

### Database

SQLite stores:

- Driver
- Pickup
- Destination
- Time
- Seats
- Price
- Gender Preference

---

## Matching Algorithm

Weight Distribution

Pickup Location .......... 30%

Destination .............. 30%

Departure Time ........... 20%

Gender Preference ........ 10%

Seat Availability ........ 10%

Maximum Score = 100

---

## Technologies

Python

FastAPI

SQLite

SQLAlchemy

HTML

CSS

JavaScript

Git & GitHub