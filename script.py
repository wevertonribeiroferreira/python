#!/bin/python3

#Variables and Methods
quote = "All is fair in love and war."
print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case

print(len(quote)) #count the caracters


name = "Weverton" #String
age = 30 #int
gpa = 3.7 #float

print(int(age))
print(int(30.1)) #integer does not around

print("My name is " + name + " and I am " + str(age) + " years old.")

age += 1
print (age)

bday = 1
age += bday
print(age)


print('\n')

#Functions
print("Here is an example function:")

def who_am_i(): #this is a function name = "Weverton" age = 35 print("My name is " + name + " and I am " + 
            str(age) + " years old.")
print('\n') who_am_i()

#adding parameters
def add_one_hundred(num):
            print(num + 100)

add_one_hundred(100)
#multiple parameters
def add(x,y):
       print(x + y)

add(7,7)

def multiply(x,y):
        return x * y

print(multiply(7,7))


def square_root(x):
          print(x ** .5)

square_root(64)


def nl():
         print('\n')

nl()

#Boolean expression (true or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))


nl()

#relationa and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = ( 7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #false


nl()
#Conditinal statements
def drink(money):
       if money >= 2:
                       return "You've got yourself a drink!"
       else:
                       return "No drink for you!"
print(drink(3))
print(drink(1))

def alcohol(age,money):
         if (age >=21) and (money >= 5):
                return "We're getting a drink !"
         elif (age >= 21) and (money < 5):
                return "Come back with more money."
         elif (age < 21) and (money >= 5):
                return "Nice try, kid!"
         else:
                return "You're too poor and too young"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,4))


nl()
#lists - Have Brackets  []
movies = ["When Harry Met Sally", "The Hangover", "The Perk of Being a Wallflower", "The Exorcist"]

print(movies[1]) #retun the second item
print(movies[0]) #returns the first item in the list
print(movies[1:4]) # return the 1 until 4 if exists
print(movies[1:]) # return the 1 until the last one
print(movies[:2]) # returns the first 2 items of the list.
print(movies[-1])

print(len(movies))
movies.append("JAWS") #it adds jaws to the end of the list
print(movies)

movies.pop() # delete something from the list jaws
print(movies)

movies.pop(0) #delete the first item on the list
print(movies)

nl()
#Tuples - Do not change, ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

nl()
#Looping

#for loops - start to finish of an iterate
vegetables = ["cucumber", "spinach", "cabbage"]
for x in vegetables:
          print(x)


#While loops - Execute as long as true

i = 1

while i < 10:
       print(i)
       i += 1 






