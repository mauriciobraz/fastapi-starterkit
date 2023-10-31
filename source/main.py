from venv import logger
import uvicorn

from dotenv import load_dotenv

from fastapi import FastAPI
from pydantic import ValidationError

from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from .api.errors.exception_handlers import (
    DataException,
    ServiceException,
    ExceptionHandlers,
)

from .api.routers.default_router import default_router

from .helpers.dotenv import get_env_variable
from .helpers.logger import setup_logger

load_dotenv()
setup_logger()


def main() -> FastAPI:
    app = FastAPI(
        tile="FastAPI Template",
        description="A template for FastAPI projects.",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(
        DataException,
        ExceptionHandlers.data_exception,
    )

    app.add_exception_handler(
        HTTPException,
        ExceptionHandlers.http_exception,
    )

    app.add_exception_handler(
        ServiceException,
        ExceptionHandlers.service_exception,
    )

    app.add_exception_handler(
        ValidationError,
        ExceptionHandlers.validation_exception,
    )

    app.add_exception_handler(
        Exception,
        ExceptionHandlers.unhandled_exception,
    )

    app.include_router(
        router=default_router,
    )

    return app


def start() -> None:
    uvicorn.run(
        app=main(),
        port=get_env_variable("PORT", int, 8000),
    )
