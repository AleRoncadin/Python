import pyinputplus as pyip

response = pyip.inputNum('Enter a number: ')

# min, max, greaterThan, lessThan
if input('min, max? ') == 's':
    response = pyip.inputNum('>  ', min=4)                  # x >= 4
    response = pyip.inputNum('> : ', max=4)                 # x <= 4
    response = pyip.inputNum('> : ', greaterThan=4)         # x > 4
    response = pyip.inputNum('> ', min=4, lessThan=6)       # 4 <= x < 6

# blank keyword: the user doesn't need to enter anything
response = pyip.inputNum("Blank: ", blank=True)

# limit, timeout: use a default argument to avoid exceptions
response = pyip.inputNum("Limit: ", limit=2, default='N/A') # hai 2 tentativi       
response = pyip.inputNum("Timeout: ", timeout=10, default='N/A') # hai 10 secondi      


# allowRegexes, blockRegexes
response = pyip.inputNum("Enter a number (allow): ", 
                        allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
response = pyip.inputNum("Enter a number (allow): ",
                        allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])

response = pyip.inputNum("Enter a number (block): ", blockRegexes=[r'[02468]$'])

# both arguments
response = pyip.inputStr(allowRegexes=[r'caterpillar', r'category'], 
                            blockRegexes=[r'cat'])
