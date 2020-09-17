from lessons_crawler.db import db, Base, Column, Integer, Text, JSON, ForeignKey, DateTime, func, relationship
from lessons_crawler.models.lessons import Lesson


class LessonData(Base):
    __tablename__ = "lesson_data"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    raw_xml = Column("xml_raw_data", Text)
    json_xml = Column("json_xml", JSON)
    raw_index = Column("raw_index", Text)
    json_index = Column("json_index", JSON)
    raw_sync = Column("raw_sync", Text)
    json_sync = Column("json_sync", JSON)

    lesson_id = Column(
        "lesson_id",
        Integer,
        ForeignKey("lessons.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False
    )

    created_at = Column("created_at", DateTime(), server_default=func.now())
    updated_at = Column("updated_at", DateTime(), server_default=func.now(), onupdate=func.now())

    lesson = relationship(Lesson, backref="LessonData")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<Subject: "
                f"id: {self.id}, "
                f"code: {self.lesson.title}"
                f">")
