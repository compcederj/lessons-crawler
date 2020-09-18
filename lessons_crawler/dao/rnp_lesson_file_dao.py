import os
from typing import Tuple

import click
import requests
from requests import Response

from dao.lesson_data_dao import LessonDataDAO
from lessons_crawler.helpers import strip_accents
from lessons_crawler.models.lessons import Lesson


class RNPLessonFileDAO:
    def __init__(self, lesson: Lesson):
        self.lesson = lesson

    @property
    def subject_name(self) -> str:
        return strip_accents(self.lesson.subject.name.lower().replace(" ", "_"))

    @property
    def lesson_index(self) -> str:
        return strip_accents(self.lesson.lesson_index.lower().replace(" ", "_"))

    @property
    def path(self) -> str:
        return os.path.join(os.getcwd(), 'storage', self.subject_name, self.lesson_index)

    def __create_path(self):
        if not os.path.isdir(self.path):
            os.makedirs(self.path)

    @staticmethod
    def __get_file_info(url) -> Tuple[str, Response]:
        file_name = os.path.split(url)[1]
        response = requests.get(url)
        return file_name, response

    def _save_file(self, file_name: str, data: bytes) -> str:
        self.__create_path()
        file_path = os.path.join(self.path, file_name)
        click.echo(file_path)
        with open(file_path, 'wb') as file:
            file.write(data)
        return file_path

    def save_mp4(self) -> str:
        file_name, response = self.__get_file_info(self.lesson.mp4_video_file)
        file_path = self._save_file(file_name, response.content)
        return file_path

    def save_webm(self) -> str:
        file_name, response = self.__get_file_info(self.lesson.webm_video_file)
        file_path = self._save_file(file_name, response.content)
        return file_path

    def save_xml(self) -> str:
        file_name, response = self.__get_file_info(self.lesson.xml_file)
        file_path = self._save_file(file_name, response.content)
        return file_path

    def save_index(self) -> str:
        file_name, response = self.__get_file_info(self.lesson.index_file)
        file_path = self._save_file(file_name, response.content)
        return file_path

    def save_sync(self) -> str:
        file_name, response = self.__get_file_info(self.lesson.sync_file)
        file_path = self._save_file(file_name, response.content)
        return file_path

    def save_slides(self):
        lesson_data = LessonDataDAO.get_by_lesson(self.lesson)
        for slide in lesson_data.json_sync.get("slides").get("slide"):
            slide_file = slide.get("@relative_path")
            code = lesson_data.lesson.subject.code
            lesson_index = lesson_data.lesson.index_file.replace(' ', '_')
            url = f"http://va05-idc.rnp.br/riotransfer/{code}/{lesson_index}/{slide_file}"
            data = requests.get(url)
            self._save_file(slide_file, data.content)

    def save_files(self):
        self.save_mp4()
        self.save_webm()
        self.save_xml()
        self.save_index()
        self.save_sync()
