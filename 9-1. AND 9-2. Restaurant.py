"""9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods."""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing name and cuisine type of the restaurant"""
        self.resname = restaurant_name
        self.ctype = cuisine_type
    
    def describe_restaurant(self):
        print("\nThe restaurant "+ self.resname.title() + ' is famous for their "' + self.ctype.title() + '" type of cuisines!')

    def open_restaurant(self):
        print("\n"+self.resname.title() + " is now open!")

Frestaurant = Restaurant("SamShanklands", "Dutch")
Srestaurant = Restaurant("Carlsens", "Sicilians")
Trestaurant = Restaurant("The Giris", "Le Prepie")

Frestaurant.describe_restaurant()
Srestaurant.describe_restaurant()
Trestaurant.describe_restaurant()
Frestaurant.open_restaurant()
Srestaurant.open_restaurant()
Trestaurant.open_restaurant()