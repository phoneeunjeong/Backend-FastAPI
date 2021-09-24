from fastapi import HTTPException, status

from sqlalchemy.orm import Session

from datetime import timedelta

from server.core.models import Redis
from server.core.models.student import Student


def get_checker_students(session: Session, grade: int, cls: int, gender: str):
    students = session.query(Student)\
        .filter(Student.number.like(f"{grade}{cls}%"), Student.gender == gender)\
        .order_by(Student.number)\
        .all()

    return [{
        "number": student.number,
        "name": student.name
    } for student in students ]


def create_black_list(session: Session, number: int, name: str, black_list: list):
    if not is_student(session=session, number=number, name=name):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="could not find student matching this")

    value = ""
    for bl in black_list:
        if black_list.index(bl) == 0:
            value += bl
        else:
            value += "|"+bl

    Redis.setex(name=f"{number}", value=value, time=timedelta(hours=18))


def is_student(session: Session, number: int, name: str):
    student = session.query(Student).filter(Student.number == number, Student.name == name).scalar()

    return True if student else False
