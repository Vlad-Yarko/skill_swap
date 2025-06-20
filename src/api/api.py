from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from src.utils.application import Application
from src.databases.pg_manager import sessionmanager
from src.api.tags_metadata import tags_metadata
from src.api.routers import users, skills
from src.api.exceptions import request_validation_error


class API(Application):
    def __init__(self):
        super().__init__()
        self.title = "Skill-Swap"
        self.tags_metadata = tags_metadata
        self.routers = [
            users.router,
            skills.router
        ]
        self.exceptions = [
            [
                RequestValidationError,
                request_validation_error.exception
            ]
        ]
    
    @staticmethod
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        sessionmanager.connect_to_db()
        yield
        await sessionmanager.close()

    def create(self):
        self.app = FastAPI(
            title=self.title,
            lifespan=self.lifespan,
            openapi_tags=self.tags_metadata
        )
        for router in self.routers:
            self.app.include_router(router)
        # for exception in self.exceptions:
        #     self.app.add_exception_handler(exception[0], exception[1])
        return self.app
    
    def run():
        pass
