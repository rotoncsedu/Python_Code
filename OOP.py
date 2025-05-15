from symtable import Class
from urllib.response import addinfourl


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

class Privilege:
    def __init__(self,privilege = 'Null'):
        self.privileges = privilege
    def show_privilage(self):
        print("This user has following privillages: ")
        for privilege in self.privileges:
            print(privilege)
class Admin(Users,Privilege):
    def __init__(self,f_name,l_name,age,privilage):
        super().__init__(f_name,l_name,age)
        self.privileges = Privilege(privilage)
admin_pre = ['Can add post', 'Can delete post', 'Can ban user']
admin_user = Admin('Meraj','Ali',33,admin_pre)
admin_user.describe_user()
admin_user.privileges.show_privilage()

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for i in self.marks:
            sum += i
        return sum/3

student_1 = Student('Meraj',[78,89,86])
avg = student_1.get_average()
print(f"{student_1.name} your average marks is : {avg}")

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  #Private Attribute
    def get_account_details(self):
        print(f"Account Number : {self.acc_no}")
        self.__get_acc_pass()
    def __get_acc_pass(self):  #Private Method
        print(f"Password of this account is : {self.__acc_pass}")

account = Account('123456','asdf@123')
account.get_account_details()

class Employee:
    org_name = "Begum Rokeya Universiy"
    name = "Anonymous"
    def __init__(self,name,age):
        self.name = name  #obj.attribute > class.attribute
        self.age = age
       # self.__class__.org_name = "XYZ"

    @staticmethod
    def greeting():
        print("\nWelcome to ",Employee.org_name) #self.__class.org_name
    @classmethod
    def change_org_name(cls,name): #Class method to change class attributes
        cls.org_name = name
'''
Employee.greeting()
e1 = Employee('meraj','Network Engineer','55000')
str1 = f"Employee Name: {e1.name.title()}\nOrganization Name: {e1.org_name}\nDesignation: {e1.designation}\nSalary: {e1.salary}"
print(str1)
e2 = Employee('Belal hosen','Network Engineer','65000')
str2 = f"Employee Name: {Employee.name.title()}\nOrganization Name: {e2.org_name}\nDesignation: {e2.designation}\nSalary: {e2.salary}"
print(str2)
e3 = Employee('sayla','Store Officer','30000')
e3.change_org_name('BRUR')
str3 = f"Employee Name: {e3.name.title()}\nOrganization Name: {Employee.org_name}\nDesignation: {e3.designation}\nSalary: {e3.salary}"
print(str3)
del e2
#print(e2.salary) #get error
'''
#Property Decorator

class AverageMarks:
    def __init__(self,phy,che,math):
        self.phy = phy
        self.chem = che
        self.math = math
      #  self.average = (self.phy + self.chem + self.math) /3
    @property
    def average(self): #Property decorator make this method as a class attribute
        return (self.phy + self.chem + self.math) /3


s1 = AverageMarks(78,65,72)
print(s1.average)
s1.chem = 80
print(s1.average)

# Dunder Function
# To make own operator
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def show_number(self):
        print(self.real,"i + ",self.img,"j")

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        newNum = Complex(newReal,newImg)
        return newNum
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        newNum = Complex(newReal,newImg)
        return newNum

num1 = Complex(3,5)
num1.show_number()
num2 = Complex(2,4)
num2.show_number()
#newnum = num1 + num2 #Error, unsupported operand
#newnum = num1.add(num2)
#newnum.show_number()
newnum = num1 + num2
newnum.show_number()
newnum = num1 - num2
newnum.show_number()

class Engineer(Employee):
    def __init__(self,name,age,designation,salary):
        super().__init__(name,age)
        self.designation = designation
        self.salary = salary

    def show_details(self):
        super().greeting()
        print(f"Employee name: {self.name}")
        print(f"Employer Organization: {self.__class__.org_name}")
        print(f"Designation: {self.designation}")
        print(f"Employee age: {self.age}")
        print(f"Employee Salary: {self.salary}")

engg1 = Engineer('Meraj Ali','33','Network Engineer', 55000)
engg1.show_details()
engg1.change_org_name('BRUR')
engg2= Engineer('BelalHosen',39,'Network Engineer',60000)
engg2.show_details()
