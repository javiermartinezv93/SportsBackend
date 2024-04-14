from pydantic import BaseModel

class Player(BaseModel):
    id: int
    first_name: str
    last_name: str
    image: str
    jersey_number: int
    birth_date: str
    status: str