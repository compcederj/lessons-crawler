import unicodedata


def strip_accents(text: str) -> str:
    text = (unicodedata.normalize("NFD", text)
            .encode("ascii", "ignore")
            .decode("utf-8"))
    return text
