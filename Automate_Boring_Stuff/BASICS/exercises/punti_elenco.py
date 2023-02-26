#! python3

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

"""
Data una lista nella clipboard, il programma ritorna dei punti elenco per ogni riga.
Esempio:
    Lists of animals
    Lists of aquarium life
    Lists of biologists by author abbreviation
    Lists of cultivars

Diventa:
    * Lists of animals
    * Lists of aquarium life
    * Lists of biologists by author abbreviation
    * Lists of cultivars

NOTA: la lista iniziale quando viene presa da pyperclip
viene letta come 'Lists of animals\nLists of aquarium life\nLists of biologists 
by author abbreviation\nLists of cultivars'
"""

import pyperclip

text = pyperclip.paste()

# TODO: Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list

text = ('\n').join(lines) 
pyperclip.copy(text)
