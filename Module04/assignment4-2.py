
# You are a renowned thief who has recently switched from stealing precious metals to stealing cakes because of the insane profit margins.
# You end up hitting the jackpot, breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.
# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.
# Each type of cake has a weight and a value, stored in a tuple with two indices:
# An integer representing the weight of the cake in kilograms
# An integer representing the monetary value of the cake in British shillings

# For example:
# # Weighs 7 kilograms and has a value of 160 shillings
# (7, 160)
# # Weighs 3 kilograms and has a value of 90 shillings
# (3, 90)

# You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.
# Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.

# For example:
# cake_tuples = [(7, 160), (3, 90), (2, 15)]
# capacity    = 20
# # Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
# max_duffel_bag_value(cake_tuples, capacity)

# Weights and values may be any non-negative integer. Yes, it's weird to think about cakes that weigh nothing or duffel bags that can't hold anything. But we're not just super mastermind criminals—we're also meticulous about keeping our algorithms flexible and comprehensive.

print("-----===== Start =====-----\n")

from math import prod

def CakeSort(cake):
    result = cake[1]/cake[0] if 0 < cake[0] else 0
    return result

def ValuateBag(bag):
    value = 0
    for cake in bag:
        value += cake[1]
    return value

def WeighBag(bag):
    weight = 0
    for cake in bag:
        weight += cake[0]
    return weight

def StuffBag(cakes, capacity):
    bag = []
    bag_weight = 0
    if 0 < len(cakes):
        while bag_weight + cakes[0][0] <= capacity:
            bag.append(cakes[0])
            bag_weight = WeighBag(bag)
        if bag_weight < capacity:
            bag += StuffBag(cakes[1:], capacity - bag_weight)
    return bag

def MaxBagValue(cakes, capacity):
    if capacity <= 0:
        value = "Bag can't hold anything"
    elif prod([cake[0] for cake in cakes]) == 0:
        value = "Weightless cakes make you infinitely rich."
    else:
        bag = StuffBag(cakes, capacity)
        value = ValuateBag(bag)
    return value

cake_tuples = [(7, 160), (3, 90), (2, 15)]
cake_tuples.sort(key=CakeSort, reverse=True)

capacity = 20

print(f"Bag Value: {MaxBagValue(cake_tuples, capacity)}")

print("\n-----===== End =====-----")