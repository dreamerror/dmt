from datetime import datetime, timedelta

from pydantic import BaseModel

from .team import TeamMember


class Task(BaseModel):
    title: str
    description: str
    start_datetime: datetime
    deadline: timedelta
    task_leader: TeamMember | None = None
