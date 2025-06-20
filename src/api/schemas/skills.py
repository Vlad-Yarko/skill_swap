from pydantic import BaseModel, Field

from src.databases.models import SkillLevel
from src.api.schemas.users_skills import UserSkill


class SkillBody(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(...)
    level: SkillLevel = Field(...)
    

class SkillPublic(BaseModel):
    id: int
