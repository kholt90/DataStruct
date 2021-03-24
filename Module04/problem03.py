
print(f"\n---- START -----\n")

def quirkyBoss(amount, denominations, combo=[], count=0):
    if sum(combo) == amount:
        print(combo)
        count += 1
    elif sum(combo) < amount:
        for i, e in enumerate(denominations):
            count += quirkyBoss(amount, denominations[i:], combo + [e])
    return count

# a = 2
# a = 4
# a = 6
# a = 8
a = 256
# b = [1]
# b = [1, 2]
b = [1, 2, 3]
# b = [1, 2, 3, 4]
# b = [4, 3, 2, 1]
# b = [3, 2, 4, 1]
# b = [10]

print(quirkyBoss(a, b))

print(f"\n---- END -----\n")
