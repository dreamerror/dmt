from pydantic import BaseModel

from .team import Team


class SimulationSettings(BaseModel):
    speed: float
    difficulty: int
    max_team_members_count: int


class Simulation(BaseModel):
    title: str
    description: str
    settings: SimulationSettings
    team: Team
