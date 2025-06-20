from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.api.dependencies.db import DBSession
from src.services.user_skill import UserSkillService
from src.repositories.skills import SkillRepository
from src.services.users import UserService
from src.repositories.users import UserRepository
from src.api.schemas.users import UserBody, UserPublic, UserSkill
from src.api.dependencies.users_skills import users_skills_dependency


async def users_add_one(session: DBSession, body: UserBody) -> UserPublic:
    service = UserService(session, UserRepository)
    id = await service.add_one(body.username, body.email, body.fullName, body.bio)
    if not id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="User has already found"
            )
    return UserPublic(id=id)
    

add_one = Annotated[UserPublic, Depends(users_add_one)]


async def users_add_skill_one(data: users_skills_dependency) -> UserSkill:
    if not data.d:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Skill has already found"
        )
    return UserSkill(skillId=data.body.skillId, userId=data.body.userId)


add_skill_one = Annotated[UserSkill, Depends(users_add_skill_one)]
