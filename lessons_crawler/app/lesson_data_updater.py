import click

from lessons_crawler.dao.lesson_dao import LessonDAO
from lessons_crawler.dao.lesson_data_dao import LessonDataDAO
from lessons_crawler.dao.rnp_lesson_data_dao import RNPLessonDataDAO


class LessonDataUpdater:

    def run(self):
        lessons = LessonDAO.get_all()
        for lesson in lessons:
            self.create_lesson_data(lesson)

    @staticmethod
    def create_lesson_data(lesson):
        rnp_lesson_data = RNPLessonDataDAO(lesson)
        lesson_data = LessonDataDAO.create_or_update(
            lesson,
            rnp_lesson_data.xml_raw_data,
            rnp_lesson_data.xml_json_data,
            rnp_lesson_data.index_raw_data,
            rnp_lesson_data.index_json_data,
            rnp_lesson_data.sync_raw_data,
            rnp_lesson_data.sync_json_data
        )
        click.echo(lesson_data)
