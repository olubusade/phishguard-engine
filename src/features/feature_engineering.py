import pandas as pd
import re
import math
from urllib.parse import urlparse

# -----------------------------
# BASIC FEATURE FUNCTIONS
# -----------------------------

def url_length(url):
    return len(str(url))


def count_dots(url):
    return str(url).count(".")


def count_digits(url):
    return sum(c.isdigit() for c in str(url))


def count_special_chars(url):
    return len(re.findall(r'[@%&+=?_~\-]', str(url)))


def subdomain_count(url):
    try:
        hostname = urlparse(url).netloc
        return hostname.count('.') - 1 if hostname else 0
    except:
        return 0


def entropy(url):
    try:
        url = str(url)
        prob = [float(url.count(c)) / len(url) for c in dict.fromkeys(url)]
        return -sum([p * math.log2(p) for p in prob])
    except:
        return 0


def suspicious_keywords(url):
    keywords = [
        "login", "verify", "secure", "account",
        "update", "bank", "confirm", "password"
    ]
    return sum(1 for k in keywords if k in str(url).lower())


# -----------------------------
# FEATURE PIPELINE
# -----------------------------

def extract_features(df):
    df["url_length"] = df["url"].apply(url_length)
    df["dots"] = df["url"].apply(count_dots)
    df["digits"] = df["url"].apply(count_digits)
    df["special_chars"] = df["url"].apply(count_special_chars)
    df["subdomains"] = df["url"].apply(subdomain_count)
    df["entropy"] = df["url"].apply(entropy)
    df["suspicious_keywords"] = df["url"].apply(suspicious_keywords)

    return df