from abc import ABC, abstractmethod
from typing import Union, Optional

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession


class Repository(ABC):
    @abstractmethod
    async def create_one():
        pass
    
    @abstractmethod
    async def select_all():
        pass
    
    @abstractmethod
    async def select_one():
        pass
    
    
class SQLAlchemyRepository(Repository):
    model = None
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def select_all():
        pass
    
    async def select_one(self, field_name: str, value: Union[int, str]):
        query = select(self.model).where(getattr(self.model, field_name) == value)
        data = await self.session.execute(query)
        obj = data.scalar()
        return obj
        
    
    async def create_one(self, **kwargs) -> int:
        stmt = insert(self.model).values(**kwargs).returning(self.model.id)
        id = await self.session.execute(stmt)
        await self.session.commit()
        return id.scalar()
    
    async def select_one_by_id(self, id: int):
        return await self.select_one("id", id)
