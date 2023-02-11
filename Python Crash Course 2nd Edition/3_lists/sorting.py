#ordina la lista e la cambia per sempre
cars = ['bmw', 'audi', 'toyota', 'subaru'] # ordine alfabetico
cars.sort()
print(cars)
cars.sort(reverse=True) # alfabetico decrescente
print(cars)

#ordina la lista, ma non la cambia
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"Sorted list: {sorted(cars)}")
print(f"Sorted reverse list: {sorted(cars, reverse=True)}")
print(f"Original list: {cars}")

#cambia l'ordine della lista per sempre, non c'entra niente con ordine alfabetico
print(f"Original list: {cars}")
cars.reverse()
print(f"Reverse list: {cars}")
