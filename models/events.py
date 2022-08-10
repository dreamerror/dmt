from typing import List

from pydantic import BaseModel, Json

from .actions import Action
from .tasks import Task


class Event(BaseModel):
    type: str = "email"
    title: str
    message: str
    previous_action: Action | None = None
    possible_actions: List[Action] | Json[List[Action]] | None = None
    connected_task: Task
