#! python3
# mclip.py - A multi-clipboard program.

"""
L'obiettivo del programma è che quando premi Win+R e scrivi 'mclip ...'
il programma prende il secondo argomento della stringa scritta con sys.arg[1], 
che è una keyphrase del dizionario TEXT, e poi inserisce nella clipboard 
del computer il valore contenuto nella rispettiva keyphrase.
Se scrivo mclip agree, mi copia negli appunti 'Yes, I agree...' e posso
incollare la frase nel blocco note o dove voglio
"""

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1] # first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)