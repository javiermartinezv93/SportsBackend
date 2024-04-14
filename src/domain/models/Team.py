from pydantic import BaseModel

class Team(BaseModel):
    id: int
    name: str
    description: str
    image: str
    extra: dict