from collections import OrderedDict

import requests

from lessons_crawler.helpers.xml_parser import XMLParser
from lessons_crawler.models.lessons import Lesson


class RNPLessonDataDAO:
    def __init__(self, lesson: Lesson):
        self.lesson = lesson

        self.__xml_data = requests.get(lesson.xml_file)
        self.__xml_data_parsed = XMLParser(self.__xml_data.text, self.__xml_data.encoding)

        self.__index_data = requests.get(lesson.index_file)
        self.__index_data_parsed = XMLParser(self.__index_data.text, self.__index_data.encoding)

        self.__sync_data = requests.get(lesson.sync_file)
        self.__sync_data_parsed = XMLParser(self.__sync_data.text, self.__sync_data.encoding)

    @property
    def xml_raw_data(self) -> str:
        return self.__xml_data_parsed.text

    @property
    def xml_json_data(self) -> OrderedDict:
        return self.__xml_data_parsed.parsed

    @property
    def index_raw_data(self) -> str:
        return self.__index_data_parsed.text

    @property
    def index_json_data(self) -> OrderedDict:
        return self.__index_data_parsed.parsed

    @property
    def sync_raw_data(self) -> str:
        return self.__sync_data_parsed.text

    @property
    def sync_json_data(self) -> OrderedDict:
        return self.__sync_data_parsed.parsed
