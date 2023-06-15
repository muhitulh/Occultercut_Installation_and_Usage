# occultercut_run
OcculterCut: A Comprehensive Survey of AT-Rich Regions in Fungal Genomes
https://academic.oup.com/gbe/article/8/6/2044/2574090

this document is provided to outline how to install and run the occultercut software for multiple libraries/isolates, also getting summarized info from the output. 

# install in local computer or remote computer e.g. nimbus

```
#download to a directory
wget https://sourceforge.net/projects/occultercut/files/OcculterCut_v1.1.tar.gz

#extract the occultercut
tar -xzf OcculterCut_v1.1.tar.gz

#cd to the folder, then run
sudo apt-get update
sudo apt install g++ #if not installed

#then 
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

  # Run OcculterCut for the current DPIRD ID
  ./OcculterCut_v1.1/OcculterCut -f ./dpird_assembly/${library}_ncl_assembly.fasta

  # Move the output files to the respective folder
  mv *.txt *.gff3 *.R0 *.R1 *.plt ./results/$library/

done < ./dpird_assembly/list.txt #if list in different directory, you have to provide path
```

# getting the summary reports
- the above script will create a directory: results
- download two summary scripts in that folder and run, it should generate summary of AT and GC percentage/lenght, and GC profiles in ~10 percentile bins for all the isolates/libraries.
