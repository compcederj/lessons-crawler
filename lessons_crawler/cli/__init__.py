import click

from lessons_crawler.app.lesson_data_updater import LessonDataUpdater
from lessons_crawler.app.lessons_updater import LessonsUpdater


@click.group()
def cli():
    ...


@cli.command()
def update_lesson():
    lessons_updater = LessonsUpdater()
    lessons_updater.run()
    click.echo("Lessons updated!")


@cli.command()
def update_lesson_data():
    lesson_data_updater = LessonDataUpdater()
    lesson_data_updater.run()
    click.echo("Lesson_data updated!")
