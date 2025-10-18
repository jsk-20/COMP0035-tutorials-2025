"""
Examples of docstring styles and functions and class
that are un-documented.
"""
import sqlite3

import pandas as pd
from matplotlib import pyplot as plt
import os
import io


# Google-style docstring specification:
# https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings
def get_column_names_g(db_path: str, table_name: str) -> list:
    """Retrieves a list of column names for the specified database table.

    Args:
        db_path: Path to the database file
        table_name: Name of the table

    Returns:
        col_names: List of column names
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Numpy-style docstring:
# https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard
def get_column_names_n(db_path: str, table_name: str) -> list:
    """
        Retrieves a list of column names for the specified database table.

        Parameters
        ----------
        db_path : str
            Path to the database file.
        table_name : str
            Name of the table.

        Returns
        -------
        col_names: list
            List of column names.
        """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Sphinx/reStructuredText style docstring:
# https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
# AI prompt:   /doc Sphinx format docstring
def get_column_names_s(db_path: str, table_name: str) -> list:
    """
        Retrieves a list of column names for the specified database table.

        :param db_path: Path to the database file.
        :type db_path: str
        :param table_name: Name of the table.
        :type table_name: str
        :return: List of column names.
        :rtype: list
        """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name});")
    col_names = [row[1] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return col_names


# Copilot in VSCode / PyCharm
# Place the cursor under the function name and generate a docstring
# e.g. '/doc Google-style docstring'
def generate_histogram(df: pd.DataFrame):
    """Generate and save histograms from a DataFrame.

    This function creates and saves three histogram plots from the provided
    pandas DataFrame:
    1. A grid of histograms for all columns with plottable dtypes (one subplot
        per column) saved to "output/histogram_df.png".
    2. A histogram grid for the two participant columns
        ("participants_m", "participants_f") saved to
        "output/histogram_participants.png".
    3. A histogram grid for rows where the "type" column equals "summer" saved
        to "output/histogram_summer.png".

    Plotting options:
    - For the first and third plots, subplots do not share y-axes
      (sharey=False) and
      the figure size is set to (12, 8) inches. The second plot uses pandas'
      default histogram layout.

    Args:
         df (pd.DataFrame): Input data frame containing the columns to plot.
            Expected to contain numeric columns for general histograms and the
              following specific columns for the other plots:
                 - "participants_m" (numeric)
                 - "participants_f" (numeric)
                 - "type" (categorical/string)

    Returns:
         None

    Side effects:
         Saves three PNG files to the "output" directory:
            - output/histogram_df.png
            - output/histogram_participants.png
            - output/histogram_summer.png

    Raises:
         KeyError: If required columns ("participants_m", "participants_f",
            "type") are missing from df when those specific histograms are
            requested.
         FileNotFoundError: If the "output" directory does not exist and
                cannot be created by the caller prior to saving.
         ImportError: If required plotting libraries (pandas/matplotlib) are
            not available in the environment.

    Example:
         >>> import pandas as pd
         >>> df = pd.DataFrame({
         ...     "participants_m": [10, 12, 7],
         ...     "participants_f": [8, 9, 11],
         ...     "type": ["summer", "winter", "summer"],
         ...     "score": [3.5, 4.0, 2.8]
         ... })
         >>> generate_histogram(df)
         # Produces three PNG files in the "output" directory.
    """
    # Histogram of any columns with values of a data type that can be plotted
    df.hist(
        sharey=False,  # defines whether y-axes will be shared among subplots.
        figsize=(12, 8)  # a tuple (width, height) in inches
    )
    plt.savefig("output/histogram_df.png")

    # Histograms of specific columns only
    df[["participants_m", "participants_f"]].hist()
    plt.savefig("output/histogram_participants.png")

    # Histograms based on filtered values
    summer_df = df[df['type'] == 'summer']
    summer_df.hist(sharey=False, figsize=(12, 8))
    plt.savefig("output/histogram_summer.png")


# Copilot in VSCode / PyCharm
# If you are happy to use gen-AI tools, place the cursor under the docstring
# and ask the AI to generate the code
def describe(csv_data_file: str) -> dict:
    """Opens the data as a pandas DataFrame, applies common pandas summaries,
    writes the outputs to a text file in the output/ directory, and returns a
    dict of the results.
    """

    # Read CSV
    df = pd.read_csv(csv_data_file)

    # Compute summaries
    shape = df.shape
    head_df = df.head()
    tail_df = df.tail()
    columns = df.columns.tolist()
    dtypes = df.dtypes.apply(lambda dt: str(dt)).to_dict()
    describe_dict = df.describe(include='all').to_dict()
    buf = io.StringIO()
    df.info(buf=buf)
    info_str = buf.getvalue()

    # Prepare output directory and filename
    out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(csv_data_file))[0]
    out_path = os.path.join(out_dir, f"describe_{base_name}.txt")

    # Write human-readable report to file
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"File: {csv_data_file}\n")
        f.write(f"Shape: {shape}\n\n")

        f.write("Head:\n")
        f.write(head_df.to_string(index=True))
        f.write("\n\n")

        f.write("Tail:\n")
        f.write(tail_df.to_string(index=True))
        f.write("\n\n")

        f.write("Columns:\n")
        for col in columns:
            f.write(f" - {col}\n")
        f.write("\n")

        f.write("Dtypes:\n")
        for col, dt in dtypes.items():
            f.write(f" - {col}: {dt}\n")
        f.write("\n")

        f.write("Describe (include='all'):\n")
        # Use DataFrame string representation for readability
        f.write(df.describe(include='all').to_string())
        f.write("\n\n")

        f.write("Info:\n")
        f.write(info_str)

    # Return machine-friendly results
    return {
        "shape": shape,
        "head": head_df.to_dict(orient="list"),
        "tail": tail_df.to_dict(orient="list"),
        "columns": columns,
        "dtypes": dtypes,
        "describe": describe_dict,
        "info": info_str,
        "output_file": out_path,
    }
