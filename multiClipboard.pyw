#! python3
# multiClipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to the clipboard.
#        py.exe mcb.pyw list - Loads all keywords to the clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower()== 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

# Command to delete individual keywords
if len(sys.argv) == 3 and sys.argv[1].lower()== 'delete':
    del(mcbShelf[sys.argv[2]])

# TODO: add command to delete all keywords
if len(sys.argv) == 2 and sys.argv[1].lower()== 'clear':
    mcbShelf.clear()

mcbShelf.close()
