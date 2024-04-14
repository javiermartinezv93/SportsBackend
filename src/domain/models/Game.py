from pydantic import BaseModel

class Game(BaseModel):
    id: int
    competition_id: int
    location_id: int
    status: str
    date_start: str
    date_finish: str
    home_team_id: int
    away_team_id: int
    home_score: str
    away_score: str
    winner: str