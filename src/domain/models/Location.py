from pydantic import BaseModel

class Location(BaseModel):
    id: int
    name: str
    description: str
    image: str
    address: str
    latitude: float
    longitude: float
    extra: dict