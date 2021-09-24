from sqlalchemy.orm import Session

from server.core.models import Redis
from server.core.models.student import Student


def get_teacher_students(session: Session):
    student_numbers = Redis.keys()

    students = session.query(Student)\
        .filter(Student.number.in_(student_numbers))\
        .order_by(Student.number)\
        .all()

    return [{
        "number": student.number,
        "name": student.name,
        "black_list": Redis.get(2211).decode("ascii").split("|")
    } for student in students ]
