""" Mimics a typical file structure when using models classes and database witin an app

See https://sqlmodel.tiangolo.com/tutorial/code-structure/
There is no actual app code yet though!
"""
from pytest import Session
from activities.starter.testing_inserting_data.database import create_db_and_tables
from activities.starter.testing_inserting_data.models import Teacher
from para_app import database


def main():
    create_db_and_tables()
    teacher = Teacher(teacher_name="Ani Sarana", teacher_email="as@school.com")
    engine = database.engine

    with Session(engine) as session:
        session.add(teacher)
        session.commit()


if __name__ == '__main__':
    main()


#  python -m activities.starter.testing_inserting_data.app
