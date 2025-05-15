class Circle:
    def __init__(self,radious):
        self.radious = radious

    def area(self):
        return (22/7)*self.radious**2
    def perimeter(self):
        return 2*(22/7)*self.radious
circle_1 = Circle(4)
print(f"Area : {circle_1.area()}")
print(f"Perimeter : {circle_1.perimeter()}")

class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    #Dunder Function
    def __gt__(self, other):
        return self.price > other.price
order1 = Order('Chips',20)
order2 = Order('Tea',10)
print(order1>order2)

import random
import string
'''
randnum = random.randint(1,100)
target = randnum
while True:
    userchioce = input("Enter your guess number: ")
    userchioce = int(userchioce)
    if userchioce == target:
        print("Your guess is correct ")
        break
    elif userchioce < target:
        print("You number is too small, take a bigger guess")
    else:
        print("You number is too big, take a smaller guess")

print("-------Game Over--------")
'''

charvalue = string.ascii_letters + string.digits + string.punctuation
password = ""
password_len = 10
#List Comprehensioin
password ="".join([random.choice(charvalue) for i in range(password_len)])
#for i in range(password_len):
#    password += random.choice(charvalue)
#print("You generated random password is: ", password)
print(password)
