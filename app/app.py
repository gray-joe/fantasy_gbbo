from fastapi import FastAPI
from pydantic import BaseModel
from app.database import Database
from app.classes.league import League

db_config = {
    'dbname': 'gbbo',
    'user': 'postgres',
    'password': 'mysecretpassword',
    'host': 'localhost',
    'port': '5432'
}

app = FastAPI()
db = Database(db_config)

class LeagueCreateRequest(BaseModel):
    name: str
    code: str

@app.get("/")
def test():
    return {"Hello": "World"}

@app.post("/leagues/")
async def create_league(league: LeagueCreateRequest):
    league_instance = League(db)
    id = league_instance.create_league(league.name, league.code)
    return {"id": id}
