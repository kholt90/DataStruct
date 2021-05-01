
from random import randint

# In order to win the prize for most cookies sold, my friend John and I are going to merge our Scout Cookies orders and enter as one unit.
# Each order is represented by an "order id" (an integer).
# We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.
# For example:
# my_list = [3, 4, 6, 10, 11, 15]
# john_list = [1, 5, 8, 12, 14, 19]

# # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
# print merge_lists(my_list, john_list)

print("\n-----===== Start =====-----\n")

def MergeLists(my_list, john_list):
    merged_list = []
    index = 0
    for i in my_list:
        while index < len(john_list) and john_list[index] < i:
            merged_list.append(john_list[index])
            index += 1
        merged_list.append(i)
    while index < len(john_list):
        merged_list.append(john_list[index])
        index += 1
    return merged_list

my_list = []
john_list = []

for i in range(randint(1,10)):
    my_list.append(randint(1,10))
my_list.sort()

for i in range(randint(1,10)):
    john_list.append(randint(1,10))
john_list.sort()

print(f"My List: {my_list}")
print(f"John's List: {john_list}")
print(f"Merged List: {MergeLists(my_list, john_list)}")

print("\n-----===== End =====-----")