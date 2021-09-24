from pydantic import BaseModel
from pydantic.types import conint, constr, conlist

from enum import Enum


class BlackListEnum(str, Enum):
    phone = "phone"
    school_laptop = "s_laptop"
    personal_laptop = "p_laptop"


class PostBlackList(BaseModel):
    number: conint(ge=1000, le=9999)
    name: constr(min_length=2, max_length=4)
    black_list: conlist(item_type=BlackListEnum, min_items=1, max_items=3)
