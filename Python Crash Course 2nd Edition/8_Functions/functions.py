def greet_users(username, age):
    """Indica nome ed età dell'utente"""  # il docstring descrive cosa fa la funzione
    print(f"Hello {username.title()}, you are {age} years old")

# argomenti posizionali
greet_users('steve', 20)

# usare keywords
greet_users(age=18, username='harry')

# funzioni con parametri con valore di default
def describe_pet(pet_name, animal_type='dog'):
    """Stampa informazioni sull'animale domestico"""
    print(f"I have a {animal_type.lower()} and its name is {pet_name.lower()}")

# NOTA: i default values vanno messi alla fine

# posso non mettere l'argomento che è già settato di default
describe_pet(pet_name='steve') 

# return e argomento facoltativo
# midlle name è opzionale, quindi lo setto a ''
def get_formatted_name(first_name, last_name, middle_name=''): 
    """Return a full formatted name"""
    if middle_name: # controlla se il parametro è diverso da vuoto
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

formatted_name1 = get_formatted_name('alex', 'savi')
formatted_name2 = get_formatted_name('alex', 'savi', 'paolo')

print(formatted_name1)
print(formatted_name2)

# ritornare un dizionario
def build_person(first_name, last_name, age=None): # age è nullo di default
    person = {'first': first_name.title(), 'last': last_name.title()}
    if age:
        person['age'] = age
    return person

cantante = build_person('jimi', 'hendrix', age=27)
print(cantante)

# esempio di funzione con while
while True:
    print("\nPlease insert your data (enter 'q' to quit): ")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    age = input("Age: ")
    if age == 'q':
        break
    elif age != '':
        age = int(age)
        person = build_person(f_name, l_name, age)
    else:
        person = build_person(f_name, l_name)

    print(person)


# passare liste come argomento
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print(f"Hello, {name.title()}!")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#modificare liste nelle funzioni
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# prevenire che una funzione modifichi una lista
# si invia come argomento una copia della lista: usare [:]
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# ARGOMENTI ARBITRARI:
# se non si sa quanti argomenti può avere una funzione
# uso * prima del nome del parametro
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with these toppings: ")
    for topping in toppings:
        print(f"- {topping.lower()}")

make_pizza('mushrooms', 'green peppers', 'extra cheese')

# puoi mixare gli argomenti posizionali con quelli arbitrari
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with these toppings: ")
    for topping in toppings:
        print(f"- {topping.lower()}")

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# keyword arbitrarie
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                                location='priceton',
                                field='physics')

print(user_profile)
