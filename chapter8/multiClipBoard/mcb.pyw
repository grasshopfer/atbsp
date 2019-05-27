#! python3

# mcb.pyw - Saves and loads pieces of text to the clipboard.❶ 
# Usage:    py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#           py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#           py.exe mcb.pyw list - Loads all keywords to clipboard.
#           py.exe mcb.pyw delete <keyword> - Removes keyword

import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb')
args = sys.argv
if len(args) == 3:
    if args[1].lower() == 'save':
        mcbShelf[args[2]] = pyperclip.paste()
    elif args[1].lower() == 'delete':
        if args[2] in mcbShelf:
            mcbShelf.pop(args[2])
elif len(args) == 2:
    if args[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif args[1].lower() == 'delete':
        mcbShelf.close()
        os.remove('mcb')
    elif args[1] in mcbShelf:
        pyperclip.copy(mcbShelf[args[1]])

mcbShelf.close()
