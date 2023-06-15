# Read the list of subfolders from the "list.txt" file
with open("list.txt", "r") as list_file:
    subfolders = list_file.read().splitlines()

# Create an empty list to store the subfolder names and output file names
output_table = []

for subfolder in subfolders:
    # Construct the path to the myGenome.txt file in the subfolder
    file_path = f"./{subfolder}/myGenome.txt"

    try:
        # Read the contents of the myGenome.txt file
        with open(file_path, "r") as file:
            content = file.readlines()

        # Find the relevant lines for Region: R1
        start_index = content.index("Region: R1\n")
        end_index = len(content)
        region_lines = content[start_index:end_index]

        # Extract GC_peak_(%GC) for Region: R1
        gc_line = region_lines[2]
        gc_peak_value = float(gc_line.split(": ")[1])

        # Extract the Proportion_of_genome value for Region: R1
        proportion_line = region_lines[3]  # Index 3 contains the Proportion_of_genome line
        proportion_value = float(proportion_line.split(": ")[1])

        # Extract the Genome_size value
        genome_size_line = content[0]  # First line contains the Genome_size value
        genome_size = float(genome_size_line.split(": ")[1])

        # Calculate the GC rich region value
        gc_rich_region = (proportion_value / 100) * genome_size

        # Find the relevant lines for Region: R0
        start_index = content.index("Region: R0\n")
        end_index = content.index("Region: R1\n")
        region_lines = content[start_index:end_index]

        # Extract GC_peak_(%GC) for Region: R0
        gc_line = region_lines[2]
        gc_peak_value_r0 = float(gc_line.split(": ")[1])

        # Extract the Proportion_of_genome value for Region: R0
        proportion_line = region_lines[3]  # Index 3 contains the Proportion_of_genome line
        proportion_value_r0 = float(proportion_line.split(": ")[1])

        # Calculate the AT rich region value
        at_rich_region = (proportion_value_r0 / 100) * genome_size

        # Append the subfolder name and output file name to the output_table list
        output_table.append((subfolder, gc_peak_value, gc_rich_region, proportion_value, gc_peak_value_r0, at_rich_region, proportion_value_r0))

    except ValueError:
        # "Region: R1" not found, move to the next subfolder
        continue

# Create the output summary file
with open("gc_at_calculation_summary.txt", "w") as output_file:
    # Write the results for each subfolder to the file
    for item in output_table:
        subfolder = item[0]
        output_file.write(f"{subfolder} R1 GC peak (%GC): {item[1]}\n")
        output_file.write(f"{subfolder} GC Rich Region (Mbp): {item[2]}\n")
        output_file.write(f"{subfolder} GC Rich Percentage: {item[3]}\n")
        output_file.write(f"{subfolder} R0 GC peak (%GC): {item[4]}\n")
        output_file.write(f"{subfolder} GC Rich Region (Mbp): {item[5]}\n")
        output_file.write(f"{subfolder} GC Rich Percentage: {item[6]}\n")

