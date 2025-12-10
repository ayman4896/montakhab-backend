from pydantic import BaseModel

class PlayerCreate(BaseModel):
    name: str
    age: str
    weight: str
    organization: str
    nationalID: str
    phone: str
    category: str
    photo: str | None = None


class PlayerOut(PlayerCreate):
    id: int

    class Config:
        orm_mode = True
