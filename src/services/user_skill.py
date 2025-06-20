from typing import Optional

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository
from src.databases.models import SkillUser


class UserSkillService(Service):
    def __init__(self, session: AsyncSession, user_repo: Repository, skill_repo: Repository):
        self.session = session
        self.user_repo = user_repo
        self.skill_repo = skill_repo
    
    async def add_skill_one(self, skill_id: str, user_id: int):
        user = await self.user_repo(self.session).select_one_by_id(user_id)
        if not user:
            return 1
        skill = await self.skill_repo(self.session).select_one_by_id(skill_id)
        if not skill:
            return 2
        try:
            await self.session.execute(insert(SkillUser).values(skill_id=skill_id, user_id=user_id))
            await self.session.commit()
        except Exception:
            return None
        return True
