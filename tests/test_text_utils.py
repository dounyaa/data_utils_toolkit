import pytest

from data_utils_toolkit.text_utils import normalize, slugify


@pytest.mark.parametrize(
    "input_text, expected",
    [
        ("hello world", "hello world"),
        ("  hello world  ", "hello world"),
        ("hello\t\tworld\n!", "hello world !"),
        ("", ""),
        ("   ", ""),
    ],
)
def test_normalize_cases(input_text: str, expected: str) -> None:
    assert normalize(input_text) == expected


@pytest.mark.parametrize(
    "raw, expected_slug",
    [
        ("Hello World", "hello-world"),
        ("Éléphant d'Afrique", "elephant-d-afrique"),
        ("Hello!!! World??", "hello-world"),
        ("Hello -- world", "hello-world"),
        ("", ""),
        ("!!!", ""),
    ],
)
def test_slugify_cases(raw: str, expected_slug: str) -> None:
    assert slugify(raw) == expected_slug
