from fastapi import APIRouter, status

from server.core.models import session_scope

from server.utils.teacher import get_teacher_students


router = APIRouter()


@router.get("/teacher", status_code=status.HTTP_200_OK, tags=["teacher"])
async def get_students():
    with session_scope() as session:
        students = get_teacher_students(session=session)

        return students
