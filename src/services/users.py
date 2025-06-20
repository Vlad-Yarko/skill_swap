from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from src.utils.service import Service
from src.utils.repository import Repository


class UserService(Service):
    def __init__(self, session: AsyncSession, user_repo: Repository):
        self.session = session
        self.user_repo = user_repo
    
    async def add_one(
        self,
        username: str,
        email: str,
        full_name: Optional[str] = None,
        bio: Optional[str] = None
    ):
        user = await self.user_repo(self.session).select_one_by_username(username)
        if user:
            return None
        user = await self.user_repo(self.session).select_one_by_email(email)
        if user:
            return None
        id = await self.user_repo(self.session).create_one(username=username, email=email, full_name=full_name, bio=bio)
        return id        
