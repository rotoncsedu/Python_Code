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