class ParalympicEvent:
    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)

    def __str__(self):
        """User-friendly string representation"""
        return f"{self.name} ({self.sport}, Class {self.classification}) with {len(self.athletes)} athlete(s)"
    
    def __repr__(self):
        """Unambiguous representation for debugging"""
        return (f"ParalympicEvent(name='{self.name}', sport={self.sport}, "
                f"classification={self.classification}, athletes={self.athletes})")

    @staticmethod
    def is_valid_classification(classification):
        """Checks if the classification is within a valid range"""
        return 1 <= classification <= 10

ev = ParalympicEvent(name="Boccia Pairs", sport="Boccia", classification="BC4")
ev.register_athlete(athlete_name="Alison Levine")
print(repr(ev))
print(ev)


