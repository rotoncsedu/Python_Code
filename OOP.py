from symtable import Class


class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the restaurant is : {self.restaurant_name} and it is a {self.cuisine_type} restaurant")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")

my_restaurant = Restaurant('Kacci Vai','Indian')
print(f"\n Two attributes are : \n1.{my_restaurant.restaurant_name}\n2.{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant_1 = Restaurant('KFC','Fast Food')
restaurant_2 = Restaurant('Pizza Hut', 'Italian')
restaurant_3 = Restaurant('Xinxian','Chinise')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

class Users:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"\nUser name is : {self.first_name} {self.last_name} and age of this user is : {self.age}")
    def greet_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, you are welcome on our website")
user_1 = Users('Atikur','Rahman',43)
user_2 = Users('Meraj','Ali',36)
user_3 = Users('abdur','rahim',48)
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()

class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_riding = 0
    def descriptive_name(self):
        full_name = f"{self.make} {self.model} {self.year}."
        return  full_name
    def read_odometer(self):
        print(f"This Card has {self.odometer_riding} miles on it.")
    def update_odometer(self,mileage):
        if mileage > self.odometer_riding:
            self.odometer_riding = mileage
        else:
            print("You cannot roll back odometer!")
    def increment_odometer(self,mile):
        self.odometer_riding += mile

class ElectricCar (Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = Battery(200)

class Battery:
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size
    def describe_battery(self):
        print(f"This car has a {self.battery_size} KWH battery.")
    def get_range(self):
        if self.battery_size < 75:
            self.range = 250
        else:
            self.range = 400
        print(f"This Car run {self.range} KM on a full charge")

my_tesla = ElectricCar('Tesla','Model S',2019)
print(my_tesla.descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors
    def get_flavors(self):
        print(f"This Ice Cream has {self.flavors} Flavors.")

my_icecream = IceCreamStand('KFC', 'Fast Food','Venilla')
my_icecream.get_flavors()
