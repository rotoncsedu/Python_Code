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


