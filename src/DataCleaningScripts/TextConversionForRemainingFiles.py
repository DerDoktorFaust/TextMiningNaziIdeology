##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2024.02.08
# Summary: Converts all files the following from HTML to TXT:
# Bericht aus Akten der Geschäftsführenden Reichsregierung Dönitz
# Meldungen aus dem Reich
# Meldungen aus den SD-Abschnittsbereichen
# Meldungen über die Entwicklung in der öffentlichen Meinungsbildung
# SD-Berichte zu Inlandsfragen
# Vierteljahreslagebericht des Sicherheitshauptamtes
#
# Output: A .txt file in markdown
# Markdown output format is intentional; due to the way the files are structured, markdown
# will make future text cleaning easier
#
# Another method for this would be to go through a higher level directory and simply
# convert all HTML files found, but I wanted to be explicit about what this script converts
# for better tracking the research process.
##########################################################################

import glob
import html2text

paths = ["/Users/cgoodwin/Desktop/Bericht aus Akten der Geschäftsführenden Reichsregierung Dönitz HTML/*.html",
         "/Users/cgoodwin/Desktop/Meldungen aus dem Reich HTML/*.html",
         "/Users/cgoodwin/Desktop/Meldungen aus den SD-Abschnittsbereichen HTML/*.html",
         "/Users/cgoodwin/Desktop/Meldungen über die Entwicklung in der öffentlichen Meinungsbildung HTML/*.html",
         "/Users/cgoodwin/Desktop/SD-Berichte zu Inlandsfragen HTML/*.html",
         "/Users/cgoodwin/Desktop/Vierteljahreslagebericht des Sicherheitshauptamtes HTML/*.html"]

for path in paths:
    # Get all files in the directory into a list
    files = glob.glob(path) #*.html above ensures only HTML files are collected

    for file in files:

        file_name = file[0:-4] + "txt"
        text = open(file).read()

        with open(file_name, 'w') as output:
            output.write(html2text.html2text(text))
