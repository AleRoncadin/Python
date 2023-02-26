import re

# \d+ and \w+ match text that has one or more \d or \w

xmasRegex = re.compile(r'\d+\s\w+')
xmas = xmasRegex.findall('12, drumers, 11 pipers, 8 maids, 5 rings, 2 doves')
print(xmas)

# the following class [aeiouAEIOU] will match any vowel
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowel = vowelRegex.findall('RoboCop eats BABY FOOD.')
print(vowel)

# this class will match lowercase, uppercase, numbers
allRegex = re.compile(r'[a-zA-Z0-9]')
all = allRegex.findall("My number is +39-088-788-1234")
allString = ''.join(all)
print(allString)


# negative character class with '^'
# insert \s to eliminate spaces
consonantRegex = re.compile(r'[^aieouAEIOU\s]')
consonant = consonantRegex.findall('RoboCop eats BABY FOOD.')
print(consonant)

# if I want the string begins with 'Hello'
beginsWithHello = re.compile(r'^Hello')
hello1 = beginsWithHello.search('Hello, world')
hello2 = beginsWithHello.search('He said hello')        # empty
print(hello1)

# if I want the string ends with a number
endsWithNumber = re.compile(r'\d$')
number1 = endsWithNumber.search("I'm 19")
number2 = endsWithNumber.search("I'm nineteen")        # empty
print(number1)

# r'^\d+$' matches strings that both begin and end with numbers
wholeStringIsNum = re.compile('^\d+$')
wholeNum = wholeStringIsNum.search('1234567890')
wholeNum2 = wholeStringIsNum.search('My number is 1234567890')      # empty
wholeNum3 = wholeStringIsNum.search('   1234567890')                # empty
print(wholeNum)

# using . (dot) for wildcard characters
# dot char means any char except the newline
atRegex = re.compile(r'.at')
at = atRegex.findall('The cat in the hat sat on the flat mat.')
print(at)

# match everything with dot char
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
name = nameRegex.search('First Name: Ale Last Name: Pizza')
first = name.group(1)
last = name.group(2)
print(first + " " + last)


# non-greedy vs greedy modes
string = "<To serve man> for dinner.>"

nongreedyRegex = re.compile(r'<.*?>')
nongreedy = nongreedyRegex.search(string)
print(nongreedy.group())

greedyRegex = re.compile(r'<.*>')
greedy = greedyRegex.search(string)
print(greedy.group())


# dot char can matches newlines with re.DOTALL
newLineRegex = re.compile(r'.*', re.DOTALL)
newLine = newLineRegex.search('Serve the public trust.\nProtect the innocent.')
print(newLine.group())


# case insensitive
robocopRegex = re.compile(r'robocop', re.IGNORECASE)
robocop = robocopRegex.search('RoboCop is a great cop').group()
print(robocop)


# Substituting Strings with the sub() Method
subsRegex = re.compile(r'Agent \w+')
subs = subsRegex.sub('CENSORED', 'Agent Alice gave the secret document to '
                        'Agent Bob')
print(subs)

subsRegex = re.compile(r'Agent (\w)\w*')
subs = subsRegex.sub(r'\1*****', 'Agent Alice gave the secret document to '
                        'Agent Bob')
print(subs)


# using | to combine re.IGNORECASE and re.DOTALL
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
