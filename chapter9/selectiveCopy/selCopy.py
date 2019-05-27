#! python3

about = """# Usage: selCopy.py <file extensions, comma separated> <source dir> <target dir> 
#
#   Example: python3 selCopy.py '.jpg,.gif' /home/myhome/photos /mnt/usbDrive/photoBackup
#
#   ** only works with 3 character file extensions **
#
#   ** Directory structure is NOT preserved in target dir. **
#
# About: selCopy.py (Selective Copy) walks through a directory structure and moves files
# with certain extensions to a specified directory."""

import os, shutil, sys

# Validate args
args = sys.argv
if len(args) < 3:
    print(about)
    sys.exit()

# get file extensions
extensions = args[1].split(',')

# get absolute paths from arguments
sourceDir = os.path.abspath(args[2])
targetDir = os.path.abspath(args[3])

# validate target dir
if not os.path.isdir(targetDir):
    print('Directory ', targetDir, ' not found. Please check for typos.')

# don't overwrite over existing files
targetFiles = os.listdir(targetDir)

filesToCopy = []    # holds abs path of files in source which do not exist in target
# walk source dir, finding files with selected extensions
for root, dirs, files in os.walk(sourceDir):
    if os.path.abspath(root) == targetDir:
        continue
    for file in files:
        if file[-4:] in extensions and file not in targetFiles:
            filesToCopy.append(os.path.join(root,file))
            #print('\tCopying ', os.path.join(root,file))
            #shutil.copy(os.path.join(root,file), targetDir)

# get user confirmation:
if len(filesToCopy) > 0:
    print('The following files will be copied to ', os.path.basename(targetDir))
    for file in filesToCopy:
        print(os.path.basename(file))
    print('\nContinue? (y/n)')
    choice = input()
    if choice == 'y':
        for file in filesToCopy:
            shutil.copy(file, targetDir)
        print('All matching files copied to:\n', targetDir)
    else:
        print('No files copied')
else:
    print('All matching files already exist in target directory.')
