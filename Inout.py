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
import collections

#While loop
'''
promt = "Enter the item you want to add as topping on your pizza : "
topping = ""
item = ""
while  item != 'quit':
    item = input(promt)
    topping += item
print(topping)

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

unconfirmed_user = ['Meraj', 'Milon', 'Rahim']
confirmed_user = []
while unconfirmed_user:
    current_user = unconfirmed_user.pop()
    print(f'Verifying user: {current_user}')
    confirmed_user.append(current_user)

print('\n The following users have been confirmed: ')
for name in confirmed_user:
    print(name)

pets = ['dog','cat', 'dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

responses = {}
polling_choice = True
while polling_choice:
    name = input("What is your name: ")
    response = input("Which mountain would you like to climb oneday: ")

    responses[name] = response

    repeat_choice = input("Would any other like to respond (y/n): ")
    if repeat_choice == 'n':
        polling_choice = False

print("\n ********Poll Result********")
for name, response in responses.items():
    print(f"{name} would like to clim {response}")
'''

#Exercise
sandwich_order = ['tuna','luna','funa']
sandwich_made = []
de = collections.deque(sandwich_order)
while de:
    current_order = de.popleft()
    print(f"I made you {current_order} sandwich")
    sandwich_made.append(current_order)


print("\n ******** Finish Sandwich List ***********")
for sandwich in sandwich_made:
    print(sandwich)

