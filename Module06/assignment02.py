
from random import randint

print("-----===== Start =====-----\n")

print("\n-----===== BiggieSize =====-----\n")

my_list = []
for i in range(randint(1,10)):
    my_list.append(randint(-10,10))

print(f"My List: {my_list}")

print("\n-----===== End =====-----")