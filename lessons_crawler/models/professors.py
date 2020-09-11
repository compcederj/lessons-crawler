from lessons_crawler.db import Base, Column, Integer, Unicode, DateTime, func, db


class Professor(Base):
    __tablename__ = "professors"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", Unicode(70), nullable=False)
    email = Column("email", Unicode(100))
    site = Column("site", Unicode())
    created_at = Column("created_at", DateTime(), server_default=func.now())
    updated_at = Column("updated_at", DateTime(), server_default=func.now(), onupdate=func.now())

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return (f"<Professor: "
                f"id: {self.id}, "
                f"name: {self.name}, "
                f"email: {self.email}, "
                f"site: {self.site}"
                f">")

    def __str__(self):
        return self.name
