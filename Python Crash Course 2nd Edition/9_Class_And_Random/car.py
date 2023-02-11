class Car:
    """Rappresenta una macchina"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # imposto un valore di default

    def get_descriptive_name(self):
        """Ritorna il nome completo"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Mostra il valore del conta km"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Modificare il valore del conta km"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Incrementa il valore del conta km"""
        if miles < 0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles

def main():
    my_new_car = Car('audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

    my_new_car.odometer_reading = 23    # modifico un valore
    my_new_car.read_odometer()

    my_new_car.update_odometer(24)      # modifico un valore tramite una funzione
    my_new_car.read_odometer()

    my_new_car.increment_odometer(-10)
    my_new_car.read_odometer()

if __name__ == "__main__":
    main()