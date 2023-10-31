import datetime as dt

from source.helpers.datetime import (
    add_days,
    format_datetime,
    get_current_datetime,
    get_date_difference,
    get_first_day_of_month,
    get_last_day_of_month,
    get_weekday,
    is_weekend,
    parse_datetime,
)


def test_get_current_datetime():
    assert isinstance(get_current_datetime(), dt.datetime)


def test_format_datetime():
    date_time = dt.datetime(2023, 10, 31, 12, 34, 56)
    assert format_datetime(date_time) == "2023-10-31 12:34:56"


def test_parse_datetime():
    date_time_str = "2023-10-31 12:34:56"
    assert parse_datetime(date_time_str) == dt.datetime(2023, 10, 31, 12, 34, 56)


def test_get_date_difference():
    date1 = dt.datetime(2020, 1, 1)
    date2 = dt.datetime(2023, 10, 31)

    print(get_date_difference(date1, date2))

    assert get_date_difference(date1, date2) == (3, 9, 30)


def test_add_days():
    date = dt.datetime(2023, 10, 31)
    assert add_days(date, 5) == dt.datetime(2023, 11, 5)


def test_get_weekday():
    date = dt.datetime(2023, 10, 31)
    assert get_weekday(date) == "Tuesday"


def test_is_weekend():
    weekday_date = dt.datetime(2023, 10, 31)  # Tuesday
    weekend_date = dt.datetime(2023, 11, 4)  # Saturday
    assert not is_weekend(weekday_date)
    assert is_weekend(weekend_date)


def test_get_first_day_of_month():
    date = dt.datetime(2023, 10, 31)
    assert get_first_day_of_month(date) == dt.datetime(2023, 10, 1)


def test_get_last_day_of_month():
    date = dt.datetime(2023, 10, 31)
    assert get_last_day_of_month(date) == dt.datetime(2023, 10, 31)
