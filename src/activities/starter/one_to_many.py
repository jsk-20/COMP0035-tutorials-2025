from sqlmodel import Field, Session, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")


# SQLModel (and SQLAlchemy) has an advantage over pure SQL as it allows you to 
# navigate the relationship from both child to parent AND parent to child by defining 
# a Relationship() attribute in both classes.

# This is the updated example from the SQLModel documentation:


from sqlmodel import Field, Relationship, SQLModel


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)

    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

# Notice that "Hero" has quote marks in heroes: list["Hero"] = Relationship(back_populates="team"). 
# This is because Hero is defined after Team, so you would get an error warning in your IDE if you try to 
# enter it as list[Hero]. Adding the "" makes the interpreter see it as a string.