import datetime as dt

from typing import Tuple
from dateutil.relativedelta import relativedelta


def get_current_datetime() -> dt.datetime:
    """Get the current date and time.

    Returns:
        datetime.datetime: Current date and time.

    Usage:
        ```python
        from date_time_helpers import get_current_datetime

        # Get the current date and time.
        now = get_current_datetime()
        ```
    """
    return dt.datetime.now()


def format_datetime(
    date_time: dt.datetime, format_str: str = "%Y-%m-%d %H:%M:%S"
) -> str:
    """Format a datetime object to a string.

    Args:
        date_time (datetime.datetime): Datetime object to be formatted.
        format_str (str, optional): Format string. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        str: Formatted datetime string.

    Usage:
        ```python
        from date_time_helpers import format_datetime

        date_time = dt.datetime(2023, 10, 31, 12, 34, 56)

        # Format datetime to string.
        formatted_datetime = format_datetime(date_time)
        ```
    """
    return date_time.strftime(format_str)


def parse_datetime(
    date_time_str: str, format_str: str = "%Y-%m-%d %H:%M:%S"
) -> dt.datetime:
    """Parse a datetime string to a datetime object.

    Args:
        date_time_str (str): Datetime string to be parsed.
        format_str (str, optional): Format string. Defaults to "%Y-%m-%d %H:%M:%S".

    Returns:
        datetime.datetime: Parsed datetime object.

    Usage:
        ```python
        from date_time_helpers import parse_datetime

        date_time_str = "2023-10-31 12:34:56"

        # Parse datetime string to datetime object.
        parsed_datetime = parse_datetime(date_time_str)
        ```
    """
    return dt.datetime.strptime(date_time_str, format_str)


def get_date_difference(date1: dt.datetime, date2: dt.datetime) -> Tuple[int, int, int]:
    """Calculate the difference between two dates in years, months, and days.

    Args:
        date1 (datetime.datetime): First date.
        date2 (datetime.datetime): Second date.

    Returns:
        Tuple[int, int, int]: Difference in years, months, and days.

    Usage:
        ```python
        from date_time_helpers import get_date_difference

        date1 = dt.datetime(2020, 1, 1)
        date2 = dt.datetime(2023, 10, 31)

        # Get the difference between two dates.
        years, months, days = get_date_difference(date1, date2)
        ```
    """
    delta = relativedelta(date2, date1)
    return delta.years, delta.months, delta.days


def add_days(date: dt.datetime, days: int) -> dt.datetime:
    """Add a specified number of days to a date.

    Args:
        date (datetime.datetime): Date to which days will be added.
        days (int): Number of days to add.

    Returns:
        datetime.datetime: Date after adding the specified number of days.

    Usage:
        ```python
        from date_time_helpers import add_days

        date = dt.datetime(2023, 10, 31)

        # Add 5 days to the date.
        new_date = add_days(date, 5)
        ```
    """
    return date + dt.timedelta(days=days)


def get_weekday(date: dt.datetime) -> str:
    """Get the name of the weekday of a date.

    Args:
        date (datetime.datetime): Date for which the weekday name is required.

    Returns:
        str: Name of the weekday.

    Usage:
        ```python
        from date_time_helpers import get_weekday

        date = dt.datetime(2023, 10, 31)

        # Get the name of the weekday.
        weekday_name = get_weekday(date)
        ```
    """
    return date.strftime("%A")


def is_weekend(date: dt.datetime) -> bool:
    """Check if a date falls on a weekend.

    Args:
        date (datetime.datetime): Date to be checked.

    Returns:
        bool: True if the date falls on a weekend, False otherwise.

    Usage:
        ```python
        from date_time_helpers import is_weekend

        date = dt.datetime(2023, 10, 31)

        # Check if the date falls on a weekend.
        is_date_weekend = is_weekend(date)
        ```
    """
    return date.weekday() in (5, 6)


def get_first_day_of_month(date: dt.datetime) -> dt.datetime:
    """Get the first day of the month of a given date.

    Args:
        date (datetime.datetime): Date for which the first day of the month is required.

    Returns:
        datetime.datetime: First day of the month.

    Usage:
        ```python
        from date_time_helpers import get_first_day_of_month

        date = dt.datetime(2023, 10, 31)

        # Get the first day of the month.
        first_day = get_first_day_of_month(date)
        ```
    """
    return dt.datetime(date.year, date.month, 1)


def get_last_day_of_month(date: dt.datetime) -> dt.datetime:
    """Get the last day of the month of a given date.

    Args:
        date (datetime.datetime): Date for which the last day of the month is required.

    Returns:
        datetime.datetime: Last day of the month.

    Usage:
        ```python
        from date_time_helpers import get_last_day_of_month

        date = dt.datetime(2023, 10, 31)

        # Get the last day of the month.
        last_day = get_last_day_of_month(date)
        ```
    """
    next_month = date.replace(day=28) + dt.timedelta(days=4)
    return next_month - dt.timedelta(days=next_month.day)
