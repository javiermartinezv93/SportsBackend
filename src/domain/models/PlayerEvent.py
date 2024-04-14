from pydantic import BaseModel

class PlayerEvent(BaseModel):
    id: int
    player_id: int
    game_id: int
    event_type: str
    event_time: str
    event_description: str
    extra: dict