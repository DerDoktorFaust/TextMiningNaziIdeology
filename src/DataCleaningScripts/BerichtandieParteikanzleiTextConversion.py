##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.02.08
# Summary: Converts all files from Bericht an die Parteikanzlei from HTML to TXT
#
# Output: A .txt file in markdown
# Markdown output format is intentional; due to the way the files are structured, markdown
# will make future text cleaning easier
##########################################################################

import glob
import html2text

path = "/Users/cgoodwin/Desktop/Bericht an die Parteikanzlei HTML/*.html"

# Get all files in the directory into a list
files = glob.glob(path) #*.html above ensures only HTML files are collected

for file in files:

    file_name = file[0:-4] + "txt"
    text = open(file).read()

    with open(file_name, 'w') as output:
        output.write(html2text.html2text(text))
