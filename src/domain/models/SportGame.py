from pydantic import BaseModel

class SportGame(BaseModel):
    id: int
    sport_id: int
    game_id: int