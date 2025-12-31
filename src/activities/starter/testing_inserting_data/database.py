""" Creates the database file with tables

Note:
    The models import is required for the create_all to create the tables.

    from activities.starter.testing_inserting_data import models

    """
from importlib import resources

from sqlmodel import SQLModel, create_engine, text, Session

from activities.starter import testing_inserting_data
from activities.starter.testing_inserting_data import models
from activities.starter.testing_inserting_data.models import Teacher

student_db = resources.files(testing_inserting_data).joinpath("students.sqlite")
sqlite_url = f"sqlite:///{str(student_db)}"
# echo=True means the SQL executed by SQLModel will be output to the terminal when the code is run.
# This can be useful for debugging.
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))  # for SQLite foreign key support
        SQLModel.metadata.create_all(engine)


def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)


def insert_sample_teacher():
    teacher = Teacher(
        teacher_name="Ani Sarana",
        teacher_email="as@school.com"
    )

    with Session(engine) as session:
        session.add(teacher)
        session.commit()