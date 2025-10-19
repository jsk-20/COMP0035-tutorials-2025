import importlib.resources
import sqlite3

import pandas as pd

from activities import data


def print_data(file_path):
    """
    Attempts to open and read the contents of a file, handling potential errors gracefully.

    Demonstrates the use of `try`, `except`, `else`, and `finally` blocks:
    - `try`: Attempts to open the file.
    - `except FileNotFoundError`: Handles the case where the file does not exist.
    - `except Exception`: Handles any other errors.
    - `else`: Executes if no exception occurs, print the file's contents.
    - `finally`: Executes regardless of whether an exception occurred, printing a completion message.

    Args:
        file_path: The path to the file to open.

    Raises:
        FileNotFoundError: If the file does not exist.

    """
    try:
        data = file_path.read_text()
    except FileNotFoundError as e:
        print(f'Sorry, could not find that file. Error {e}')
    else:
        print(data)
    finally:
        print('Finished attempting to read the file.')


def print_data_group_example(file_path):
    """
    Attempts to open and read the contents of a file, handling potential errors gracefully.

    Demonstrates the use of exception groups (requires Python > 3.11)

    Args:
        file_path: The path to the file to open.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file does not grant permission to open.

    """
    try:
        data = file_path.read_text()
    except* FileNotFoundError as fnf_errors:
        for e in fnf_errors.exceptions:
            # Example also using the e.add_note method
            e.add_note(f"File not found while trying to locate the traffic data set")
            raise
    except* PermissionError as perm_errors:
        for e in perm_errors.exceptions:
            print(f"Permission error: {e}")
    else:
        print(f'File contents: {data}')
    finally:
        print('Finished attempting to read the file.')


def print_data_pattern_example(file_path):
    """
    Attempts to open and read the contents of a file, handling potential errors gracefully.

    Demonstrates the use of structural pattern matching (requires Python > 3.10)

    Args:
        file_path: The path to the file to open.

    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file does not grant permission to open.

    """
    try:
        data = file_path.read_text()
    except Exception as e:
        match e:
            case FileNotFoundError():
                print(f"File not found: {e}")
            case PermissionError():
                print(f"Permission error: {e}")
    else:
        print(f'File contents: {data}')
    finally:
        print('Finished attempting to read the file.')


# Activity 4.7 add exception handling to this function
def create_db(schema_path, db_path):
    """ Create a SQLite database using the provided schema file.

    Args:
        schema_path (str): Path to the SQL schema file.
        db_path (str): Path where the SQLite database will be created.
    """
    # # Create a connection
    # conn = sqlite3.connect(db_path)
    # cursor = conn.cursor()

    # # Read the SQL schema file
    # with open(schema_path, 'r') as f:
    #     schema_sql = f.read()

    # # Execute the schema SQL
    # cursor.executescript(schema_sql)

    # # Commit and close the connection
    # conn.commit()
    # conn.close()

    conn = None

    try:
        # Try to connect to the database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Try to open and read the schema file
        with open(schema_path, 'r') as f:
            schema_sql = f.read()

        # Try to execute the SQL commands
        cursor.executescript(schema_sql)

        conn.commit()
        print(f"Database created successfully at: {db_path}")
        return True

    except FileNotFoundError:
        print(f"Error: schema file '{schema_path}' does not exist.")
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

        return False

# Activity 4.7 add exception handling to this function
def describe(file_path):
    """Uses pandas DataFrame functions to describe the data.

    Applies the following pandas functions to the DataFrame and prints the output to file instead of terminal:
        df.shape
        df.head(num)
    NB some functions removed to shorten the output for the exception handling activity!

       Args:
           file_path: The path to the .csv file.

        Raises:
            FileNotFoundError: If the file does not exist.

    """
    # df = pd.read_csv(file_path)

    # # 2.3 Describe
    # pd.set_option("display.max_columns", None)  # Change the pandas display options to print all columns
    # print("\nThe number of rows and columns\n", df.shape)
    # print("\nThe first 5 rows\n", df.head(5))

    try:
        # Try to read the CSV file
        df = pd.read_csv(file_path)

        # Print data description if successful
        pd.set_option("display.max_columns", None)
        print("\nThe number of rows and columns:\n", df.shape)
        print("\nThe first 5 rows:\n", df.head(5))

    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'.")

    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{file_path}' is empty.")

    except pd.errors.ParserError:
        print(f"Error: Could not parse the CSV file at '{file_path}'. Is it corrupted or incorrectly formatted?")

    except Exception as e:
        # Catch any other unanticipated errors
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    # Sample data files
    not_file = importlib.resources.files(data).joinpath("traffic.csv")  # exists
    is_file = importlib.resources.files(data).joinpath("student_data.csv")  # does not exist

    print_data(not_file)
    print_data(is_file)

    print_data_group_example(not_file)
    print_data_group_example(is_file)

    print_data_pattern_example(not_file)
    print_data_pattern_example(is_file)
