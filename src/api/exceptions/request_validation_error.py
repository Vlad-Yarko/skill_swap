from fastapi import Request, HTTPException, status
from fastapi.exceptions import RequestValidationError


async def exception(request: Request, exc: RequestValidationError):
    detail = exc.errors()[0]["msg"]
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=detail
    )
