bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

print(bicycles[-1]) #ritorna l'ultimo elemento nella lista
print(bicycles[-2]) #ritorna il penultimo elemento nella lista
print(bicycles[-3]) #ritorna il terzultimo elemento nella lista

print(f"My first bicycle was {bicycles[-1].upper()}")

# changing values
bicycles[-1] = 'TRX'
print(bicycles)

# appending elements
bicycles.append('specialized')
print(bicycles)

# inserting elements
bicycles.insert(0, 'hoppo')
print(bicycles)

# removing elements
del bicycles[2]

# pop: rimuove l'elemento dalla lista per poi salvarlo in un altra variabile
popped_bicycles = bicycles.pop() #rimuove l'ultimo elemento se non specifichi
print(f'Last bicycle was {popped_bicycles}')
first_bicycles = bicycles.pop(0)
print(f'First bicycle was {first_bicycles}')

# remove item by its value
bicycles.remove('redline')

# lunghezza della lista
len = len(bicycles)
print(f"Length of the list: {len}")