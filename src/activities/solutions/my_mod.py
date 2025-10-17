from pathlib import Path
# import csv

project_root = Path(__file__).parent.parent
csv_file = project_root.joinpath('data', 'paralympics_raw.csv')
print(csv_file.exists())

# Not needed
# with open(csv_file, newline='') as f:
#     reader = csv.reader(f, delimiter=',')
#     first_row = next(reader)
#     print(first_row)
