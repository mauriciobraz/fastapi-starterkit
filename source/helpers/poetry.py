import toml
import pkg_resources

from pathlib import Path
from typing import Optional

from .decorators.cache import memoize


@memoize
def get_project_metadata() -> dict:
    """Get the project metadata from the pyproject.toml file.

    Returns:
        dict: The project metadata.
    """
    project_file = Path(
        pkg_resources.resource_filename(__name__, "../../pyproject.toml")
    )

    with project_file.open() as file:
        return toml.load(file)


def get_project_name() -> str:
    """
    Retrieves the project name from pyproject.toml.

    Returns:
        str: The project name as a string.
    """
    return get_project_metadata()["tool"]["poetry"]["name"]


def get_project_version() -> str:
    """
    Retrieves the project version from pyproject.toml.

    Returns:
        str: The project version as a string.
    """
    return get_project_metadata()["tool"]["poetry"]["version"]


def get_project_description() -> str:
    """
    Retrieves the project description from pyproject.toml.

    Returns:
        str: The project description as a string.
    """
    return get_project_metadata()["tool"]["poetry"]["description"]


def get_project_authors() -> list[str]:
    """
    Retrieves the project authors from pyproject.toml.

    Returns:
        list[str]: The project authors as a list of strings.
    """
    return get_project_metadata()["tool"]["poetry"]["authors"]
