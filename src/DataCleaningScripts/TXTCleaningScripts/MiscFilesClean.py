##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.09
# Summary: Cleans text files for all other portions of NSHWE Stimmungs- und Lageberichte database
#
# Outputs: Cleand .txt file of each original .txt file and one combined file
##########################################################################

import glob

input_paths = ["/Users/cgoodwin/Desktop/Bericht an die Parteikanzlei TXT/*.txt",
               "/Users/cgoodwin/Desktop/Bericht aus Akten der Geschäftsführenden Reichsregierung Dönitz TXT/*.txt",
               "/Users/cgoodwin/Desktop/Meldungen aus den SD-Abschnittsbereichen TXT/*.txt",
               "/Users/cgoodwin/Desktop/Meldungen über die Entwicklung in der öffentlichen Meinungsbildung TXT/*.txt",
               "/Users/cgoodwin/Desktop/Vierteljahreslagebericht des Sicherheitshauptamtes TXT/*.txt"]

for input_path in input_paths:

    # Get all files in the directory into a list
    files = glob.glob(input_path) #*.txt above ensures only text files are collected

    for file in files:

        file_name = file[0:-3] + "txt"

        output_file = open(file_name[0:-4] + " Cleaned.txt", "w")

        lines = open(file).readlines()

        for line in lines:

            # The only cleaning really needing to be done is cutting off the end of each file that contains
            # database metadata and source information
            if line[0:20] == "**Source Citation:**":
                break
            else:
                output_file.write(line)