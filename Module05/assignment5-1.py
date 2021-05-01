
# A building has 100 floors.
# One of the floors is the highest floor an egg can be dropped from without breaking.
# If an egg is dropped from above that floor, it will break.
# If it is dropped from that floor or below, it will be completely undamaged and you can drop the egg again.
# Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.

print("\n-----===== Start =====-----\n")

from random import randint

def EggBreak(floors, breaking_point, eggs, step):
    print(f"Breaking Point: {breaking_point}")
    drop_count = 1
    drop = floors // step
    while eggs > 1 and step > 1:
        if drop < breaking_point:
            drop_count += 1
            drop += step
        else:
            eggs -= 1
            drop -= step
            step = step // 2
    while drop < breaking_point:
        drop += 1
        drop_count += 1
    return drop, drop_count

floors = 100
breaking_point = randint(1, floors)
eggs = 2
step = 10

print(f"First Test, {floors} floors, {eggs} eggs, {step} step")
floor, count = EggBreak(floors, breaking_point, eggs, step)
print(f"Floor {floor}; Drops: {count}")

floors = randint(10, 100)
breaking_point = randint(1, floors)
eggs = randint(1,10)
step = floors // 2
step = randint(10 if floors > 10 else 1, step if step > 10 else 10)

print(f"\nSecond Test, {floors} floors, {eggs} eggs, {step} step")
floor, count = EggBreak(floors, breaking_point, eggs, step)
print(f"Floor {floor}; Drops: {count}")

print("\n-----===== End =====-----")