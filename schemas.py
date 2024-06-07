from pydantic import BaseModel

class PhoneBase(BaseModel):
    modelName: str
    modelDescription: str
    price: int