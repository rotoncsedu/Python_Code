filename = 'pi_digits.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
with open(filename) as file_object:
 #   line1 = file_object.readline() #Read each character of first line
    lines = file_object.readlines() #Read each lines in a complete file
#print(line1)
#print(lines)
pi_string = ''
for line in lines:
    pi_string +=line.strip()
print(pi_string)
print(len(pi_string))

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string +=line.strip()
print(pi_string[:52],'....')
print(len(pi_string))
# birthday = input("Enter your birthday, in DDMMYYYY format: ")
# if birthday in pi_string:
#     print("your birthday appears in first million of pi!")
# else:
#     print("your birthday does not appears in first million of pi!")
filename = 'sample.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
with open(filename) as file_object:
    lines = file_object.readlines()
print(lines)
for line in lines:
    print(line.strip())