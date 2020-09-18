from lessons_crawler.db import db
from lessons_crawler.models.lessons import Lesson
from lessons_crawler.models.lesson_data import LessonData


class LessonDataDAO:
    @staticmethod
    def create_or_update(lesson: Lesson, raw_xml: str = None, json_xml: dict = None,
                         raw_index: str = None, json_index: dict = None,
                         raw_sync: str = None, json_sync: dict = None):
        lesson_data = (
            db.session.
            query(LessonData).
            filter(LessonData.lesson_id == lesson.id).
            first()
        )

        if not lesson_data:
            lesson_data = LessonData()

        lesson_data.lesson_id = lesson.id
        lesson_data.raw_xml = raw_xml
        lesson_data.json_xml = json_xml
        lesson_data.raw_index = raw_index
        lesson_data.json_index = json_index
        lesson_data.raw_sync = raw_sync
        lesson_data.json_sync = json_sync

        lesson_data.save()

        return lesson_data

    @staticmethod
    def get_by_lesson(lesson: Lesson) -> LessonData:
        lesson_data = db.session.query(LessonData).filter(LessonData.lesson_id == lesson.id).first()
        return lesson_data
