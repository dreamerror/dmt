from datetime import datetime, timedelta
from typing import List, Tuple

from pydantic import BaseModel, Json

from .team import TeamMember


class Task(BaseModel):
    title: str
    description: str
    start_datetime: datetime
    deadline: timedelta
    members_and_roles: List[Tuple[TeamMember, str]] | Json[List[Tuple[TeamMember, str]]]
