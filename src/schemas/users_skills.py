from typing import Union

from pydantic import Field

from src.utils.schema import Schema


class UserSkill(Schema):
    skillId: int = Field(...)
    userId: int = Field(...)


class UserSkillSchema(Schema):
    body: UserSkill
    d: Union[int, bool, None]
