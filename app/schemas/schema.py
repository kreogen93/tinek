from fastapi import FastAPI
from pydantic import BaseModel


class Team(BaseModel):
    id: int
    name: str


class Match(BaseModel):
    id: int
    team1: Team
    team2: Team
    score1: int
    score2: int


class Stage(BaseModel):
    level: int
    matches: list[Match]


class Tournament(BaseModel):
    id: int
    name: str
    status: str
    stages: list[Stage]

class Score(BaseModel):
    score1: int
    score2: int