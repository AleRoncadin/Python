# importo la singola classe
from car import Car as c

# per importare più classi da un singolo modulo
#   from electric_car import ElectricCar, Battery

# importare tutte le classi da un modulo:
#   from electric_car import *

# esempio di classe figlia

class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")



class ElectricCar(c):
    """Rappresenta un'auto elettrica"""

    # super() è una funzione che permette di chiamare un metodo dalla classe padre
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery() # crea una istanza di battery nell'attributo

    def describe_battery(self):
        """Descrive la batteria"""
        print(f"This car has a {self.battery_size}-kWh battery")

    # overriding methods from the parent class
    # (metodi del padre che non ci sono nel figlio)
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

def main():
    my_tesla = ElectricCar('tesla', 'model s', 2019)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    my_tesla.battery.get_range()

if __name__ == "__main__":
    main()