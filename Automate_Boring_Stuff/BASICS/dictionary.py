import pprint

# imposta un nuovo attributo 'color' impostato a 'black'
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')

# pretty printing
pprint.pprint(spam)


message = 'It was a bright cold day in April, and the clocks' \
            ' were striking thirteen.'

print(message)
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)