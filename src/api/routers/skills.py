from fastapi import APIRouter

from src.api.schemas.skills import UserSkill, SkillPublic
from src.api.dependencies.skills import add_user_one, add_one


router = APIRouter(
    tags=['SKILLS'],
    prefix='/skills'
)


@router.post('/add/one', response_model=SkillPublic)
async def skills_add_one(data: add_one):
    return data


@router.post('/add/user/one', response_model=UserSkill)
async def skills_add_user_one(data: add_user_one):
    return data
