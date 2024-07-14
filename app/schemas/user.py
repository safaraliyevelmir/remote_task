from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    
class User(BaseModel):
    id: int
    email: str

class UserRead(BaseModel):
    id: int
    email: str

class TokenData(BaseModel):
    email: str

class Token(BaseModel):
    access_token: str
    token_type: str


