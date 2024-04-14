from pydantic import BaseModel

class CompetitionFixture(BaseModel):
    id: int
    competition_id: int
    game_id: int
    name: str
    extra: dict