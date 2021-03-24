
import collections

def check_palindrome(astring):

    aDict = {}
    for i in astring:
        if i not in aDict.keys():
            aDict[i] = 1
        else:
            aDict[i] = (aDict[i] + 1) % 2
return sum(aDict.values()) > 1

print(checkPal('civic'))
print(checkPal('civc'))
print(checkPal('level'))
