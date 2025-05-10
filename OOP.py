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
