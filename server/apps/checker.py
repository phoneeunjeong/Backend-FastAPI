from fastapi import APIRouter, status

from server.core.models import session_scope
from server.core.schemas.checker import PostBlackList

from server.utils.checker import get_checker_students, create_black_list


router = APIRouter()


@router.get("/checker", status_code=status.HTTP_200_OK, tags=["checker"])
async def get_students(grade: int, cls: int, gender: str):
    with session_scope() as session:
        students = get_checker_students(session=session, grade=grade, cls=cls, gender=gender)

        return students


@router.post("/submit", status_code=status.HTTP_201_CREATED, tags=["checker"])
async def post_black_list(body: PostBlackList):
    with session_scope() as session:
        create_black_list(session=session, number=body.number, name=body.name, black_list=body.black_list)

        return {
            "message": "success"
        }
