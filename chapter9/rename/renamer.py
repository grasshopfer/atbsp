#! python3

# renames files with American-style dates to have European-style dates. MM-DD-YYYY to DD-MM-YYYY

import os, re, shutil

# find files in current directory with American-style dates in name
reDate = re.compile(r'\d\d-\d\d-\d\d\d\d')
reUSdate = re.compile(r"""^(.*?)            # All text before date
        ((0|1)?\d)-                         # One or two digits for the month
        ((0|1|2|3)?\d)-                     # One or two digits for the day
        ((19|20)\d\d)                       # Year beginning with 19 or 20
        (.*?)$                              # All text after the date
        """, re.VERBOSE)
curDir = os.getcwd()
files = os.listdir()

usDateFiles = []
for file in files:
    if reUSdate.match(file):
        usDateFiles.append(file)

# rename file to have Euro-style date
for file in usDateFiles:
    reResult = reUSdate.search(file)
    print(reResult)
# use shutil.move() to rename file

