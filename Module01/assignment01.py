
from random import randint

# Countdown
# Create a function that accepts a number as an input.
# Return a new list that counts down by one, from the number (as lists 'zero'th element) down to 0 (as the last element).
# For example countDown(5) should return [5,4,3,2,1,0].

def Countdown(the_number):
    the_list = []
    for i in range(the_number + 1):
        the_list.append(the_number - i)
    return the_list

# Print and Return
# Your function will receive a list with two numbers.
# Print the first value, and return the second.

def PrintReturn(to_print, to_return):
    print(to_print)
    return to_return

# First Plus Length
# Given a list, return the sum of the first value in the list, plus the list's length.

def FirstLength(the_list):
    return the_list[0] + len(the_list)

# Values Greater than Second
# Write a function that accepts a list, and returns a new list with the list values that are greater than its 2nd value.
# Print how many values this is.
# If the list is only one element long, have the function return False

def GreaterSecond(the_list):
    new_list = False
    if 1 < len(the_list):
        new_list = []
        for i in the_list:
            if the_list[1] < i:
                new_list.append(i)
    return new_list

# This Length, That Value
# Write a function called lengthAndValue which accepts two parameters, size, and value.
# This function should take two numbers and return a list of length size containing only the number in value.
# For example, lengthAndValue(4,7) should return [7,7,7,7].

def LengthAndValue(size, value):
    new_list = []
    for i in range(size):
        new_list.append(value)
    return new_list

print("-----===== Start =====-----\n")

print("\n-----===== Countdown =====-----\n")

print(f"Countdown from 10: {Countdown(10)}")

target = randint(11,20)

print(f"Countdown from {target}: {Countdown(target)}")

print("\n-----===== Print and Return =====-----\n")

x = randint(1,5)
y = randint(6,10)

print(f"To Print: {x}")
print(f"To Return: {y}\n")
print(f"Returned Value: {PrintReturn(x,y)}")

print("\n-----===== First Plus Length =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"List Length: {len(my_list)}")
print(f"Result: {FirstLength(my_list)}")

print("\n-----===== Values Greater Than Second =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Results: {GreaterSecond(my_list)}")

print("\n-----===== This Length, That Value =====-----\n")

x = randint(1,10)
y = randint(1,10)

print(f"Size: {x}")
print(f"Value: {y}")
print(f"Result: {LengthAndValue(x,y)}")

print("\n-----===== End =====-----")
