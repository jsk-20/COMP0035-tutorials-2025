from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# Not needed


# import csv

project_root = Path(__file__).parent.parent
csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
print(csv_file.exists())

# Not needed
# with open(csv_file, newline='') as f:
#     reader = csv.reader(f, delimiter=',')
#     first_row = next(reader)
#     print(first_row)


xlsx_file = project_root.joinpath('data', 'paralympics_all_raw.xlsx')
# print(xlsx_file.exists())

sheet1 = pd.read_excel(xlsx_file)
sheet2 = pd.read_excel(xlsx_file, sheet_name=1)

variable_name_for_df = pd.read_csv(csv_file)
# print(variable_name_for_df)


def describe_dataframe(df):
    """Summary or description of the function
        Parameters:
        argument1 (int): Description of argument1
        Returns:
        int: Description of the returning value
    """
    print("\n--- DataFrame Shape ---")
    print(df.shape)  # (rows, columns)

    print("\n--- First 5 Rows ---")
    print(df.head())

    print("\n--- Last 5 Rows ---")
    print(df.tail())

    print("\n--- Column Labels ---")
    print(df.columns.tolist())

    print("\n--- Column Data Types ---")
    print(df.dtypes)

    print("\n--- DataFrame Info ---")
    df.info()

    print("\n--- Descriptive Statistics ---")
    print(df.describe())

    #  Missing values
    print("\n--- Missing Values Summary ---")
    print(df.isna().sum())  # Count of missing values per column

    # Create a new DataFrame with only rows containing missing values
    missing_rows = df[df.isna().any(axis=1)]
    print(f"\nNumber of rows with missing values: {len(missing_rows)}")

    if not missing_rows.empty:
        print("\nExample rows with missing data:")
        print(missing_rows.head())
    else:
        print("No missing values found in this dataset.")


def createhist(df):
    # Create a histogram of the DataFrame
    # df.hist()
    columns = ["participants_m", "participants_f"]  # specify the columns to plot
    df[columns].hist()

    # Show the plot
    plt.show()


def boxplots(df):
    # Create boxplots of the DataFrame
    # df = pd.DataFrame(np.random.rand(10, 5), columns=["A", "B", "C", "D", "E"])
    # df.boxplot()
    # df.plot.box()  # This syntax is also valid
    columns = ["sports"]
    df[columns].boxplot()
    plt.show()


# dataframe(sheet1)

if __name__ == "__main__":
    # Filepath of the csv data file (you may have used importlib.resources
    # rather than pathlib.Path)
    paralympics_csv = (
        Path(__file__).parent.parent.joinpath("data", "paralympics_raw.csv")
    )
    # Read the data from the file into a Pandas dataframe
    events_csv_df = pd.read_csv(paralympics_csv)
    # Call the function named 'describe_dataframe' - you may have a different
    # name for your function
    describe_dataframe(events_csv_df)

    createhist(events_csv_df)

    boxplots(events_csv_df)
