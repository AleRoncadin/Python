class Dog:
    """Classe che descrive i cani"""

    # metodo per inizializzare
    # self è obbligatorio
    def __init__(self, name, age):
        """Inizializza nome ed età"""
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name.title()} is now sitting")

    def roll_over(self):
        print(f"{self.name.title()} rolled over")

# crea istanza
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 10)

# stampa gli attributi
print(f"My dog's name's {my_dog.name.title()}, yours is {your_dog.name.title()}")
print(f"My dog's {my_dog.age} years old, yours is {your_dog.age}")

# chiama i metodi
my_dog.sit()
my_dog.roll_over()