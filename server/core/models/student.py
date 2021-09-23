from sqlalchemy import Column, VARCHAR

from server.core.models import Base


class Student(Base):
    __tablename__ = "student"

    number = Column(VARCHAR(4), primary_key=True)
    name = Column(VARCHAR(4), nullable=False)
    gender = Column(VARCHAR(1), nullable=False)
