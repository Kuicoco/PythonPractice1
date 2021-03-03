
''''
print("Hello, I am Raija Macayan")
x=5
y=7
print(x)
print(y)
print(x+y*x)

print((5+6)*8)
print(5 ** 3)

x=5
y=7
print(x+y)
print(float(x+y))

studentName = input("Please enter your name: ")
print("Welcome", studentName)


fName = input("Please enter your First Name: ")
lName = input("Please enter your Last Name: ")
print("Hello and Welcome", fName, lName)


name = input("Please enter your Name: ")
age = input("How old are you? ")
print("Hi", name, "you are", age, "years old")



Num1 = input("Please enter Num1:")
Num2 = input("Please enter Num2:")

z

x = 10
y = 50
temp = x 
x = y 
y = temp 
  
print("Value of x:", x) 
print("Value of y:", y) 

Num1 = input("Please enter Num1:")
Num2 = input("Please enter Num2:")

temp = Num1
Num1 = Num2
Num2 = temp

print("After swapping Num1 =", Num1,"and Num2 =", Num2)

Num1 = input("Please enter Num1:")
Num2 = input("Please enter Num2:")

Num1, Num2 = Num2, Num1

print("After swapping Num1 =", Num1,"and Num2 =", Num2)

hi =float(input("Enter a number:"))
if hi >= 0:
    print("number is positive")
else:
    print("number is negative")




name = input("Please enter your name: ")
salesVal = int(input("What is your gross sales value? "))

if salesVal >= 5000:
    print("Congratulations %s!" %(name))
    print("You are entitled to $5000 bonus!")

else:
    print("Sorry %s! You are NOT entitled to $5000 bonus" %(name))

num = int(input("Enter a number: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
 
if (num1 > num2) and (num1 > num3):
   largest = num1
elif (num2 > num1) and (num2 > num3):
   largest = num2
else:
   largest = num3
 
print("The largest number is",largest)

age = 21
if age < 12:
    print("You're still a child!" )
elif age < 18:
    print("You're a teenager!" )
elif age < 30:
    print("You're pretty young!" )
elif age <50:
    print("Wisening up, are we?" )
else:
    print("Aren't the years weighing heavy?" )

    

weight = int(input("Enter your weight:"))

if weight > 20:
    print("There is a $25 surcharge for luggage that is too heavy.")
elif weight < 20:
    print("Have a safe flight!")
elif weight == 20:
    print("The weight is just right!")

grade = int(input("Enter your grade:"))

if grade > 75:
    print("You got an A!")
elif grade > 60:
    print("You got a B!")
elif grade > 45:
    print("You got a C!")
elif grade > 40:
    print("You got a D!")
elif grade > 0:
    print("You got a B!")
elif grade < 0:
    sys.exit("Invalid grade")

i = 1
while(i<=100):
    print(i)
    i += 1


groceries = ["Apple", "Bacon", "Chicken"]
for x in groceries:
    print(x)

def Greetings (firstName, lastName):
    print("Greetings ", firstName, " ", lastName)

def Hi (firstName):
    print("Hi", firstName)

Greetings("John", "Smith")
Hi("Python")



def num(i):
    for i in range(i):
        print("x")
num(int(input("Please enter number:")))

def my_function(fname):
  print(fname + " Refsnes")

my_function(input("Please enter first name:"))
'''
def printX(i):
    for i in range(i):
        print("x")
def MultipleX():
    printX(int(input("Please enter an integer number: ")))
MultipleX()

