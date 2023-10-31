from typing import Optional
from pydantic import BaseModel


class ErrorInfoModel:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __repr__(self):
        return f"code:{self.code},message:{self.message}"


class ErrorInfoContainer:
    unhandled_error = ErrorInfoModel(
        code=1,
        message="Internal server error",
    )

    could_not_get_excepted_response = ErrorInfoModel(
        code=2,
        message="Could not get expected response",
    )

    model_validation_error = ErrorInfoModel(
        code=3,
        message="Model validation error",
    )

    not_found_error = ErrorInfoModel(
        code=4,
        message="Not found",
    )


class ErrorResponseModel(BaseModel):
    error_code: Optional[int] = None
    error_detail: Optional[list] = None
    error_message: Optional[str] = None
