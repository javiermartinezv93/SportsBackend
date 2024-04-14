from pydantic import BaseModel
# Events like goals, fouls, and substitutions are stored in the GameEvent model.
class GameEvent(BaseModel):
    id: int
    game_id: int
    team_id: int
    player_id: int
    event_type: str
    event_time: str
    event_description: str
    extra: dict