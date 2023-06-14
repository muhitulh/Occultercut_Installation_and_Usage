#!/bin/bash

# Read the IDs from the list.txt file
while IFS= read -r library; do

  # Create a folder for the current ID
  mkdir -p ./results_dpird/$library

  # Run OcculterCut for the current DPIRD ID
  ./OcculterCut_v1.1/OcculterCut -f ./dpird_assembly/${library}_ncl_assembly.fasta

  # Move the output files to the respective folder
  mv *.txt *.gff3 *.R0 *.R1 *.plt ./results_dpird/$library/
done < ./dpird_assembly/list.txt
