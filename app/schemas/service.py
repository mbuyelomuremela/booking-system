from pydantic import BaseModel
from typing import Union

class ServiceAddModel(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

class ServiceData(ServiceAddModel):
    id: int

    class Config:
        from_attributes = True