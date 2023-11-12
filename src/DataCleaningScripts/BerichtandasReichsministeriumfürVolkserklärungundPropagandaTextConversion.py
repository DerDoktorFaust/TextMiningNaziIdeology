##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2023.11.12
# Summary: Converts all files from Bericht an das Reichsministerium für Volksaufklärung und Propaganda from HTML to TXT
##########################################################################

from bs4 import BeautifulSoup
import glob

path = "/Users/cgoodwin/Desktop/Bericht an das Reichsministerium für Volksaufklärung und Propaganda HTML/*.html"

# Get all files in the directory into a list
files = glob.glob(path) #*.html above ensures only HTML files are collected

for file in files:
    page = open(file)
    soup = BeautifulSoup(page, features="html.parser")

    text = soup.get_text()

    file_name = file[0:-4] + "txt"

    with open(file_name, 'w') as output:
        output.write(text)