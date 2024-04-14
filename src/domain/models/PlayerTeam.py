from pydantic import BaseModel

class PlayerTeam(BaseModel):
    id: int
    player_id: int
    team_id: int
    start_date: str
    end_date: str
    extra: dict
