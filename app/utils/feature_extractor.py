import re
import math
from urllib.parse import urlparse


# -----------------------------
# FEATURE EXTRACTOR
# -----------------------------
def extract_features(url: str):
    """
    Extract structural URL features for ML model.
    Input MUST be string.
    """

    url = str(url).lower().strip()

    # -------------------------
    # BASIC FEATURES
    # -------------------------
    length = len(url)
    dots = url.count(".")
    digits = sum(c.isdigit() for c in url)
    special_chars = len(re.findall(r'[@%&+=?_~\-]', url))

    # -------------------------
    # DOMAIN FEATURES
    # -------------------------
    parsed = urlparse(url)
    hostname = parsed.netloc

    subdomains = hostname.count('.') - 1 if hostname else 0

    # -------------------------
    # ENTROPY
    # -------------------------
    try:
        prob = [url.count(c) / len(url) for c in set(url)]
        entropy = -sum(p * math.log2(p) for p in prob if p > 0)
    except:
        entropy = 0

    # -------------------------
    # SUSPICIOUS KEYWORDS
    # -------------------------
    keywords = [
        "login", "verify", "secure",
        "account", "update", "bank",
        "confirm", "password"
    ]

    keyword_count = sum(1 for k in keywords if k in url)

    return [
        length,
        dots,
        digits,
        special_chars,
        subdomains,
        entropy,
        keyword_count
    ]