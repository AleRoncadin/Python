cars = ['audi', 'bmw', 'subaru', 'toyota']
car = 'Audi'
car2 = 'BMW'

print(car == 'subaru') # stampa falso perché car == 'Audi'

# car == 'AUDI' è case sensitive ritorna false
if car == 'AUDI':
    print(True)
else:
    print(False)

# così invece ritorna true
if car.upper() == 'AUDI':
    print(True)
else:
    print(False)

print("------------------------------------------------------")

# and e or
if (car == 'Audi') and (car2 == 'BMW'):
    print(True)

if (car == 'audi') or (car2 == 'BMW'):
    print(True)

print("------------------------------------------------------")

# verifica se un elemento è nella lista
if 'subaru' in cars:
    print(True)

# verifica se un elemento non è nella lista
if 'ferrari' not in cars:
    print(True)

print("------------------------------------------------------")

#  if - elif - else
age = 14
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")

print("------------------------------------------------------")

# ATTENZIONE:
#   Questo codice è diverso da:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# questo:
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

# nel secondo pezzo esce e quindi si avrebbe un risultato incompleto

print("------------------------------------------------------")

# controllare se una lista è vuota
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}")
    print("\nFinished making your pizza")
else:
    print("Are you sure you want a plain pizza?")

print("------------------------------------------------------")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni'
                        'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}")

print("\nFinished making your pizza!")

