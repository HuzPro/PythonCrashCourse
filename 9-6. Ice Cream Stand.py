"""9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand 
that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). 
Either version of the class will work; just pick the one you like better. Add an attribute called 
flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method."""


import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, flavors, restaurant_name, cuisine_type):
        def super().__init__(restaurant_name, cuisine_type)

        self.flavors = flavors


    def display_flavors(self):
        print("Available flavors are: "  )
