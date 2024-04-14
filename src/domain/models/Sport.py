from pydantic import BaseModel

class Sport(BaseModel):
    id: int
    name: str
    description: str
    image: str