from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str


class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    name: str
    description: str

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
