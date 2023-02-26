import random

# Per scorrere gli indici di una lista puoi:
# usare range(len(someList)) con un ciclo for
# usare enumerate() con un ciclo for

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
supplies.insert(0, 'SUPPLIES: ')
print(supplies)

for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# assegnamento multiplo
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat
# si poteva anche scrivere come:
size = cat[0]
color = cat[1]
disposition = cat[2]

# random.choice(): sceglie un elemento a caso dalla lista
print(random.choice(supplies))

# random.shuffle(): riordina a caso gli elementi

shuffled = random.shuffle(cat)
print(shuffled)


# list replication
bacon = ['Zophie']
bacon *= 3              # diventa ['Zophie', 'Zophie', 'Zophie']
bacon += ['Zophie']     # diventa ['Zophie', 'Zophie', 'Zophie', 'Zophie']
print(bacon)

# reverse values of a list
reversed = cat.reverse()
print(reversed)


# convertire in lista o tupla
tupla = tuple(['cat', 'dog', 5])
print(tupla)
lista = list(('cat', 'dog', 5))
print(lista)
hello = list('hello')
print(hello)

