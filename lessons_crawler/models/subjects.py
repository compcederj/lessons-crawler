from enum import Enum

from lessons_crawler.db import db, Base, Column, ForeignKey, Integer, Unicode, DateTime, func, relationship, DbEnum
from lessons_crawler.models.professors import Professor


class SubjectTypeEnum(Enum):
    OBRIGATORIA = 1
    OPCIONAL = 2


class Subject(Base):
    __tablename__ = "subjects"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    code = Column("code", Unicode(8), unique=True, nullable=False)
    name = Column("name", Unicode(70), nullable=False)
    type = Column("type", DbEnum(SubjectTypeEnum), nullable=False)
    workload = Column("workload", Integer, nullable=False)
    amount_lessons = Column("amount_lessons", Integer, nullable=False, default=0)
    drive_link = Column("drive_link", Unicode())
    whatsapp_link = Column("whatsapp_link", Unicode())
    github_link = Column("github_link", Unicode())
    created_at = Column("created_at", DateTime(), server_default=func.now())
    updated_at = Column("updated_at", DateTime(), server_default=func.now(), onupdate=func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<Subject: "
                f"id: {self.id}, "
                f"code: {self.code}, "
                f"name: {self.name}"
                f">")


class ProfessorSubject(Base):
    __tablename__ = "professors_subjects"
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

    subject = relationship(Subject, backref="professor_subject")
    professor = relationship(Professor, backref="professor_subject")

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<ProfessorSubject: "
                f"subject_id: {self.subject_id}, "
                f"professor_id: {self.professor_id}"
                f">")
