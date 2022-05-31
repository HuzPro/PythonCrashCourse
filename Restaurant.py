class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """Initializing name and cuisine type of the restaurant"""
        self.resname = restaurant_name
        self.ctype = cuisine_type
    
    def describe_restaurant(self):
        print("\nThe restaurant "+ self.resname.title() + ' is famous for their "' + self.ctype.title() + '" type of cuisines!')

    def open_restaurant(self):
        print("\n"+self.resname.title() + " is now open!")