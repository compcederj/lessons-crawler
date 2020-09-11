from lessons_crawler.db import db, Base, Column, ForeignKey, Integer, Unicode, Time, DateTime, func, relationship
from lessons_crawler.models.subjects import Subject
from lessons_crawler.models.professors import Professor


class Lesson(Base):
    __tablename__ = "lessons"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    lesson_index = Column("lesson_index", Unicode(10), nullable=False, index=True)
    title = Column("title", Unicode(100), nullable=False)
    length = Column("length", Time())
    original_url = Column("original_url", Unicode(), nullable=False)
    index_file = Column("index_file", Unicode(100), nullable=False)
    xml_file = Column("xml_file", Unicode(100), nullable=False)
    sync_file = Column("sync_file", Unicode(100), nullable=False)
    mp4_video_file = Column("mp4_video_file", Unicode(100), nullable=False)
    webm_video_file = Column("webm_video_file", Unicode(100), nullable=False)
    thumbnail = Column("thumbnail", Unicode(100), nullable=False)

    subject_id = Column(
        "subject_id",
        Integer,
        ForeignKey("subjects.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )
    created_at = Column("created_at", DateTime(), server_default=func.now())
    updated_at = Column("updated_at", DateTime(), server_default=func.now(), onupdate=func.now())

    subject = relationship(Subject, backref="lesson")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<Lesson: "
                f"id: {self.id}, "
                f"lesson_index: {self.lesson_index}, "
                f"title: {self.title}"
                f">")


class ProfessorLesson(Base):
    __tablename__ = "professors_lessons"
    lesson_id = Column(
        "lesson_id",
        Integer,
        ForeignKey("lessons.id", ondelete="CASCADE", onupdate="CASCADE"),
        primary_key=True
    )
    subject_id = Column(
        "subject_id",
        Integer,
        ForeignKey("subjects.id", onupdate="CASCADE"),
        primary_key=True
    )
    professor_id = Column(
        "professor_id",
        Integer,
        ForeignKey("professors.id", ondelete="SET NULL", onupdate="CASCADE"),
        primary_key=True
    )

    lesson = relationship(Lesson, backref="professor_lesson")
    subject = relationship(Subject, backref="professor_lesson")
    professor = relationship(Professor, backref="professor_lesson")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<ProfessorSubject: "
                f"subject_id: {self.subject_id}, "
                f"professor_id: {self.professor_id}"
                f">")
