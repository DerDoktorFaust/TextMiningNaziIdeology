##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2023.11.11
# Summary: Converts all files from Bericht an die Parteikanzlei
# from the NSHWE De Gruyter database from HTML to PDF format
#
# This script simply gets all the file names in the path using GLOB
# then it goes through using PDFKit which calls WKHTMLTOPDF
##########################################################################

import pdfkit
import glob

# My path to the database files
path = "/Users/cgoodwin/Desktop/Bericht an die Parteikanzlei/*.html"

# Get all files in the directory into a list
files = glob.glob(path) #*.html above ensures only HTML files are collected

for file in files:
    # from_file is for local files and local file access MUST be enabled
    pdfkit.from_file(file, file[0:len(file)-5] + ".pdf", options={"enable-local-file-access" :""})