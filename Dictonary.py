name = 'Imran'
age = 35
print("My name is", name, "and I am",age ,"years old")
print(f"My name is {name} and I am {age} years old.")
print(f"My name is {name} and I am {age} years old.",end='****')
print(name,age)
print(name,age,sep="-")

#Intialize Dictionary
alien_0 = {'color':'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
color = alien_0['color']
points= alien_0['points']
print(f"Alien you are {color} in Color and You have {points} Points.")
alien_0['x_position'] = 0
alien_0['y_position'] = 30
alien_0['speed'] = 'medium'
print(alien_0)
print(f"You Initial X position is {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increase = 2
elif alien_0['speed'] == 'medium':
    x_increase = 4
else:
    x_increase = 6

alien_0['x_position'] = alien_0['x_position'] + x_increase
print(f"You Updated X position is {alien_0['x_position']}")

del alien_0['speed']
print(alien_0)
#speed = alien_0['speed', "Looking Key doesn't exist"]
speed = alien_0.get('speed', "Looking Key doesn't exist")
print(speed)

#Practice of Exercise
person = {'f_name' : 'Meraj', 'l_name' : 'Ali', 'age' : 36, 'city' : 'Saidpur'}
print(person)
fav_num = {
    'Meraj' : 20,
    'Belal' : 30,
    'Shamim' : 40,
    'Arif' : 50,
    'Sojib' : 30,
}
print(fav_num)
for i in fav_num:
    print(f"{i} you favourite number is : {fav_num[i]}")


for key, value in fav_num.items():
    print(f"{key} you favourite number is {value}")

for name in fav_num.keys():
    print(f"Hi {name}")
    if fav_num[name] == 30:
        print("You like the number", fav_num[name])

for name in sorted(fav_num.keys()):
    print(f"{name.title()},thank you for tell your favourite number and it is : {fav_num[name]}")

for number in set(fav_num.values()):
    print(number)

poll_member = ['Meraj', 'Milon', 'Rahim', 'Belal', 'Saiful']
for poll_mem in poll_member:
    if poll_mem in fav_num.keys():
        print(f"{poll_mem.title()}, thank you for participating to this poll")
    else:
        print(f"{poll_mem.title()}, hurry up and participate to this poll")


#Nesting
person_0 = {'f_name': 'Belal', 'l_name' : 'Hosen', 'age': 39, 'city' : 'Rajshahi'}
person_1 = {'f_name': 'Saiful', 'l_name' : 'Islam', 'age': 32, 'city' : 'Nilphamari'}

people = [person,person_0, person_1]
for person in people:
    print(person)

fav_place = {
    'Zayed' : ['Rangpur', 'Rajshahi', 'Syhlet'],
    'Milon' : ['Cox\'s Bazzar' ],
    'Mondol' : ['Bandorban', 'Khulna']
}
for name in fav_place.keys():
    print(len(fav_place[name]))
    if len(fav_place[name]) > 1:
        print(f"Mr {name} you favourite places are : ")
    else:
        print(f"Mr {name} you favourite places is : ")
    for place in fav_place[name]:
        print(place)


cities = {
    'Dhaka' : {
        'country' : 'Bangladesh',
        'poulation' : '180M',
        'fact' : 'Capital of Bangladesh'
    },
    'Chottogram' : {
        'country' : 'Bangladesh',
        'poulation' : '180M',
        'fact' : 'City of commerce in Bangladesh'
    },
    'Delhi' : {
        'country' : 'India',
        'poulation' : '1.4B',
        'fact' : 'Capital of India'
    },
}

for city,info in cities.items():
    print(f"Information about {city} as below:")
    for key,value in info.items():
        print(f"{key} : {value}")





