from pydantic import BaseModel, Field, EmailStr

from src.api.schemas.users_skills import UserSkill


class UserBody(BaseModel):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(...)
    fullName: str = Field(None, max_length=100)
    bio: str = Field(None)
    

class UserPublic(BaseModel):
    id: int
