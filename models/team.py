from datetime import datetime, timedelta
from typing import List

from pydantic import BaseModel, AnyUrl, Json

from .tasks import Task


class TeamMemberCharacteristics(BaseModel):
    motivation: float
    skills: dict | Json


class TeamMember(BaseModel):
    name: str
    photo: AnyUrl | None = None
    characteristics: TeamMemberCharacteristics
    task_on_work: Task | None = None
    role_on_task: str | None = None


class Team(BaseModel):
    members: List[TeamMember] | Json[List[TeamMember]]
