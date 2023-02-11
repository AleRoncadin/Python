# contare da 1 a 5 con un while
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

prompt = """\nPlease enter the name of a city you visited.
Enter 'quit when you have finished: """

# usare break
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"{city.title()} is a beautiful city")

# usare continue per stampare solo i numeri dispari di una lista
# continue ritorna all'inizio del loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# spostare gli elementi di una lista ad un'altra
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:    # finché ci sono elementi nella lista
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following accounts have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"- {confirmed_user.title()}")

# rimuovere elementi dalla lista
pets = ['dog', 'cat', 'rabbit', 'cat', 'goldfish', 'cat']
print(pets)
#pets = sorted(set(pets))   tolgo i duplicati di ogni elemento
#print(pets)
while 'cat' in pets:
   pets.remove('cat')

print(pets)


# usare while nei dizionari
responses = {}
while True:
    name = input("\nWhat is your name? ")
    mountain = input("Which mountain would you like to climb someday? ")

    responses[name] = mountain

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'yes' or repeat.lower() == 'y':
        continue
    break

for name, mountain in responses.items():
    print(f"{name.title()} would like to climb {mountain.title()}")