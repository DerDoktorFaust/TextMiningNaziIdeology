##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.07
# Summary: Cleans text files of extraneous text created by original database creators
#
# Outputs: Cleand .txt file of each original .txt file
##########################################################################

import glob

input_path = "/Users/cgoodwin/Desktop/Meldungen aus dem Reich TXT/*.txt"

# Get all files in the directory into a list
files = glob.glob(input_path) #*.txt above ensures only text files are collected

for file in files:

    file_name = file[0:-3] + "txt"

    output_file = open(file_name[0:-4] + " Cleaned.txt", "w")


    lines = open(file).readlines()

    begin_count = 0 # used to discover where to begin writing file (after extraneous front matter from original file)

    for line in lines:

        if line[0:20] == "**Source Citation:**":
            break

        if begin_count >= 1 and line[0:24] != "![](images/minusbox.gif)":
            output_file.write(line)

        if line[0:24] == "![](images/minusbox.gif)" and begin_count == 0:
            begin_count += 1
