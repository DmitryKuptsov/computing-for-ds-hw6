import datetime
from hw4 import get_day_month_year
import pytest


def test_single_date():
    dates = [datetime.date(2025, 11, 3)]
    df = get_day_month_year(dates)

    assert list(df.columns) == ["day", "month", "year"]
    assert df.iloc[0]["day"] == 3
    assert df.iloc[0]["month"] == 11
    assert df.iloc[0]["year"] == 2025


def test_multiple_dates():
    dates = [
        datetime.date(2000, 1, 1),
        datetime.date(2020, 12, 31),
        datetime.date(1999, 7, 15)
    ]
    df = get_day_month_year(dates)

    assert list(df.columns) == ["day", "month", "year"]
    assert len(df) == 3
    assert list(df["day"]) == [1, 31, 15]
    assert list(df["month"]) == [1, 12, 7]
    assert list(df["year"]) == [2000, 2020, 1999]


def test_empty_list():
    dates = []
    df = get_day_month_year(dates)

    assert list(df.columns) == ["day", "month", "year"]
    assert df.empty


def test_leap_day():
    dates = [datetime.date(2020, 2, 29)]
    df = get_day_month_year(dates)

    assert list(df.columns) == ["day", "month", "year"]
    assert df.iloc[0]["day"] == 29
    assert df.iloc[0]["month"] == 2
    assert df.iloc[0]["year"] == 2020


def test_date_order_preserved():
    dates = [
        datetime.date(2025, 5, 1),
        datetime.date(2025, 1, 1),
        datetime.date(2025, 12, 31)
    ]
    df = get_day_month_year(dates)

    assert list(df.columns) == ["day", "month", "year"]
    assert list(df["day"]) == [1, 1, 31]
    assert list(df["month"]) == [5, 1, 12]
    assert list(df["year"]) == [2025, 2025, 2025]


def test_invalid_input_type_raises_error():
    invalid_dates = ["2025-11-03", "2024-01-01"]
    with pytest.raises(AttributeError):
        get_day_month_year(invalid_dates)