# per importare più classi da un modulo:
from electric_car import ElectricCar, Battery

# 9.1, 9.2, 9.4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.name = restaurant_name
        self.c_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        """Stampa informazioni"""
        print(f"- Restaurant name: {self.name.title()}")
        print(f"- Cuisine Type: {self.c_type}")

    def open_restaurant(self):
        print(f"Restaurant {self.name.title()} is now open!")

    def read_number_served(self):
        """Indica quanti clienti sono stati serviti"""
        print(f"Number served: {self.number_served}")

    def set_number_served(self, n):
        """Imposta il numero di clienti che sono stati serviti"""
        if n < 0:
            print("Not allowed")
        else:
            self.number_served = n
    
    def increment_number_served(self, n):
        """Incrementa il numero di clienti che sono stati serviti"""
        if n < 0:
            print("Not allowed")
        else:
            self.number_served += n

# 9.3, 9.5
class User:
    def __init__(self, id, first_name, last_name, age, login_attempts=0):
        self.id = id.upper()
        self.first = first_name
        self.last = last_name
        self.age = age
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"\nInformation of user with ID: {self.id}")
        print(f"- First name: {self.first.title()}")
        print(f"- First name: {self.last.title()}")
        print(f"- First name: {self.age}")

    def greet_user(self):
        print(f"Welcome {self.first.title()} {self.last.title()}!")

    def increment_login_attempts(self):
        self.login_attempts +=1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print(f"Login attempts: {self.login_attempts}")

# 9.6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = ['fragola', 'cioccolato', 'vaniglia', 'nocciola']

    def read_flavors(self):
        print("\nFlavors:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


# 9.8
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")

# 9.7
class Admin(User):
    def __init__(self, id, first_name, last_name, age, login_attempts=0):
        super().__init__(id, first_name, last_name, age, login_attempts)
        self.privileges = Privileges()


def main():
    # prove con la classe ristorante
    restaurant = Restaurant('Adriatico', 'italiana')
    print(restaurant.name.title())
    print(restaurant.c_type)
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
    restaurant.set_number_served(15)
    restaurant.read_number_served()
    restaurant.increment_number_served(40)
    restaurant.read_number_served()


    # prove con la classe user
    user = User('a1s39dk', 'alessandro', 'rossi', 38)
    user.describe_user()
    user.greet_user()
    user.read_login_attempts()
    user.increment_login_attempts()
    user.read_login_attempts()
    user.reset_login_attempts()
    user.read_login_attempts()

    # prove con la classe ice cream flavor
    iceCream = IceCreamStand('Al Naturale', 'gelati')
    iceCream.read_flavors()

    # prove con la classe admin
    admininistrator = Admin('9293idk', 'giuseppe', 'orsi', 49)
    admininistrator.privileges.show_privileges()

if __name__ == "__main__":
    main()