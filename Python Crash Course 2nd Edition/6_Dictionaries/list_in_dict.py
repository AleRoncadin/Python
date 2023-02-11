pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

print(f"You ordered a {pizza['crust']}-crust pizza "
        "with the following topics:")
    
for topping in pizza['toppings']:
    print(f"- {topping}")

# ESERCIZIO IMPORTANTE

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {languages[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in sorted(set(languages)):
            print(f"- {language.title()}")
