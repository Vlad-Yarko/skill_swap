from abc import ABC, abstractmethod
from typing import Union, Optional

from sqlalchemy import insert, select, func
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
    
    @abstractmethod
    async def select_all_count():
        pass
    
    
class SQLAlchemyRepository(Repository):
    model = None
    PAGINATION_OFFSET = 5
    PAGINATION_LIMIT = 5
    
    def __init__(self, session: AsyncSession):
        self.session = session
        
    async def select_all_count(self):
        query = select(func.count()).select_from(self.model)
        data = await self.session.execute(query)
        data = data.scalar_one()
        return data
    
    async def select_all(self, page: Optional[int] = None) -> tuple[list, int, int]:
        query = None
        total = await self.select_all_count()
        if page is None:
            query = select(self.model)
        else:
            offset_page = page - 1
            offset = self.PAGINATION_OFFSET * offset_page
            query = select(self.model).offset(offset).limit(self.PAGINATION_LIMIT)
        data = await self.session.execute(query)
        data = data.scalars().all()
        return data, total, self.PAGINATION_OFFSET
        
    
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
