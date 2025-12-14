from datetime import date, datetime

_DATE_FORMAT : str = "%Y-%m-%d"
def parse_date(date_str: str) -> date:
    """
    parse a date string in format "YYYY-MM-DD" and return a date object
    """
    if not isinstance(date_str, str):
        raise TypeError(f"parse_date() expected a string, got {type(date_str)!r}")
    cleaned = date_str.strip()
    if not cleaned:
        raise ValueError("parse_date() expected a non-empty string")
    try:
        date_obj = datetime.strptime(cleaned, _DATE_FORMAT).date()
    except ValueError as e:
        raise ValueError(f"invalid date format {cleaned!r}, expected YYYY-MM-DD") from e

    return date_obj

def format_date(value: date) -> str:
    """Format a date object as 'YYYY-MM-DD'."""
    if not isinstance(value, date):
        raise TypeError(f"format_date() expected a date object, got {type(value)!r}")

    return value.strftime(_DATE_FORMAT)

