##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.09
# Summary: Combines all cleaned text files into one file for SD-Berichte zu Inlandsfragen
#
# Outputs: One text file
##########################################################################

import glob
import shutil

input_path = "/Users/cgoodwin/Desktop/SD-Berichte zu Inlandsfragen TXT Cleaned/*.txt"

output_file = "/Users/cgoodwin/Desktop/SD-Berichte zu Inlandsfragen TXT Cleaned/SD-Berichte zu Inlandsfragen Combined.txt"

# Get all files in the directory into a list
files = glob.glob(input_path) #*.txt above ensures only text files are collected

with open(output_file, 'w') as outfile:
    for file in files:
        with open(file, 'r') as infile:
            shutil.copyfileobj(infile, outfile)