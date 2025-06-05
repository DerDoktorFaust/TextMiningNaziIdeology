##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.07
# Summary: Combines all cleaned text files into one file for Meldungen aus dem Reich
#
# Outputs: One text file
##########################################################################

import glob
import shutil

input_path = "/Users/cgoodwin/Desktop/Meldungen aus dem Reich TXT Cleaned/*.txt"

output_file = "/Users/cgoodwin/Desktop/Meldungen aus dem Reich TXT Cleaned/Meldungen aus dem Reich Combined.txt"

# Get all files in the directory into a list
files = glob.glob(input_path) #*.txt above ensures only text files are collected

with open(output_file, 'w') as outfile:
    for file in files:
        with open(file, 'r') as infile:
            shutil.copyfileobj(infile, outfile)