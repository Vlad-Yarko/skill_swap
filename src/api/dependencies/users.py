from typing import Annotated

from fastapi import Depends, HTTPException, status

from src.api.dependencies.db import DBSession
from src.services.users import UserService
from src.repositories.users import UserRepository
from src.schemas.users import UserBody, UserPublic, UserSkill, UsersBody, UsersPublic
from src.api.dependencies.users_skills import users_skills_dependency


async def user_service_dep(session: DBSession) -> UserService:
    service = UserService(session, UserRepository)
    return service


user_service = Annotated[UserService, Depends(user_service_dep)]


async def users_add_one(service: user_service, body: UserBody) -> UserPublic:
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


async def users_get_all(service: user_service, query_body: UsersBody = Depends()) -> UsersPublic:
    data = await service.get_all(query_body.page)
    return data


users_get = Annotated[UsersPublic, Depends(users_get_all)]
