##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.09
# Summary: Cleans text files (Bericht an den Reichsschatzmeister der NSDAP) of extraneous text created by original database creators
#
# Outputs: Cleaned .txt file of each original .txt file
##########################################################################

import glob

input_path = "/Users/cgoodwin/Desktop/Bericht an den Reichsschatzmeister der NSDAP TXT/*.txt"

# Get all files in the directory into a list
files = glob.glob(input_path) #*.txt above ensures only text files are collected

for file in files:

    file_name = file[0:-3] + "txt"

    output_file = open(file_name[0:-4] + " Cleaned.txt", "w")


    lines = open(file).readlines()

    begin_count = 0 # used to discover where to begin writing file (after extraneous front matter from original file)

    for line in lines:

        # The only cleaning really needing to be done is cutting off the end of each file that contains
        # database metadata and source information
        if line[0:20] == "**Source Citation:**":
            break
        else:
            output_file.write(line)