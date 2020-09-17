from typing import Dict, List

import requests
from bs4 import BeautifulSoup

from lessons_crawler.dao.subject_dao import SubjectDAO


class RNPLessonDAO:
    servers = [
        "http://va05-idc.rnp.br/riotransfer",
        "http://va05-idc.rnp.br/riotransfer/cederj/sistemas_comp/ead05018/Aula_001/Aula_001.xml,",
        "http://va10-idc.rnp.br/riotransfer"
    ]
    xml_server = servers[0]
    lesson_base_url = "http://videoaula.rnp.br/v.php?f="

    def __init__(self, subject_code: str, lesson_path: str):
        self.subject_code = subject_code
        self.lesson_path = lesson_path
        
        self.url_path = f"{self.xml_server}/cederj/sistemas_comp/{self.subject_code}/{self.lesson_path}"
        self.xml_url = f"{self.url_path}/{self.lesson_path}.xml"
        self.lesson_url = (f"{self.lesson_base_url}/cederj/sistemas_comp/"
                           f"{self.subject_code}/{self.lesson_path}/{self.lesson_path}.xml")
        
        self.__response = requests.get(self.xml_url)
        self.__data = self.__response.text
        self.__soup = BeautifulSoup(self.__data, 'lxml')

    @property
    def title(self) -> str:
        return self.__soup.find("general").find("title").find("string").text

    @property
    def thumbnail(self) -> str:
        thumbnail = self.__soup.find("videoaula").find("technical").find("thumbnail")
        if thumbnail:
            file = thumbnail.entry.text
            return f"{self.url_path}/{file}"
        return ""

    @property
    def __related_media(self) -> Dict[str, str]:
        elements = self.__soup.find("videoaula").find_all("relatedmedia")
        related_media = {}

        for element in elements:
            catalog: str = element.find("catalog").text

            if catalog in ("index", "sync", "video"):
                file: str = element.entry.text

                if catalog == "video":
                    file_extension = file.split(".")[-1]
                    related_media[f"{catalog}_{file_extension}"] = file
                else:
                    related_media[catalog] = file

        return related_media

    @property
    def index(self) -> str:
        return f"{self.url_path}/{self.__related_media.get('index')}"

    @property
    def sync(self) -> str:
        return f"{self.url_path}/{self.__related_media.get('sync')}"

    @property
    def video_mp4(self) -> str:
        return f"{self.url_path}/{self.__related_media.get('video_mp4')}"

    @property
    def video_webm(self) -> str:
        return f"{self.url_path}/{self.__related_media.get('video_webm')}"
    
    @property
    def __related_lessons_from_soup(self):
        relations = self.__soup.find_all("relation")
        related_lessons: List[RNPLessonDAO] = []

        for relation in relations:
            if relation.find("resource"):
                lesson_url = relation.resource.identifier.entry.text
                lesson_path = lesson_url.split("/")[-2]
                related_lessons.append(RNPLessonDAO(self.subject_code, lesson_path))

        return related_lessons

    @property
    def __related_lessons_from_database(self) -> List:
        subject = SubjectDAO.get_from_code(self.subject_code)
        related_lessons: List[RNPLessonDAO] = [
            RNPLessonDAO(self.subject_code, f"Aula_{lesson + 1:0>3}")
            for lesson in range(1, subject.amount_lessons)
        ]

        return related_lessons
    
    @property
    def related_lessons(self) -> List:
        # from_soup = self.__related_lessons_from_soup
        return self.__related_lessons_from_database

    def exists(self):
        return self.__response.status_code == 200
