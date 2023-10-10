#Lesson 07 - Exercise 02
# Task 01
for i in range(1,101): # i is a variable used to control the increment. Any variable can be used but is has become the standard
    print(i) 
# This method elimates the need for adding to a counter that while uses

# Task 2
for i in range(1, 101):
    if i % 2 == 1:
        print(i)
# OR to print the even numbers
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

# Task 3
names = "" # Initilised the variable as a blank string

while names != "stop": # While loop will run as long as the word stop is not in the variable
    names = input("Please enter a name, enter stop to exit the loop: ")
    print("\nThe name entered is: ", names)

