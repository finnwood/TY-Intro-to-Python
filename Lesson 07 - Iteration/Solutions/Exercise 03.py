#Lesoson 07 - Exercise 03

#Task 01
total = 0 # Initilises the variable to ensure it is 0 - This is good practice for any variable

for i in range(10): # What would you change to look for more or less numbers
    num = int(input(str(i + 1) + ".Please enter a number: ")) # Can you understand what is happening here
    total += num
print("\nThe average is:", total / 10) # How would you modify this to calculate the correct average depending on how many numbers have been entered

#Task 02
num = int(input("Please enter a number: "))

for i in range(12):
    print(num, "x", i, "=", num * i) # THis print command creates the times tables by adding the different elements together

# Task 03
inNumber = int(input("Please enter a number: "))
total = 0
count = 0

while inNumber != "stop":
    print("Number added was :", inNumber)
    inNumber = input("Please enter another number: ")
    if inNumber.isnumeric():
        inNumber = int(inNumber)
        total += inNumber
        count += 1
# this will only execute after typing "stop"
print("\nThe average for these numbers is:", total / count)

