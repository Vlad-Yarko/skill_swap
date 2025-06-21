from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.api.dependencies.db import DBSession
from src.services.user_skill import UserSkillService
from src.repositories.skills import SkillRepository
from src.repositories.users import UserRepository
from src.schemas.users_skills import UserSkill, UserSkillSchema


async def users_skills_dep(session: DBSession, body: UserSkill) -> UserSkillSchema:
    service = UserSkillService(session, UserRepository, SkillRepository)
    d = await service.add_skill_one(body.skillId, body.userId)
    if d == 1:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="User was not found"
        )
    if d == 2:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Skill was not found"
        )
    return UserSkillSchema(body=body, d=d)


users_skills_dependency = Annotated[UserSkillSchema, Depends(users_skills_dep)]
