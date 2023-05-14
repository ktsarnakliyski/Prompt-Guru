from sqlalchemy import Column, Integer, String

from db import Base


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=255), unique=True)
    system_message = Column(String)
    message = Column(String)

    def __repr__(self):
        return "<Prompt %r>" % self.name
