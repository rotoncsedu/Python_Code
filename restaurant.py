class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the restaurant is : {self.restaurant_name} and it is a {self.cuisine_type} restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")
