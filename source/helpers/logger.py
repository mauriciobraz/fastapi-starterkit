import sentry_sdk

from pathlib import Path
from loguru import logger

from sentry_sdk.integrations.loguru import LoguruIntegration

from ..helpers.dotenv import get_env_variable
from ..helpers.poetry import get_project_name, get_project_version


def setup_logger() -> None:
    """
    Configures the Loguru logger with file rotation and Sentry integration.

    - Logs are saved in the "logs/logs.log" file.
    - Logs are rotated every week to prevent large log files.
    - If a Sentry DSN is provided via the environment variable SENTRY_DSN, logs are also sent to Sentry.
    """
    logger.add(
        sink="logs/logs.log",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | {message}",
        rotation="1 week",
        backtrace=True,
        diagnose=True,
    )

    if (
        sentry_dsn := get_env_variable(
            type=str,
            name="SENTRY_DSN",
            default="UNKNOWN",
        )
    ) != "UNKNOWN":
        project_name = get_project_name()

        if project_name == "source":
            # NOTE: This is a hacky way to get the project name.
            #       If you change this file path, you will need to update this.
            project_name = Path(__file__).resolve().parent.parent.parent.name

        sentry_sdk.init(
            dsn=sentry_dsn,
            release=f"{project_name}@{get_project_version()}",
            environment=get_env_variable("ENVIRONMENT", str, "development"),
            integrations=[
                LoguruIntegration(),
            ],
        )
