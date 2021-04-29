import random
import math

d = "being"

print(f"-----===== Start =====-----\n")

# Problem 1.
# A crack team of love scientists from JeUp (a hot new dating site) have devised a way to represent dating profiles as rectangles on a two-dimensional plane.
# They need help writing an algorithm to find the intersection of two users' love rectangles.
# They suspect finding that intersection is the key to a matching algorithm so powerful it will cause an immediate acquisition by Google or Facebook or Obama or something.
# Write a function to find the rectangular intersection of two given love rectangles.
# As with the example above, love rectangles are always "straight" and never "diagonal."
# More rigorously: each side is parallel with either the x-axis or the y-axis.
# They are defined as dictionaries like this:

print(f"\n-----===== Problem 1 =====-----\n")

def LoveIntersect(rect_a, rect_b):
    love = None

    if (
        (rect_a['left_x'] < (rect_b['left_x'] + rect_b['width']))
        and (rect_a['bottom_y'] < (rect_b['bottom_y'] + rect_b['height']))
        and (rect_b['left_x'] < (rect_a['left_x'] + rect_a['width']))
        and (rect_b['bottom_y'] < (rect_a['bottom_y'] + rect_a['height']))
    ):
        love = {
            # Coordinates of bottom-left corner
            'left_x'   : None,
            'bottom_y' : None,
            # Width and height
            'width'    : None,
            'height'   : None
        }
        love['left_x'] = max(rect_a['left_x'], rect_b['left_x'])
        love['bottom_y'] = max(rect_a['bottom_y'], rect_b['bottom_y'])

        if rect_a['left_x'] < rect_b['left_x']:
            love["width"] = (rect_a['left_x'] + rect_a["width"]) - love['left_x']
            if (rect_b['left_x'] + rect_b["width"]) < (rect_a['left_x'] + rect_a["width"]):
                love["width"] = love["width"] - ((rect_a['left_x'] + rect_a["width"]) - (rect_b['left_x'] + rect_b["width"]))
        elif rect_b['left_x'] < rect_a['left_x']:
            love["width"] = (rect_b['left_x'] + rect_b["width"]) - love['left_x']
            if (rect_a['left_x'] + rect_a["width"]) < (rect_b['left_x'] + rect_b["width"]):
                love["width"] = love["width"] - ((rect_b['left_x'] + rect_b["width"]) - (rect_a['left_x'] + rect_a["width"]))

        if rect_a['bottom_y'] < rect_b['bottom_y']:
            love["height"] = (rect_a['bottom_y'] + rect_a["height"]) - love['bottom_y']
            if (rect_b['bottom_y'] + rect_b["height"]) < (rect_a['bottom_y'] + rect_a["height"]):
                love["height"] = love["height"] - ((rect_a['bottom_y'] + rect_a["height"]) - (rect_b['bottom_y'] + rect_b["height"]))
        elif rect_b['bottom_y'] < rect_a['bottom_y']:
            love["height"] = (rect_b['bottom_y'] + rect_b["height"]) - love['bottom_y']
            if (rect_a['bottom_y'] + rect_a["height"]) < (rect_b['bottom_y'] + rect_b["height"]):
                love["height"] = love["height"] - ((rect_b['bottom_y'] + rect_b["height"]) - (rect_a['bottom_y'] + rect_a["height"]))

    return love

my_rectangle = {
    # Coordinates of bottom-left corner
    'left_x': random.randint(1,5),
    'bottom_y': random.randint(1,5),
    # Width and height
    'width': random.randint(5,10),
    'height': random.randint(5,10)
}

your_rectangle = {
    # Coordinates of bottom-left corner
    'left_x': random.randint(1,5),
    'bottom_y': random.randint(1,5),
    # Width and height
    'width': random.randint(5,10),
    'height': random.randint(5,10)
}

b = "feel"
print(f"Me: {my_rectangle}")
print(f"You: {your_rectangle}")
print(f"Potential: {LoveIntersect(my_rectangle, your_rectangle)}")

# Your output rectangle should use this format as well.

# Problem 2.
# Given a list of integers, find the highest product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.

print(f"\n-----===== Problem 2 =====-----\n")

def highest_product_of_three(integer_list):
    integer_list.sort()
    product_1 = integer_list[-2] * integer_list[-3]
    product_2 = integer_list[0] * integer_list[1]
    if product_1 > product_2:
        return product_1 * integer_list[-1]
    else:
        return product_2 * integer_list[-1]

my_integer_list = []
integer_list_length = random.randint(3,10)
for i in range(integer_list_length):
    my_integer_list.append(random.randint(1,5))

print(f"Integer List: {my_integer_list}")
print(f"Highest Product: {highest_product_of_three(my_integer_list)}")

c = "you're"

# Problem 3.
# You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.
# Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.
# For example, given:
#   [1, 7, 3, 4]
# your function would return:
#   [84, 12, 28, 21]
# by calculating:
#   [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]
# Here's the catch: You can't use division in your solution!

print(f"\n-----===== Problem 3 =====-----\n")

def get_products_of_all_ints_except_at_index(integer_list):
    list_of_products = []
    if len(integer_list) > 1:
        for i in range(len(integer_list)):
            product = math.prod(integer_list[:i] + integer_list[i+1:])
            list_of_products.append(product)
    else:
        list_of_products = None
    return list_of_products

my_integer_list = []
integer_list_length = random.randint(1,10)
for i in range(integer_list_length):
    my_integer_list.append(random.randint(1,5))

f = "ched"

print(f"Integer List: {my_integer_list}")
print(f"Products: {get_products_of_all_ints_except_at_index(my_integer_list)}")

# Problem 4.
# You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.
# Write a class TempTracker with these methods:
# insert()—records a new temperature
# get_max()—returns the highest temp we've seen so far
# get_min()—returns the lowest temp we've seen so far
# get_mean()—returns the mean  of all temps we've seen so far
# get_mode()—returns a mode  of all temps we've seen so far
# Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.
# get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..110.
# If there is more than one mode, return any of the modes.

print(f"\n-----===== Problem 4 =====-----\n")

class TempTracker:
    def __init__(self):
        self.temps = []

    def __str__(self):
        return str(self.temps)

    def insert(self, temp):
        self.temps.append(temp)

    def get_max(self):
        return max(self.temps)

    def get_min(self):
        return min(self.temps)

    def get_mean(self):
        return sum(self.temps) / len(self.temps)

    def get_mode(self):
        keys = set(self.temps)
        counts = dict()
        for i in keys:
            counts[i] = self.temps.count(i)
        return max(counts, key=counts.get)

job_a = TempTracker()
job_length = random.randint(1, 100)
for i in range(job_length):
    job_a.insert(random.randint(0, 110))

e = "wat"

print(f"Job A length: {job_length}")
print(f"Job A: {job_a}")
print(f"Job A Max Temp: {job_a.get_max()}")
print(f"Job A Min Temp: {job_a.get_min()}")
print(f"Job A Mean Temp: {job_a.get_mean()}")
print(f"Job A Mode Temp: {job_a.get_mode()}")

# Problem 5.
# Suppose we had a list of n integers sorted in ascending order. How quickly could we check if a given integer is in the list?
# Write a fast function to check a given integer in the list.

print(f"\n-----===== Problem 5 =====-----\n")

def FindInteger(IntegerList, given):
    found = False
    if len(IntegerList) > 1:
        mid = len(IntegerList) // 2
        if IntegerList[mid] == given:
            found = True
        elif given < IntegerList[mid]:
            found = FindInteger(IntegerList[:mid], given)
        else:
            found = FindInteger(IntegerList[mid+1:], given)
    elif len(IntegerList) == 1 and IntegerList[0] == given:
        found = True
    return found

a = "ever"

my_integer_list = []
integer_list_length = random.randint(1,10)
for i in range(integer_list_length):
    my_integer_list.append(i + 1)

lost_integer = random.randint(1, 10)

print(f"Integer List: {my_integer_list}")
print(f"Given Integer: {lost_integer}")
print(f"Find Integer: {FindInteger(my_integer_list, lost_integer)}")

print(f"\n-----===== End =====-----\n")

print(f"You {a} {b} like {c} {d} {e + f}")
