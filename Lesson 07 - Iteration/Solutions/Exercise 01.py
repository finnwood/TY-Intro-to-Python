# Lesson 07 - Iteration

# Exercise 01
# Task 01

counter = 1 #Ay time the program is run Initiales the counter ever

while counter <= 10: # Sets the condition that while the variable counter is less than or equal to 10 this statement is true and will run
    print(counter)
    counter += 1 # shorthand for counter = counter + 1 - this adds one to the value stored in counter

# Task 2
# Opposite of Task 1 - Start the counter at 10
counter = 10
while counter > 0: # Checks to see if valye of counter is greater than 0
    print(counter)
    counter -= 1 # Subtracts 1 from the value in counter
# Question: What do you think will happen if you put the print command last?

#Task 3
inputString = input("Please enter a string: ")
counter = 0

while counter < len(inputString):
    if counter % 2 == 1: # % sign looks for the remainder. Even numbers will always have a remainder of 0 when divided by 2 odd will have a remainder of 1
        print(inputString[counter]) # Watch indentation here print is under the if command only
    counter += 1 # Counter is under the while command based on indentation. What would happen if it was indented again to be under the if command.

#Task 4
print("═" * 38) # This trick can be used instead of pressing = 38 times
print("*      Graphical User Interface      *")
print("═" * 38)
print(" 1-   Print numbers from 1 to 10")
print(" 2-   Print numbers from 10 to 1")
print(" 3-   Find even values of a string")
print(" 4-   Exit")
print("═" * 38)
menu_input = int(input("Enter your choice from the menu: ")) # Gets the value for the next stage. What will happen if you use a number greater than 4
while menu_input != 4: # While loop will run while value is not 4 and will skip or exit if = to 4
# The 3 loops below are form Tasks 1 to 3 and can be copied from there
    if menu_input == 1:
        counter = 1
        while counter <= 10:
            print(counter)
            counter += 1
        menu_input = int(input("Enter your choice from the menu: ")) # Location of this is very important
    
    elif menu_input == 2:
        counter = 10
        while counter > 0:
            print(counter)
            counter -= 1
        menu_input = int(input("Enter your choice from the menu: "))
 
    elif menu_input == 3:
        inputString = input("Please enter a string: ")
        counter = 0
        while counter < len(inputString):
            if counter % 2 == 1:
                print(inputString[counter])
            counter += 1
        menu_input = int(input("Enter your choice from the menu: "))
    else:
        menu_input = int(input("Enter your choice from the menu: "))