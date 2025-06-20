from typing import Optional

from sqlalchemy import select, insert

from src.utils.repository import SQLAlchemyRepository
from src.databases.models import Skill


class SkillRepository(SQLAlchemyRepository):   
    model = Skill
    
    async def select_one_by_title(self, title: str):
        return await self.select_one("title", title)
    