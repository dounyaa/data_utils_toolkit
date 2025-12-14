import re
import unicodedata


def normalize(text: str) -> str:
    """Normalize input: trim, collapse whitespace, return empty if blank."""
    if not text:
        return ""

    cleaned = text.strip()
    if not cleaned:
        return ""

    return re.sub(r"\s+", " ", cleaned)


def slugify(text: str) -> str:
    """Return a URL-safe slug: lowercase, ascii-only, hyphen-separated."""
    cleaned = normalize(text)
    if not cleaned:
        return ""

    lowered = cleaned.lower()
    decomposed = unicodedata.normalize("NFKD", lowered)
    ascii_only = decomposed.encode("ascii", "ignore").decode("ascii")
    replaced = re.sub(r"[^a-z0-9]", "-", ascii_only)
    collapsed = re.sub(r"-+", "-", replaced)
    slug = collapsed.strip("-")
    return slug
