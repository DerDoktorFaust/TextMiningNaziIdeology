##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2023.11.08
# Summary: Renames all SD-Berichte zu Inlandsfragen files
# from the NSHWE De Gruyter database.
# All files originally named from downloading files and the OS adding a number to prevent duplicates
# Uses Beautiful Soup to get HTML text
# Then renames according to patter "date Part # - SD-Berichte zu Inlandsfragen.html"
# Date format: YYYY.MM.DD
#
# All HTML file's first text line is of example: "SD-Berichte zu Inlandsfragen vom DD. Month YYYY (Series designation)"
# The script isolates that line, removes white space, captures the date after "vom",
# captures the month after the "." that comes after the date day, then grabs the year at the end but before series designation
# It then uses that as the basis for creating the final file name.
# However, since multiple files have the same date but are actually different,
# a dictionary stores and counts the dates and
##########################################################################

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

new_file_names = {} # dictionary to hold and count new file names

# My path to the database files
path = "/Users/cgoodwin/Desktop/SD-Berichte zu Inlandsfragen"

# Get all files in the directory into a list

files = []

for file in os.listdir(path):
    if file.endswith(".html"):
        files.append(file)


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

    day = ""

    # Find the start position, which occurs after the "vom" in the line
    # then find the end position of the day date, which is just before the "." (that comes after the ")")
    for i in range(len(title)):

        if title[i:i+3] == "vom":
            pos_start = i+3

            for j in range(i+1, len(title)):
                if title[j] == ".":
                    pos_end = j
                    break
            break

    day = title[pos_start:pos_end]

    # If the day is less than 10, we need to add a 0 so we always have our DD date format
    if int(day) < 10:
        day = "0" + day

    pos_start = pos_end + 1

    for i in range(pos_start, len(title)):
        if title[i].isnumeric(): #stop when it gets to the year (i.e. a number)
            pos_end = i
            break

    month = title[pos_start:pos_end]

    year = title[pos_end:pos_end+4]

    new_file_name = year + "." + month_dict[month] + "." + day + " - SD-Berichte zu Inlandsfragen.html"

    # Multiple files come from the same date
    # A dictionary stores the "base" new_file_name
    # the count starts at 1 and sets the first file to "Part 1"
    # every subsequent file with the same base new_file_name adds 1 to the count

    if new_file_name in new_file_names:
        new_file_names[new_file_name] += 1
    else:
        new_file_names[new_file_name] = 1

    # the final file is of form YYYY.MM.DD Part # - SD-Berichte zu Inlandsfragen.html
    new_file_name = year + "." + month_dict[month] + "." + day + " Part " + str(new_file_names[new_file_name]) + " - SD-Berichte zu Inlandsfragen.html"

    # Uses os.replace because script had to be run multiple times to get script to work and replace always
    # overwrites, in contrast to os.rename (but os.rename would work too)
    os.replace(src=os.path.join(path, file), dst=os.path.join(path, new_file_name))

