# occultercut_workflow
OcculterCut: A Comprehensive Survey of AT-Rich Regions in Fungal Genomes
https://academic.oup.com/gbe/article/8/6/2044/2574090

This document provides instructions on how to install and run the OcculterCut software for multiple libraries/isolates, as well as how to obtain summarized information from the output

# install in local computer or remote computer e.g. nimbus

```
#download to a directory
wget https://sourceforge.net/projects/occultercut/files/OcculterCut_v1.1.tar.gz

#extract the occultercut
tar -xzf OcculterCut_v1.1.tar.gz

#cd to the folder, update the package manager, install the g++ compiler if it's not already installed
sudo apt-get update
sudo apt install g++ 

#then run the make command to generate execuatble files
make
```

# run the program

#create list of isolates ID / library
`ls -1 *_ncl_assembly.fasta | sed 's/_ncl_assembly.fasta//' >list.txt`

- then run the script
```
#!/bin/bash

# Read the IDs from the list.txt file
while IFS= read -r library; do

  # Create a folder for the current ID
  mkdir -p ./results/$library

  # Run OcculterCut for the current ID
  ./OcculterCut_v1.1/OcculterCut -f ./path/${library}_ncl_assembly.fasta

  # Move the output files to the respective folder
  mv *.txt *.gff3 *.R0 *.R1 *.plt ./results/$library/

done < ./dpird_assembly/list.txt #if list in different directory, you have to provide path
```

# getting the summary reports
- the above script will create a directory: results
- download above summary scripts: calculate_10_percentile_bin_gc.py and calculate_summary_gc_at_length_percent.py in the results directory and run, it extract AT and GC percentage/length info, and GC profiles in ~10 percentile bins info for all the isolates/libraries.
- then run final_gc_at_summary_table.py it should generate a summary of AT and GC percentage/length and final_10_percentile_bin_summary_table.py should generate a summary of gc_10_percentile_bin as csv
