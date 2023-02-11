magicians =  ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("------------------------------------------------------")

for value in range(1, 5):
    print(value)                #stampa da 1 a 4, per stampare fino a 5: (range 1, 6)

print("------------------------------------------------------")

for value in range(6):          #stampa da 0 a 5
    print(value)

print("------------------------------------------------------")

numbers = list(range(1, 6))     # crea una lista di numeri da 1 a 5

# se si mette un terzo elemento n, salta n elementi in quel range
even_numbers = list(range(2, 11, 2))    # salta di 2, quindi stampa i numeri pari
print(even_numbers)

print("------------------------------------------------------")

# Esercizio: stampare i quadrati dei numeri da 1 a 10
square_numbers = []
for square in range(1, 11):
    square_numbers.append(square ** 2)

print(square_numbers)

# Questo si può abbreviare in:
squares = [value**2 for value in range(1, 11)]
print(squares)
print("------------------------------------------------------")

# Statistica con le liste (MIN, MAX, SUM)
min(square_numbers)
max(square_numbers)
sum(square_numbers)

# stampare i primi tre elementi di una lista
print(square_numbers[0:3])

# stampare dal primo al quarto elemento
print(square_numbers[1:4])

# stampare fino all'indice 4
print(square_numbers[:4])

# stampare dall'elemento di indice 2 in poi
print(square_numbers[2:])

# stampare gli ultimi 3 elementi
print(square_numbers[-3:])

# puoi usare una parte della lista al posto di tutta all'interno dei for
print("------------------------------------------------------")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(f"\t- {player.title()}")

# copiare le liste
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]    # copia tutti gli elementi della lista sopra qui