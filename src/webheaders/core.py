SECURITY_HEADERS = (
    "content-security-policy",
    "strict-transport-security",
    "x-content-type-options",
    "x-frame-options",
    "referrer-policy",
)


def normalize_headers(headers: dict[str, str]) -> dict[str, str]:
    return {str(k).strip().lower(): str(v).strip() for k, v in headers.items()}


def get_header(headers: dict[str, str], name: str, default=None):
    normalized = normalize_headers(headers)
    return normalized.get(name.strip().lower(), default)


def security_headers(headers: dict[str, str]) -> dict[str, bool]:
    normalized = normalize_headers(headers)
    return {name: name in normalized for name in SECURITY_HEADERS}
