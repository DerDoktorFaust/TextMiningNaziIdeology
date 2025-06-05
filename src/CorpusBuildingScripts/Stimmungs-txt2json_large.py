##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.10
# Summary: Converts entire database of cleaned txt files from Stimmungs- und Lageberichte to json
#
# Outputs: One json file
##########################################################################

import json
import glob
import os

input_path = "/Users/cgoodwin/Desktop/00 - All Cleaned TXT Files/*.txt"

# dictionary to store files' metadata and contents
# structure is: key: date of report, collection it came from, and contents of report
data = dict()

files = glob.glob(input_path) #*.txt above ensures only text files are collected

file_count = 0 # serves as our dictionary key

for file in files:

    filename = os.path.basename(file)[0:-12] # removes .txt extension and " Cleaned" from the filename
    date = filename[0:10] # always the first 10 characters in format yyyy.mm.dd
    collection = filename[filename.index("-")+2:] # always comes after the first hyphen in filename

    with open(file, "r") as f:
        report = f.read().splitlines() # read in as a list of strings, join later

    data[file_count] = {"date": date, "collection": collection, "report": " ".join(report)}

    file_count += 1

#convert the data dictionary to json file and write it
with open ("/Users/cgoodwin/Desktop/data.json", "w") as output_file:
    json.dump(data, output_file, ensure_ascii=False) # ensure_ascii=False to preserve umlauts