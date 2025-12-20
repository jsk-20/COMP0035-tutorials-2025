from datetime import date
from enum import Enum
from typing import Optional

from sqlmodel import Field, SQLModel


class Games(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    type: str = Field()
    year: int
    start: date
    end: date
    countries: int
    events: int
    sports: int
    participants_m: int
    participants_f: int
    participants: int
    highlights: str
    URL: str


class Country(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    country: str

class Disability(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str


class Region(str, Enum):
    Asia = "Asia"
    Europe = "Europe"
    Africa = "Africa"
    America = "America"
    Oceania = "Oceania"


class MemberType(str, Enum):
    country = "country"
    team = "team"
    dissolved = "dissolved"
    construct = "construct"


class Team(SQLModel, table=True):
    code: str = Field(primary_key=True)
    name: str
    region: Optional[Region] = Field(default=None)
    sub_region: str
    member_type: Optional[MemberType] = Field(default=None)
    notes: str
    country_id: Optional[int] = Field(
        default=None,
        foreign_key="country.country_id",
        onupdate="CASCADE",
        ondelete="SET NULL"
    )
