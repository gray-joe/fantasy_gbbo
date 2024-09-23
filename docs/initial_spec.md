# Fantasy League App - Project Specification

## 1. Overview
A traditional Fantasy League app centered around the Great British Bake off, allows users to create leagues, invite 
players, make predictions. Accumulating points based on what happens in the show and seeing how they match up against
other players.

Terminology:
* Admin - app maintainers.
* League owner - the creator of the league, with permissions to manage the league and it's participants.
* Player - end user.

## 2. Project Goals

Provide a UI for users with the ability to
* create and join leagues
* manage leagues that they created & invite other players
* make predictions each week
* view their award points based on their predictions
* view other players points in their league

Provide a RESTful API for the frontend to consume.

Store data in an relational database, e.g PostgreSQL.

_Nice to have: Admin system for submitting the results of the show._

## 3. Technologies (TBD)

**Backend**: Python, FastAPI

**Database**: PostgreSQL

**Database** ORM/Tools: SQLAlchemy, Alembic

**Containerization**: Docker, Docker Compose

**Dependency Management**: Poetry

**Frontend**: React


## 4. Key Features

### 4.1. League Management

* Create League: Users can create leagues with a unique name and code.
* Join League: Players can join a league using the league code.
* Update League: League details, such as the name or code, can be updated by league owners.
* Delete League: Owners can delete leagues.

### 4.2. Player Management

* Register Players: Players can register, providing a name, email, password, and display name.
* Login/Authentication: Players must authenticate to access their account.
* Update Profile: Players can update their profile information.

### 4.3. Prediction System

* Make Predictions: Players can submit predictions for the upcoming week. Players can make a 1 off prediction of an 
overall winner.
* View Predictions: Players can view and modify their predictions until they are locked at TBD time before show.
* Leaderboard: Points are awarded based on prediction accuracy, and a leaderboard is maintained for each league.

### 4.4. REST API
The backend will expose a RESTful API to interact with the system. These should be simple CRUD endpoints, e.g:

```
POST /leagues/: Create a new league.
GET /leagues/{id}: Get league details.
PUT /leagues/{id}: Update league details.
DELETE /leagues/{id}: Delete a league.
POST /players/: Register a new player.
POST /login/: Authenticate and login.
POST /predictions/: Submit a prediction.
GET /leaderboard/{league_id}: View leaderboard for a league.
```

### 4.5 Results submission

* Admins can submit the results of each week to separate endpoint.

## 5. Data Models (TBD)

### 5.1. Leagues

| Column | Type        | Description               |
|--------|-------------|---------------------------|
| id     | UUID (pk)   | Unique ID for each league |
| name   | string (32) | The name of the league.   |
| code   | int         | Unique code for joining.  |

### 5.2. Players (TBD)

### 5.3. Predictions (TBD)

### 5.4. Results (TBD)

## 6. Authentication & Authorization

JWT-based Authentication(?): Players will authenticate using JSON Web Tokens (JWT). Tokens are issued upon successful 
login and must be provided with every request to protected endpoints. Should expire after a set amount of time.

Role-based Access: Certain endpoints (like managing leagues) will be restricted to authorized users (e.g., league 
owners).

## 7. Deployment & Infrastructure (TBD)

## 8. Testing Strategy (TBD)

## 9. Future Features (TBD)
