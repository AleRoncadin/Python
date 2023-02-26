"""Find phone numbers and email address on the clipboard"""

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                  # cerca 3 digit con o senza parentesi
    (\s|-|\.)?                          # cerca uno spazio, un -, o un .
    (\d{3})                             # cerca 3 digit
    (\s|-|\.)                           # cerca uno spazio, un -, o un .
    (\d{4})                             # cerca gli ultimi 4 digit
    (\s*(ext|x|ext.)\s*(\d{2,5}))?      # estensione opzionale
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+                   # username
    @                                   # @ symbol
    [a-zA-Z0-9.-]+                      # domain name
    (\.[a-zA-Z]{2,})                   # dot-something
    )''', re.VERBOSE)

urlRegex = re.compile(r'''(
    (http|https)?
    ://
    [a-zA-Z0-9._%+-]+
    (\.[a-zA-Z]{2,})+
    [a-zA-Z0-9._%+-/?=]*
    )''', re.VERBOSE | re.IGNORECASE)

dateRegex = re.compile(r'''(
    (\d{1,2}|\d{4})
    (/|-)
    (\d{1,2})
    (/|-)
    (\d\d)+
    (\d\d)*
    )''', re.VERBOSE | re.IGNORECASE)

def getMatches():

    text = str(pyperclip.paste())
    matches = ['\nPHONE NUMBERS: ']

    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)

    matches.append('\nEMAIL ADDRESSES: ')
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    matches.append('\nURLS: ')
    for groups in urlRegex.findall(text):
        matches.append(groups[0])

    matches.append('\nDATES: ')
    for groups in dateRegex.findall(text):
        matches.append(groups[0])
    
    return matches

matches = getMatches()

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses or URLS found.')
