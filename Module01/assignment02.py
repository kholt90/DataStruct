
from random import randint

# Biggie Size
# Given an array, write a function that changes all positive numbers in the array to "big".
# Example: makeItBig([-1, 3, 5, -5]) returns that same array, changed to [-1, "big", "big", -5].

def MakeItBig(the_list):
    for i, el in enumerate(the_list):
        if 0 < el:
            the_list[i] = "big"
    return the_list

# Count Positives
# Given an array of numbers, create a function to replace last value with number of positive values.
# Example, countPositives([-1,1,1,1]) changes array to [-1,1,1,3] and returns it.
# (Note that zero is not considered to be a positive number).

def CountPositives(the_list):
    count = 0
    for i in the_list:
        if 0 < i:
            count += 1
    the_list[-1] = count
    return the_list

# SumTotal
# Create a function that takes an array as an argument and returns the sum of all the values in the array.
# For example sumTotal([1,2,3,4]) should return 10

def SumTotal(the_list):
    return sum(the_list)

# Average
# Create a function that takes an array as an argument and returns the average of all the values in the array.
# For example multiples([1,2,3,4]) should return 2.5

def Average(the_list):
    return None if len(the_list) == 0 else SumTotal(the_list) / len(the_list)

# Length
# Create a function that takes an array as an argument and returns the length of the array.
# For example length([1,2,3,4]) should return 4

def Length(the_list):
    return len(the_list)

# Minimum
# Create a function that takes an array as an argument and returns the minimum value in the array.
# If the passed array is empty, have the function return false.
# For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.

def Minimum(the_list):
    return False if len(the_list) < 1 else min(the_list)

# Maximum
# Create a function that takes an array as an argument and returns the maximum value in the array.
# If the passed array is empty, have the function return false.
# For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -1.

def Maximum(the_list):
    return False if len(the_list) < 1 else max(the_list)

# UltimateAnalyze
# Create a function that takes an array as an argument and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.

def UltimateAnalyze(the_list):
    analysis = {}
    analysis["sum_total"] = SumTotal(the_list)
    analysis["average"] = Average(the_list)
    analysis["minimum"] = Minimum(the_list)
    analysis["maximum"] = Maximum(the_list)
    analysis["length"] = Length(the_list)
    return analysis

# ReverseList
# Create a function that takes an array as an argument and return an array in a reversed order.
# Do this without creating an empty temporary array.
# For example reverse([1,2,3,4]) should return [4,3,2,1]. 

def Reverse(the_list):
    for i in range(len(the_list) // 2):
        the_list[i], the_list[-(i + 1)] = the_list[-(i + 1)], the_list[i]
    return the_list

print("-----===== Start =====-----\n")

print("\n-----===== BiggieSize =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(-10,10))

print(f"My List: {my_list}")
print(f"Result: {MakeItBig(my_list)}")

print("\n-----===== Count Positives =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(-10,10))

print(f"My List: {my_list}")
print(f"Result: {CountPositives(my_list)}")

print("\n-----===== SumTotal =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Total: {SumTotal(my_list)}")

print("\n-----===== Average =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Average: {Average(my_list)}")

print("\n-----===== Length =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Length: {Length(my_list)}")

print("\n-----===== Minimum =====-----\n")

my_list = []
for i in range(randint(0,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Minimum: {Minimum(my_list)}")

print("\n-----===== Maximum =====-----\n")

my_list = []
for i in range(randint(0,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Maximum: {Maximum(my_list)}")

print("\n-----===== Ultimate Analysis =====-----\n")

my_list = []
for i in range(randint(0,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Analysis: {UltimateAnalyze(my_list)}")

print("\n-----===== Reverse List =====-----\n")

my_list = []
for i in range(randint(0,10)):
    my_list.append(randint(1,10))

print(f"My List: {my_list}")
print(f"Reversed List: {Reverse(my_list)}")

print("\n-----===== End =====-----")
