"""
car = input("What type of Car you want to rant: ")
print(f"Let me see if I can find a {car} for you")
numofpeople = input("How many people in your dinner group sir: ")
numofpeople  = int(numofpeople)
if numofpeople > 8:
    print("Sorry sir! you have to wait for a table")
else:
    print("Congratulation! your table is ready, please take your seat.")

num = input("Please enter a number: ")
num = int(num)
if num % 10 == 0:
    print(f"{num} is multiple of 10")
else:
    print(f"{num} is not multiple of 10")
"""
#While loop
'''
promt = "Enter the item you want to add as topping on your pizza : "
topping = ""
item = ""
while  item != 'quit':
    item = input(promt)
    topping += item
print(topping)
'''
while True:
    ticket_price = 0
    flag = 0
    age = input("Please enter your age : ")
    if age == 'quit':
        break
    age = int(age)
    if age <  0:
        flag = 1
    if flag > 0:
        print(f" You enter an invalid age, please enter correct one.")
        continue
    else:
        if age < 3:
            ticket_price = 0
        elif age <13:
            ticket_price = 10
        else:
            ticket_price = 15
    print(f"Price for your ticket is : {ticket_price}$")