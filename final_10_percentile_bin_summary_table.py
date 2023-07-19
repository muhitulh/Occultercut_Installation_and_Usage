
import pandas as pd

# Replace 'dpird_summary_10_bins_percent_GC.txt' with the actual path to your file
file_path = 'summary_10_bins_percent_GC.txt'

# Read the data from the file and specify column names
data = pd.read_table(file_path, delimiter=':', names=['ID', 'Header', 'Value'])

# Pivot the table to get the desired format
pivot_df = data.pivot(index='ID', columns='Header', values='Value')

# Reset the index and rename the columns
pivot_df = pivot_df.reset_index()
pivot_df.columns.name = None

# Save the resulting dataframe to a new CSV file
output_csv_file = 'summary_gc_10percentile.csv'
pivot_df.to_csv(output_csv_file, index=False)