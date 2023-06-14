# Initialize variables
sum_values = 0
output_table = []

# Read the list.txt file to get the subfolder names
with open("list.txt", "r") as list_file:
    subfolders = list_file.read().splitlines()

# Process each subfolder
for subfolder in subfolders:
    # Construct the path to the compositionGC.txt file in the subfolder
    file_path = f"./{subfolder}/compositionGC.txt"

    # Reset the sum for each subfolder
    sum_values = 0

    # Open the compositionGC.txt file for reading
    with open(file_path, "r") as file:
        # Iterate over each line in the file
        for index, line in enumerate(file):
            # Split the line into columns
            columns = line.strip().split()

            # Get the second column value
            second_column = float(columns[1])

            # Add the second column value to the sum
            sum_values += second_column

            # Check if we reached the end of a group of 10 values or the last row
            if (index + 1) % 10 == 0 or index == 100:
                # Determine the range for the current group
                start_range = (index // 10) * 10 + 1
                end_range = start_range + 9

                # Add the sum of values for the current group to the output table
                output_table.append((f"{subfolder}: {start_range}-{end_range}", sum_values))

                # Reset the sum for the next group
                sum_values = 0

# Open the summary file for writing
with open("summary_10_bins_percent_GC.txt", "w") as summary_file:
    # Write the output table to the summary file
    for range_value, sum_value in output_table:
        summary_file.write(f"{range_value}: {sum_value}\n")

