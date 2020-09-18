from datetime import timedelta
from typing import List

import click

from lessons_crawler.db import db
from lessons_crawler.models.lessons import Lesson
from lessons_crawler.models.subjects import Subject


class LessonDAO:
    @staticmethod
    def create_or_update(
            subject: Subject, lesson_index: str, original_url: str, title: str, xml_file: str,
            index_file: str, sync_file: str, mp4_video_file: str, webm_video_file: str, thumbnail: str,
            length: timedelta = None) -> Lesson:
        lesson = (
            db.session.
            query(Lesson).
            filter(Lesson.subject_id == subject.id).
            filter(Lesson.lesson_index == lesson_index).
            first()
        )

        if not lesson:
            lesson = Lesson()

        lesson.lesson_index = lesson_index.replace("_", " ")
        lesson.title = title
        lesson.length = length
        lesson.original_url = original_url
        lesson.subject_id = subject.id
        lesson.xml_file = xml_file
        lesson.index_file = index_file
        lesson.sync_file = sync_file
        lesson.mp4_video_file = mp4_video_file
        lesson.webm_video_file = webm_video_file
        lesson.thumbnail = thumbnail

        lesson.save()

        return lesson

    @staticmethod
    def get_all() -> List[Lesson]:
        lessons = db.session.query(Lesson).all()
        return lessons
