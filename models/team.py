from typing import List

from pydantic import BaseModel, AnyUrl, Json


class TeamMemberCharacteristics(BaseModel):
    motivation: float
    skills: dict | Json


class TeamMember(BaseModel):
    name: str
    photo: AnyUrl | None = None
    characteristics: TeamMemberCharacteristics


class Team(BaseModel):
    members: List[TeamMember] | Json[List[TeamMember]]
