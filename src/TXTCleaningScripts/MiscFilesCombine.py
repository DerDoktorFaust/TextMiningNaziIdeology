##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.04.09
# Summary: Combines all cleaned text files into one file for misc portions of NSHWE
#
# Outputs: One text file
##########################################################################

import glob
import shutil

input_paths = ["/Users/cgoodwin/Desktop/Bericht an die Parteikanzlei TXT Cleaned/*.txt",
               "/Users/cgoodwin/Desktop/Bericht aus Akten der Geschäftsführenden Reichsregierung Dönitz TXT Cleaned/*.txt",
               "/Users/cgoodwin/Desktop/Meldungen aus den SD-Abschnittsbereichen TXT Cleaned/*.txt",
               "/Users/cgoodwin/Desktop/Meldungen über die Entwicklung in der öffentlichen Meinungsbildung TXT Cleaned/*.txt",
               "/Users/cgoodwin/Desktop/Vierteljahreslagebericht des Sicherheitshauptamtes TXT Cleaned/*.txt"]

output_files = ["/Users/cgoodwin/Desktop/Bericht an die Parteikanzlei TXT Cleaned/Bericht an die Parteikanzlei Combined.txt",
                "/Users/cgoodwin/Desktop/Bericht aus Akten der Geschäftsführenden Reichsregierung Dönitz TXT Cleaned/Bericht aus Akten der Geschäftsführenden Reichsregierung Dönitz Combined.txt",
                "/Users/cgoodwin/Desktop/Meldungen aus den SD-Abschnittsbereichen TXT Cleaned/Meldungen aus den SD-Abschnittsbereichen Combined.txt",
                "/Users/cgoodwin/Desktop/Meldungen über die Entwicklung in der öffentlichen Meinungsbildung TXT Cleaned/Meldungen über die Entwicklung in der öffentlichen Meinungsbildung Combined.txt",
                "/Users/cgoodwin/Desktop/Vierteljahreslagebericht des Sicherheitshauptamtes TXT Cleaned/Vierteljahreslagebericht des Sicherheitshauptamtes Combined.txt"]

counter = 0 # lines up input_paths with output_files

for input_path in input_paths:

    # Get all files in the directory into a list
    files = glob.glob(input_path) #*.txt above ensures only text files are collected

    with open(output_files[counter], 'w') as outfile:
        for file in files:
            with open(file, 'r') as infile:
                shutil.copyfileobj(infile, outfile)

    counter += 1