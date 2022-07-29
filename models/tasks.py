from datetime import datetime, timedelta

from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    start_datetime: datetime
    deadline: timedelta
