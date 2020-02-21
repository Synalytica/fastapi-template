from typing import List
from .base import Base

class UserInResponse(Base):
    users: List[dict] = []
