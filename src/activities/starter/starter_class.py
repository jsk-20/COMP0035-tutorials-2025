class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes

     """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)


## Old method to test the ParalympicEvent class
# event = ParalympicEvent(
#     name="Men's individual BC1",
#     sport="Boccia",
#     classification="BC1",
# )

# event.describe()  # Should print the event description, "Athletes competing" will be empty
# event.register_athlete("Sungjoon Jung")  # should register the athlete
# event.describe()  # Should print the event again, "Athletes competing" should include Sungjoon Jung


## New Athlete class to represent an athlete
# class Athlete:
#     """Represents an athlete competing in the Paralympics"""
#     def __init__(self, name, team, classification):
#         self.name = name
#         self.team = team
#         self.classification = classification


#     def __str__(self):
#         return (
#             f"Athlete: {self.name}, "
#             f"Team: {self.team}, "
#             f"Classification: {self.classification}"
#         )


# athlete1 = Athlete(
#     name="Sungjoon Jung",
#     team="KOR",
#     classification="BC1"
# )

# print(athlete1)


from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Medal:
    type: str
    design: str
    date_designed: date


class Athlete:
    def __init__(self, first_name: str, last_name: str, team_code: str, disability_class: str, medals: List[Medal]):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class
        self.medals = medals  # Composition: Athlete has Medals

    def __str__(self):
        medal_list = ", ".join(m.type for m in self.medals) or "None"
        return (
            f"Athlete: {self.first_name} {self.last_name}\n"
            f"Team: {self.team_code}\n"
            f"Classification: {self.disability_class}\n"
            f"Medals: {medal_list}"
        )
    
# Create medals
medal1 = Medal("gold", "Paris 2024 design", date(2023, 7, 1))
medal2 = Medal("silver", "Tokyo 2020 design", date(2019, 8, 25))

# Create an athlete with medals
athlete = Athlete(
    first_name="Wei",
    last_name="Wang",
    team_code="CHN",
    disability_class="T54",
    medals=[medal1, medal2]
)

print(athlete)