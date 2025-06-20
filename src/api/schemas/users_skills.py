from typing import Union

from pydantic import BaseModel, Field


class UserSkill(BaseModel):
    skillId: int = Field(...)
    userId: int = Field(...)


class UserSkillSchema(BaseModel):
    body: UserSkill
    d: Union[int, bool, None]
