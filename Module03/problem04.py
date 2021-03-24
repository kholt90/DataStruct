
import collections
import regex

def sortSub(word):
    return len(word)

def findSubs(s1):
    subs = [s1[i: j] for i in range(len(s1)) for j in range(i + 1, len(s1) + 1)]
    subs.sort(reverse=True,key=sortSub)
    return subs

def longySub(s1):
    subs = findSubs(s1)
    for sub in subs:
        if len(sub) > 1 and subs.count(sub) > 1:
            return sub
    return ""

def longySubREGEX(s1):
    subs = findSubs(s1)
    for sub in subs:
        print(f"{sub}:")
        if len(regex.findall(sub, s1, overlapped=True)) > 1 and len(sub) > 1:
            return sub
        else:
            print("no dupe")
    return ""

print(f"Substring: {longySubREGEX('start')}")
print(f"Substring: {longySub('banana')}")
print(f"Substring: {longySub('banbana')}")
print(f"Substring: {longySub('banabana')}")
print(f"Substring: {longySub('ragecage')}")
print(f"Substring: {longySub('iceage')}")
print(f"Substring: {longySub('abcd')}")
