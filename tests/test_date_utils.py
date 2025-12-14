from datetime import date

import pytest

from data_utils_toolkit.date_utils import format_date, parse_date


def test_parse_date():
    assert parse_date("2024-01-15") == date(2024, 1, 15)

def test_parse_date_invalid_format():
    with pytest.raises(ValueError):
        parse_date("2025/10/11")

def test_parse_date_invalid_type():
    with pytest.raises(TypeError):
        parse_date(1)

def test_parse_date_blank():
    with pytest.raises(ValueError) :
        parse_date("   ") 


def test_format_date():
    assert format_date(date(2024, 1, 15)) == "2024-01-15"

def test_format_date_invalid_type():
    with pytest.raises(TypeError):
        format_date("2025/10/11")

def test_date_roundtrip():
    d = parse_date("2024-01-15")
    assert format_date(d) == "2024-01-15"