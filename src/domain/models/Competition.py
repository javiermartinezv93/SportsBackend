from pydantic import BaseModel

class Competition(BaseModel):
    id: int
    sport_id: int
    name: str 
    code: str 
    date_start: str
    date_finish: str
    status: str



