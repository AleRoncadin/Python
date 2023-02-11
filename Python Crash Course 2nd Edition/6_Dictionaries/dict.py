alien_0 = {
    'color': 'green',
    'points': 5
}

print(alien_0['color'])
print(alien_0['points'])

points = alien_0['points']
print(f"You earned {points} points")

# aggiungere dei valori
alien_0['x_position'] = 0
alien_0['x_position'] = 25

#puoi inizializzare anche dizionari vuoti:
alien_1 = {}

print("------------------------------------------------------")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# modificare il valore di un attributo
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print("------------------------------------------------------")

# rimuovere attributi dal dizionario
del alien_0['speed']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}")

print("------------------------------------------------------")

# get function: se non trova il valore stampa la stringa scritta dal programmatore
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)    #stampa 'no point value assigned'

# in questo caso trova 'points' quindi stampa 2
alien_0 = {'color': 'green', 'speed': 'slow', 'points': 2}
point_value = alien_0.get('points', 'No point value assigned.')

print(point_value)    #stampa 2

print("------------------------------------------------------")

# for nei dizionari
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

for name in favorite_languages.keys():      # se non devo usare i valori
    print(name.title())

# puoi anche omettere il metodo .keys()
for name in favorite_languages:
    print(name.title())

# esempio:
friends = ['phil', 'sara']

for name in favorite_languages.keys():
    if name in friends:
        language = favorite_languages[name].title()
        print(f"Hi {name.title()}, your fav language is {language.title()}")

# fare un loop su una lista ordinata: usare sorted
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

# mostrare solo i valori senza le keys(): usare .values()
# per non ripetere i valori (per non farli apparire più di una volta) uso .set()
print("The following languages have been mentioned: ")
for language in sorted(set(favorite_languages.values())):
    print(f"- {language.title()}")


# guardare esercizio 6.6

print("------------------------------------------------------")

