from typing import Optional

from sqlalchemy import select, insert

from src.utils.repository import SQLAlchemyRepository
from src.databases.models import User


class UserRepository(SQLAlchemyRepository):
    model = User
    
    async def select_one_by_username(self, username: str):
        return await self.select_one("username", username)
    
    async def select_one_by_email(self, email: str):
        return await self.select_one("email", email)
