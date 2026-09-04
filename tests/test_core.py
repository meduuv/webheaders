from webheaders import get_header, normalize_headers, security_headers


def test_normalization():
    assert normalize_headers({" Content-Type ": " text/html "}) == {"content-type": "text/html"}


def test_lookup_and_security():
    headers = {"X-Frame-Options": "DENY", "Content-Type": "text/html"}
    assert get_header(headers, "x-frame-options") == "DENY"
    assert security_headers(headers)["x-frame-options"] is True
    assert security_headers(headers)["referrer-policy"] is False
