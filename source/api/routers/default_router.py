from fastapi import status, APIRouter
from fastapi.responses import PlainTextResponse, JSONResponse

default_router = APIRouter(
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Not found"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"},
    },
)


@default_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_class=JSONResponse,
    responses={
        status.HTTP_200_OK: {
            "model": str,
            "content": {
                "application/json": {"example": {"message": "Hello World!"}},
            },
        }
    },
)
async def get_root():
    return JSONResponse(
        {"message": "Hello World!"},
        status_code=status.HTTP_200_OK,
    )


@default_router.get(
    "/health",
    status_code=status.HTTP_200_OK,
    response_class=PlainTextResponse,
    responses={
        status.HTTP_200_OK: {
            "model": str,
            "content": {
                "text/plain": {"example": "OK"},
            },
        }
    },
)
async def get_health():
    return "OK"


@default_router.get(
    "/status",
    status_code=status.HTTP_200_OK,
    response_class=JSONResponse,
)
async def get_status():
    return JSONResponse(
        # Update this to include any other services that need to be checked.
        {"api": "OK", "redis": "OK", "database": "OK"},
        status_code=status.HTTP_200_OK,
    )
