from sqlalchemy import Column, Integer, String

from db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80))
    email = Column(String(120), unique=True)

    def __repr__(self):
        return "<User %r>" % self.name
