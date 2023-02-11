# 6.5
rivers = {
    'nilo': 'egitto',
    'po': 'italia',
    'tigri': 'mesopotamia'
}

for fiume, stato in rivers.items():
    print(f"Il {fiume.title()} si trova in {stato.title()}")

print("I fiumi presenti sono: ")
for fiume in sorted(set(rivers)):
    print(f"- {fiume.title()}")

print("Gli stati presenti sono: ")
for stato in sorted(set(rivers.values())):
    print(f"- {stato.title()}")

# 6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

people = ['jen', 'alberto', 'edward', 'francesco', 'luca']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for responding")
    else:
        print(f"Hi {person.title()}, I'm inviting you to take the poll")