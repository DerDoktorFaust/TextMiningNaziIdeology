##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2023.11.04
# Summary: Converts all Meldungen aus dem Reich files
# from the NSHWE De Gruyter database from HTML to PDF format
#
# This script was run after renaming all original HTML files to their
# proper names of the format YYYY.MM.DD - Meldungen aus dem Reich.html
# which was run with the script MeldungenausdemReichFileRenaming.py
#
# This script simply gets all the file names in the path using GLOB
# then it goes through using PDFKit which calls WKHTMLTOPDF
##########################################################################

import pdfkit
import glob

# My path to the database files
path = "/Users/cgoodwin/Desktop/Meldungen aus dem Reich/*.html"

# Get all files in the directory into a list
files = glob.glob(path) #*.html above ensures only HTML files are collected

for file in files:
    # from_file is for local files and local file access MUST be enabled
    pdfkit.from_file(file, file[0:len(file)-5] + ".pdf", options={"enable-local-file-access": ""})