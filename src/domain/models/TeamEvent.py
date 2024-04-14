from pydantic import BaseModel

class TeamEvent(BaseModel):
    id: int
    team_id: int
    event_type: str
    event_time: str
    event_description: str
    extra: dict