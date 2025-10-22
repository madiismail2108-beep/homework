from enum import Enum
from dataclasses import dataclass

class TODOTYPE(Enum):
    PERSONAL="personal"
    WORKING="workining"

class UserROLE(Enum):
    ADMIN='ADMIN'
    USER='user'

@dataclass
class USER:
    username: str
    password: str
    email: str|None = None
    id: int|None=None
    role: UserROLE=UserROLE.USER.value
    created_at: None = None

    @staticmethod
    def from_tuple(user_data: tuple):
        return USER(
            id= user_data[0],
            username=user_data[1],
            password=user_data[2],
            role=user_data[3],
            email=user_data[4],
            created_at=user_data[5]
        )
    
@dataclass
class TODO:
    title : str
    user_id : int
    description : str | None = None
    todo_type : TODOTYPE = TODOTYPE.PERSONAL.value
    created_at : None = None
    id : int | None = None
