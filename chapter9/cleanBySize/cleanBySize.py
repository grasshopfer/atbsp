#! python3

# About: cleanBySize.py walks through a directory tree looking for files
#   larger than a specified size and asks the user whether the file
#   should be kept or removed.
# Usage: python cleanBySize.py <parent directory> <max filesize>
# Example: cleanBySize.py /home/myHome/Videos/Movies 4.0GB

import os, sys, shutil, re, send2trash

# get arguments
args = sys.argv
if len(args) < 3:
    print(usage)
    sys.exit()

rootDir = os.path.abspath(args[1])
sizeArg = args[2]

# convert maxSize to byte value
byteSize = re.compile(r'^(\d+)([a-zA-Z]+)?')
size = byteSize.search(sizeArg).groups()
maxSize = 0
if size[1].upper() == 'KB':
    maxSize = int(size[0]) * 1024
elif size[1].upper() == 'MB':
    maxSize = int(size[0]) * 1024 * 1024
elif size[1].upper() == 'GB':
    maxSize = int(size[0]) * 1024 * 1024 * 1024
elif size[1].upper() == 'TB':
    maxSize = int(size[0]) * 1024 * 1024 * 1024 * 1024
elif size[1].upper() == 'b' or size[1] == '':
    maxSize = int(size[0])

# human readable filesizes
suffixes = ['B','KiB','MiB','GiB','TiB']
def humanBytes(nbytes):
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])

# walk through directory, prompt user
for root, dirs, files in os.walk(rootDir):
    print('Checking ' + root + '...')
    found = False
    for file in files:
        filePath = os.path.join(root,file)
        if os.path.getsize(filePath) > maxSize:
            found = True
            print('Delete ' + file + ' (' + str(humanBytes(os.path.getsize(filePath))) + ') ?')
            choice = input()
            if str(choice) == 'y':
                print('Moving file to trash...')
                send2trash.send2trash(filePath)
    if not found:
        print('\tno matching files')

