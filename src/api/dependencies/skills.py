from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.api.dependencies.db import DBSession
from src.repositories.skills import SkillRepository
from src.services.skills import SkillService
from src.api.schemas.skills import UserSkill, SkillBody, SkillPublic
from src.api.dependencies.users_skills import users_skills_dependency


async def skills_add_one(session: DBSession, body: SkillBody) -> SkillPublic:
    service = SkillService(session, SkillRepository)
    id = await service.add_one(title=body.title, description=body.description, level=body.level)
    if not id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Skill has already found"
            )
    return SkillPublic(id=id)
    

add_one = Annotated[SkillPublic, Depends(skills_add_one)]


async def users_add_user_one(data: users_skills_dependency) -> UserSkill:
    if data.d is None:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="User has already found"
        )
    return UserSkill(skillId=data.body.skillId, userId=data.body.userId)


add_user_one = Annotated[UserSkill, Depends(users_add_user_one)]
