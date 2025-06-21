from typing import Optional

from pydantic import BaseModel, Field, EmailStr

from src.utils.schema import Schema
from src.schemas.users_skills import UserSkill


class UserBody(Schema):
    username: str = Field(..., max_length=50)
    email: EmailStr = Field(...)
    fullName: str = Field(None, max_length=100)
    bio: str = Field(None)
    

class UserPublic(Schema):
    id: int
    
    
class UsersSchema(Schema):
    page: Optional[int] = Field(None, ge=1)
    
    
class UsersBody(UsersSchema):
    pass
    
    
class UsersPublic(UsersSchema):
    data: list[UserPublic]
    count: int
    total: int
    next: bool
    
    # model_config = {"from_attributes": True}
