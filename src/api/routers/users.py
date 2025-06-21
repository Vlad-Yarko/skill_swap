from fastapi import APIRouter

from src.schemas.users import UserPublic, UserSkill, UsersPublic
from src.api.dependencies.users import add_one, add_skill_one, users_get


router = APIRouter(
    tags=['USER'],
    prefix='/users'
)


@router.post('/add/one', response_model=UserPublic)
async def users_add_one(data: add_one):
    return data


@router.post('/add/skill/one', response_model=UserSkill)
async def users_add_skill_one(data: add_skill_one):
    return data

@router.get('/get/all', response_model=UsersPublic)
async def users_get_all(data: users_get):
    return data
