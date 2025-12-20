from sqlmodel import SQLModel, create_engine
from pathlib import Path

# 1. Define the classes (code not shown here)
import models

# 2. Create a connection to a SQLlite database, replace 'database_name.db' with path to the database and its name
BASE_DIR = Path(__file__).resolve().parent

# Database file inside test sql/
DB_FILE = BASE_DIR / "paralympics_sqlmodel.db"

sqlite_url = f"sqlite:///{DB_FILE}"

engine = create_engine(sqlite_url, echo=False)

# 3. Create all the tables in the database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# from sqlmodel import SQLModel, create_engine

# # 1. Define the classes (code not shown here)

# # 2. Create a connection to a SQLlite database, replace 'database_name.db' with path to the database and its name
# engine = create_engine("sqlite:///database_name.db")

# # 3. Create all the tables in the database
# SQLModel.metadata.create_all(engine)


