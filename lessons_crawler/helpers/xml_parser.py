import json
from collections import OrderedDict

import xmltodict


class XMLParser:
    def __init__(self, text: str, encoding: str = "utf-8"):
        self.encoding = encoding if encoding else "utf-8"
        self.text = text.encode(self.encoding).decode()

    @property
    def parsed(self) -> OrderedDict:
        raw_parsed = xmltodict.parse(self.text)
        data = self.__clean_data(raw_parsed)
        return data

    @staticmethod
    def __clean_data(data: OrderedDict) -> OrderedDict:
        raw_text = json.dumps(data)
        clean_text = raw_text.replace("\"#", "\"").replace("\"@", "\"")
        new_data = json.loads(clean_text, object_pairs_hook=OrderedDict)
        return new_data
