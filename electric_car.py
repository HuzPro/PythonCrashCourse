class Car():
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
class Battery():
    """Issa battery madude"""

    def __init__(self, battery_size = 120):
        """Initializing the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Printing a statement telling battery's size."""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def get_range(self):
        """Printing a statement about the range """
        if self.battery_size == 120:
            range = 280
        elif self.battery_size == 145:
            range = 310
        
        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank():
        """Electric cars don't have gas tanks..."""
        print("This car doesn't need a gas tank!")
 
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()