
from collections import Counter

def jewelCount(jewels, stones):
    jewelSet = set(jewels)
    stonesCount = Counter(stones)
    print(stonesCount)
    jewelsCount = 0
    for jewel in jewelSet:
        jewelsCount = jewelsCount + stonesCount[jewel]
        print(f"jewels: {jewel} count: {stonesCount[jewel]}")
    return jewelsCount

jewels = "abbc"
stones = "aaaaAAbbbb"

print(jewelCount(jewels, stones))
