from .error_models import ErrorInfoModel


class ApplicationException(Exception):
    """
    Base class for all application exceptions.
    """

    def __init__(
        self, error_info: ErrorInfoModel, exception: Exception | None = None
    ) -> None:
        super().__init__()

        self.exception = exception
        self.error_info = error_info


class DataException(ApplicationException):
    """
    Exception class for all data related exceptions.
    """

    pass


class ServiceException(ApplicationException):
    """
    Exception class for all service related exceptions.
    """

    pass
