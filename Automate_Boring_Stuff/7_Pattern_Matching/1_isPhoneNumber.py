import re

# Indica se la stringa inserita è un numero telefonico USA.
# Ad esempio: 415-555-4242

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False

    return True

text = input("Insert a phone number: ")
B_phone = isPhoneNumber(text)
if B_phone:
    print("Yes, it is a phone number")
else:
    print("No, it is not a phone number")


# trova numeri di telefono dentro una stringa
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print("Phone number found: " + chunk)
print('Done')

# using re method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('Phone number found: ' + mo.group())

# using re method with parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
print('First part: ' + mo.group(1))
print('Second part: ' + mo.group(2))
print('Full number: ' + mo.group())

# print all groups at once
print('Groups: ' + str(mo.groups()))
areaCode, mainNumber = mo.groups()      # assign each value to variables
print(areaCode + "-" + mainNumber)

# escape the parentheses to print them using \( and \)
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))


# use \ for these characters:
# \. \^ \$ \* \+ \? \{ \} \[ \] \\ \| \( \)

print("\n----------------------------------------------------------\n")

# | this char is named pipe and it matches groups
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo1.group())
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile is huge')
print(mo.group())


# optional matching
# in this case (wo)? is optional
batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())


# matching zero or more with *
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventures of Batman')
print(mo.group())

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The adventures of Batwowowowoman')
print(mo.group())

# matching one or more with +
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventures of Batman')
print("Empty string: ")

mo = batRegex.search('The adventures of Batwoman')
print(mo.group())

mo = batRegex.search('The adventures of Batwowowowoman')
print(mo.group())


# repetitions:
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')      #==> empty string

# (Ha) {3,5} ==> can match 3, 4, 5 instances of Ha
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo3 = greedyHaRegex.search('HaHaHaHaHa')
print(mo3.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo4 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo4.group())


# using findall() to find ALL matches
# print a list of elements that matches with the text
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)