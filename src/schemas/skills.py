from pydantic import Field

from src.utils.schema import Schema
from src.databases.models import SkillLevel
from src.schemas.users_skills import UserSkill


class SkillBody(Schema):
    title: str = Field(..., max_length=100)
    description: str = Field(...)
    level: SkillLevel = Field(...)
    

class SkillPublic(Schema):
    id: int
