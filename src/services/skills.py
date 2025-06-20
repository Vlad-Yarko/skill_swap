from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository


class SkillService(Service):
    def __init__(self, session: AsyncSession, skills_repo: Repository):
        self.session = session
        self.skills_repo = skills_repo
    
    async def add_one(
        self,
        title: str,
        description: str,
        level: str
    ):
        skill = await self.skills_repo(self.session).select_one_by_title(title)
        if skill:
            return None
        id = await self.skills_repo(self.session).create_one(
            title=title,
            description=description,
            level=level
        )
        return id
