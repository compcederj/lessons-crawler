import click

from lessons_crawler.dao.lesson_dao import LessonDAO
from lessons_crawler.dao.subject_dao import SubjectDAO
from lessons_crawler.models.lesson_data import LessonData
from lessons_crawler.models.subjects import Subject


class LessonsUpdater:
    FIRST_LESSON_PATH = "Aula_001"

    def run(self):
        subjects = SubjectDAO.get_all()

        for subject in subjects:
            click.echo(subject)
            self.create_lessons(subject)

    def create_lessons(self, subject: Subject):
        first_lesson = LessonData(subject.code, self.FIRST_LESSON_PATH)
        if first_lesson.exists():
            lesson = LessonDAO.create_or_update(
                subject=subject,
                lesson_index=first_lesson.lesson_path,
                original_url=first_lesson.lesson_url,
                title=first_lesson.title,
                xml_file=first_lesson.xml_url,
                index_file=first_lesson.index,
                sync_file=first_lesson.sync,
                mp4_video_file=first_lesson.video_mp4,
                webm_video_file=first_lesson.video_webm,
                thumbnail=first_lesson.thumbnail
            )
            click.echo(lesson)
        for lesson in first_lesson.related_lessons:
            if lesson.exists():
                lesson = LessonDAO.create_or_update(
                    subject=subject,
                    lesson_index=lesson.lesson_path,
                    original_url=lesson.lesson_url,
                    title=lesson.title,
                    index_file=lesson.index,
                    xml_file=first_lesson.xml_url,
                    sync_file=lesson.sync,
                    mp4_video_file=lesson.video_mp4,
                    webm_video_file=lesson.video_webm,
                    thumbnail=lesson.thumbnail
                )
                click.echo(lesson)
