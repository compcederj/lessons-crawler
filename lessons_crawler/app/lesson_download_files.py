from lessons_crawler.dao.lesson_dao import LessonDAO
from lessons_crawler.dao.rnp_lesson_file_dao import RNPLessonFileDAO


class LessonDownloadFiles:
    @staticmethod
    def run():
        lessons = LessonDAO.get_all()
        for lesson in lessons:
            file_dao = RNPLessonFileDAO(lesson)
            file_dao.save_files()
