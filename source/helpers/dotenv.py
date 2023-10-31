import os

from dotenv import load_dotenv
from typing import Type, TypeVar

load_dotenv()

T = TypeVar("T")


def get_env_variable(name: str, default: T, var_type: Type[T]) -> T:
    """Type-safe wrapper for `os.getenv`.

    Args:
        name (str): Name of the environment variable.
        default (T): Default value if the environment variable is not set.
        var_type (Type[T]): Type of the environment variable.

    Returns:
        T: Value of the environment variable.

    Usage:
        ```python
        from source.helpers.dotenv import get_env_variable

        # Get a string environment variable with a default value.
        get_env_variable("ENVIRONMENT", "development", str)

        # Get an integer environment variable with a default value.
        get_env_variable("PORT", 8000, int)
        ```
    """

    try:
        value = os.getenv(name, default)
        return var_type.__call__(value)
    except ValueError:
        raise ValueError(
            f"Environment variable '{name}' is not of type '{var_type.__name__}'."
        )
    except TypeError:
        raise TypeError(
            f"Environment variable '{name}' is not set and has no default value."
        )
