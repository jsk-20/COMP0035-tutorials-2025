""" Starter for activity 5.4 Pydantic classes with validation """
from datetime import date
from enum import Enum

from pydantic import BaseModel, Field, field_validator


# This is not a Pydantic class! It is an Enum https://docs.python.org/3/library/enum.html
class MedalType(Enum):
    BRONZE = 3
    SILVER = 2
    GOLD = 1


class Medal(BaseModel):
    """ Represents a Medal

    Attributes:
        type (MedalType):  A string representing "gold", "silver", "bronze"
        date_won (date):  Date the medal was won

    """
    type: MedalType
    date_won: date


class Athlete(BaseModel):
    """Represents an Athlete"""

    first_name: str = Field(min_length=1)
    last_name: str = Field(min_length=1)
    team_code: str = Field(min_length=3, max_length=3)
    disability_class: str
    medals: list[Medal] = Field(default_factory=list)

    @field_validator("team_code")
    @classmethod
    def team_code_must_be_uppercase(cls, value: str) -> str:
        if not value.isupper():
            raise ValueError("team_code must be uppercase (e.g. 'GBR')")
        return value

    @field_validator("disability_class")
    @classmethod
    def disability_class_not_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("disability_class cannot be empty")
        return value

    def introduce(self) -> str:
        """
                Prints an introduction of the athlete, including their name, team, and disability class.
                """
        return f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}."


class ParalympicEvent(BaseModel):
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         register_athlete() Adds an athlete to the list of athletes

     """
    name: str
    sport: str
    classification: str
    athletes: list[Athlete]

    def register_athlete(self, athlete: Athlete):
        """ Register the athlete with the event

        Args:
            athlete (Athlete): The athlete to register
        """
        self.athletes.append(athlete)



athlete = Athlete(
    first_name="Bianka",
    last_name="Pap",
    team_code="HUN",
    disability_class="T54"
)

# print(athlete.introduce())

medal1 = Medal(
    type=MedalType.GOLD,
    date_won=date(2021, 8, 29)
)   

athlete.medals.append(medal1)

# print(f"{athlete.first_name} has won {len(athlete.medals)} medal(s).")

# # --- INVALID (no try/except) ---
# bp_bad = Athlete(
#     first_name="Bianka",
#     last_name="Pap",
#     team_code="hun",          # invalid: not uppercase
#     disability_class="",      # invalid: empty after strip()
#     medals=1                  # invalid: should be a list[Medal]
# )

# print(bp_bad)  # this line will never run


from pydantic import ValidationError

# --- INVALID (with try/except) ---
try:
    bp_bad2 = Athlete(
        first_name="Bianka",
        last_name="Pap",
        team_code="hun",       # invalid
        disability_class="",   # invalid
        medals=1               # invalid
    )
except ValidationError as e:
    print("Validation failed!")
    for err in e.errors():
        print(err)
