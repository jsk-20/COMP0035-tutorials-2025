from database import create_db_and_tables

def main() -> None:
    create_db_and_tables()
    print("✅ Created paralympics_sqlmodel.db and all tables.")


if __name__ == "__main__":
    main()


