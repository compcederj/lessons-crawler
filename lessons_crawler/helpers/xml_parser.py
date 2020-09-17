import json

import xmltodict


class XMLParser:
    def __init__(self, text: str, encoding: str = "utf-8"):
        self.encoding = encoding
        self.text = text.encode(self.encoding).decode()
        self.parsed = xmltodict.parse(self.text)
