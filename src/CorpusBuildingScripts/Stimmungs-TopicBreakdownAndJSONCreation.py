##########################################################################
# Author: Christopher Thomas Goodwin
# Creation Date: 2025.06.05
# Summary: Previously, the SD reports were broken down simply by report on each date.
# This means that each broad category (Economics, Justice, etc.) are all mixed in together
# because the only criterion for categorization was date.
# This script creates all new files to bring together larger categories and separate them out.
# This allows further machine learning analyses to dive more deeply into each topic. Rather than
# looking at each document and categorizing it as "Economics," it will now have all the Economics
# documents together and will give more specific topics.
#
# Outputs: Text files for each SD-report broken down along larger categories; JSON files for each of
# these large categories
##########################################################################