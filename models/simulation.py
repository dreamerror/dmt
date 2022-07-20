from typing import List

from pydantic import BaseModel, Json

from .events import Event
from .team import Team


class SimulationSettings(BaseModel):
    speed: float
    difficulty: int


class Simulation(BaseModel):
    title: str
    description: str
    start_events: List[Event] | Json[List[Event]]
    settings: SimulationSettings
    team: Team
