#####################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2023.11.01
# Summary: Renames all Meldungen aus dem Reich files
# from the NSHWE De Gruyter database.
# All files named in pattern: numberInSeries.html
# Uses Beautiful Soup to get HTML text
# Then renames according to patter "date - Meldungen aus dem Reich.html"
# Date format: YYYY.MM.DD
#
# All HTML file's first text line is of example: "Bericht zur innenpolitischen Lage (Nr. 8) 25. Oktober 1939"
# The script isolates that line, removes white space, captures the date after the ")" character,
# captures the month after the "." that comes after the date day, then grabs the year at the end.
# It then uses that as the basis for creating the final file name.
#
# Notable exceptions in database: Out of about 350 files, about 5 have the pattern "(Nr. #) vom DD Month YYYY"
# These don't fit the pattern of the script and were manually altered
# as it made more sense than to alter the script to account for something of such low frequency.

from bs4 import BeautifulSoup

import os

# Dictionary that translates German text of month to number string
month_dict = {"Januar":"01",
        "Februar":"02",
        "März":"03",
        "April":"04",
        "Mai":"05",
        "Juni":"06",
        "Juli":"07",
        "August":"08",
        "September":"09",
        "Oktober":"10",
        "November":"11",
        "Dezember":"12"}

# My path to the database files
path = "/Users/cgoodwin/Desktop/Meldungen aus dem Reich"

# Get all files in the directory into a list
files = os.listdir(path)

# Remove non-HTML stray files
for i in range(len(files)-1):
    print(files[i][-4:-1])
    if files[i][-4:-1] != "htm":
        print("here")
        del files[i]


for file in files:

    # Open each file in BeautifulSoup
    page = open(path + "/" + file)
    soup = BeautifulSoup(page, features="html.parser")

    text = soup.get_text()
    lines = text.splitlines()

    # Cut all trailing white space on each side of line and all spaces in the line
    for line in lines:
        if line != "":
            title = line.strip()
            title = title.replace(" ", "")
            break

    # The year is just the last four characters in the line
    year = title[len(title)-4: len(title)]

    day = ""

    # Find the start position, which occurs after the ")" in the line
    # then find the end position of the day date, which is just before the "." (that comes after the ")")
    for i in range(len(title)):

        if title[i] == ")":
            pos_start = i+1

            for j in range(i+1, len(title)):
                if title[j] == ".":
                    pos_end = j
                    break
            break

    day = title[pos_start:pos_end]

    # If the day is less than 10, we need to add a 0 so we always have our DD date format
    if int(day) < 10:
        day = "0" + day

    month = title[pos_end+1:len(title)-4]

    new_file_name = year + "." + month_dict[month] + "." + day + " - Meldungen aus dem Reich.html"

    # Uses os.replace because script had to be run multiple times to get script to work and replace always
    # overwrites, in contrast to os.rename (but os.rename would work too)
    os.replace(src=os.path.join(path, file), dst=os.path.join(path, new_file_name))

