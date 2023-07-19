import pandas as pd
import pandas as pd

# Replace 'gc_at_calculation_summary.txt' with the actual path to your file
file_path = 'dpird_gc_at_calculation_summary.txt'

# Read the data from the file and specify column names
data = pd.read_csv(file_path, delimiter=':', names=['Column', 'Value'])

# Extract the first column as the row names
data['Sample'] = data['Column'].str.split().str[0]

# Extract the second, third, and fourth words from the 'Column' and concatenate them into the 'Header' column
data['Header'] = data['Column'].str.split().str[1] + ' ' + data['Column'].str.split().str[2] + ' ' + data['Column'].str.split().str[3]

# Group by 'Sample' and 'Header' and aggregate values as lists
final_table = data.groupby(['Sample', 'Header'])['Value'].agg(list).unstack()

print(final_table)

# Print the final_table as a CSV file
final_table.to_csv('output.csv', index=True)


import csv

input_file = "output.csv"
output_file = "final_gc_at_summary_table.csv"

def clean_value(value):
    return value.strip("[]").split(", ")

with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = ["Sample", "GC Rich Percentage", "rp_ro", "GC Rich Region", "rr_ro", "R0 GC peak", "R1 GC peak"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        gc_percentage = clean_value(row["GC Rich Percentage"])
        gc_region = clean_value(row["GC Rich Region"])
        row["GC Rich Percentage"] = gc_percentage[0]
        row["rp_ro"] = gc_percentage[1]
        row["GC Rich Region"] = gc_region[0]
        row["rr_ro"] = gc_region[1]
        row["R0 GC peak"] = clean_value(row["R0 GC peak"])[0]
        row["R1 GC peak"] = clean_value(row["R1 GC peak"])[0]
        writer.writerow(row)