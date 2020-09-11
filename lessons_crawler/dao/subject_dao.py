from typing import List

from lessons_crawler.db import db
from lessons_crawler.models.subjects import Subject


class SubjectDAO:

    @staticmethod
    def get_all() -> List[Subject]:
        data = db.session.query(Subject).all()
        return data

    @staticmethod
    def get_from_code(subject_code):
        data = db.session.query(Subject).filter(Subject.code == subject_code).first()
        return data
