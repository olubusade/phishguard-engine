import socket
from urllib.parse import urlparse


def url_exists(url: str) -> bool:
    """
    Lightweight DNS check (no HTTP request).
    Returns True if domain resolves.
    """

    try:
        domain = urlparse(str(url)).netloc

        if not domain:
            return False

        socket.gethostbyname(domain)
        return True

    except:
        return False