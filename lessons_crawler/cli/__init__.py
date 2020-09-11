import click

from lessons_crawler.app.lessons_updater import LessonsUpdater


@click.group()
def cli():
    ...


@cli.command()
def update_lesson():
    lessons_updater = LessonsUpdater()
    lessons_updater.run()
    click.echo("Lessons updated!")
