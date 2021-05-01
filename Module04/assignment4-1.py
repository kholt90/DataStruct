
# Your quirky boss collects rare, old coins...
# They found out you're a programmer and asked you to solve something they've been wondering for a long time.
# Write a function that, given:
# an amount of money
# a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.
# Example: for amount=44 (44¢) and denominations=[1,2,3][1,2,3] (11¢, 22¢ and 33¢), your program would output 44—the number of ways to make 44¢ with those denominations:
# 1¢, 1¢, 1¢, 1¢
# 1¢, 1¢, 2¢
# 1¢, 3¢
# 2¢, 2¢

print("-----===== Start =====-----\n")

from random import randint

def quirkyBoss(amount, denominations, combo=[]):
    count = 0
    if sum(combo) == amount:
        count += 1
    elif sum(combo) < amount:
        for i, e in enumerate(denominations):
            count += quirkyBoss(amount, denominations[i:], combo + [e])
    return count

target = randint(1,100)
denominations = [1, 5, 10, 25]

print(f"Target: {target}")
print(f"Denominations: {denominations}")
print(quirkyBoss(target, denominations))

print("\n-----===== End =====-----")