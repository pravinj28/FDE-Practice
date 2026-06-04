#print("My name is Pravin")
#print("O----")
#print("||||")
#print("*" *10) 

#price = 10
#price = 20 #Integer
#rating = 4.9 #Float
#is_published = True #Boolean, Python is case sensitive which means it's 
                    #sensitive to lower case and upper case letters. so when defining variables
                    # we should always use lowercase letters, but here false and true are special keywords 
                    #in the language it will not recognise if we spell it small. 
#print(price) 


#Name = "John Smith"
#Age = 20
#is_new = True 

#Name = input("What is your name? ")
#print("Your name is:",Name)
#print("Your name is" + Name) #Using + does not give you space between

#name = input("What is your name? ")
#color = input("What is your favourite color ")
#print(Name , "Likes" , color)

#birth_year = input("Enter year: ")
#age = 2026 - int(birth_year)
#print(age)

#weight = input("Enter your weight in Pounds: ")
#kg = float(weight) * 0.45
#print(kg)

Course = "Python's Course for Begineers "
print(Course[9]) #This is called indexing 
print(Course[-2])
print(Course[0:3]) #This returns the range from 0 to 2 index 
print(Course[0:]) #This will print complete string 
print(Course[1:]) #This will exclude 0th index letter and will print complete string 
print(Course[:5]) #If we add an end index like 5 here, python interpretor will assume 0 to start index 
print(Course[:]) #Can copy or clone complete string 

print(Course[1:-1])


#FORMATED STRINGS

first = 'John'
last = 'smith'

#message = first + '['+ last + '] is a coder' #Not ideal harder to visualise the output
#print(message)

message2 = f"{first} [{last}] is a coder"
print(message2)

course = 'python for begineers'
print(len(course))

print(course.upper()) #This will print the string in uppercase.

print(course.find('p')) 

print(course.replace('begineers', 'absolute begineers'))

print('python' in course) #This is boolean 

import math
print(math.pi)

#IF AND ELSE STATEMENTS

is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")

elif is_cold:
    print("It's a cold day, wear warm clothes")
    print("Enjoy your day")

else:
    print("It's a lovely day")


has_good_credit = False
price = 10000

if has_good_credit:
    print("If you have a good credit")
    print("Pay", 0.1 * price)
else:
    print("If you have a bad credit")
    print("Pay", 0.2 * price)

    
#if applicant has high income AND good credit then he is eligible for LOAN. Use AND Logical operator 

has_high_income = True 
has_good_credit = False

if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Not eligible for loan")


temp = int(input("Temperature today: "))

if temp > 30:
    print("It's a hot day today")
elif temp < 10:
    print("It's a cold day")
else:
    print("It's neither hot not cold")


name = len(input("Enter you name: "))

if name < 3:
    print("Name must be at least 3 characters")
elif name >50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")


#WEIGHT CONVERTER PROGRAM 

i = 1

while i <= 5:
    print(i)
    i = i + 1 
print("Done")

i = 1
while i <= 5:
    print('x' * i )
    i = i + 1
print(i)

#FOR LOOPS 

for i in range (1, 20):
    print(i)

for item in "Python":
    print(item)

for item in ["PRAVIN","SONU","MAYUR"]:
    print(item)

for x in range(4):
    for y in range(3):
        print(f"({x},{y})") #Use to print the coordinates




