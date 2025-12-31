from sqlmodel import Session, create_engine
# 1. Create the engine which creates the connection to the database
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

# 2. Create one or more rows to add
teacher = Teacher(name="Freida", email="freida@myorg.com")

# 3. Create a session
with Session(engine) as session:
    # 4. Add the rows (or rows if add_all)
    session.add(teacher)
    # 5. Commit the new row
    session.commit()