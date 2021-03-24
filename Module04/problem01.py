
print("\n===== START =====\n")

def isp(inString, curString="", outSet=set()):
    if len(inString) == 1:
        outSet.add(curString + inString)
        return inString
    else:
        for i, c in enumerate(inString):
            # print()
            current = curString + c
            leftovers = inString[:i] + inString[i+1:]
            # print(f"For {inString}, {c} is at index {i}")
            # print(f"The current string is {current}")
            # print(f"The leftover characters are {leftovers}")
            isp(leftovers, current, outSet)
    return outSet

# theString = "abc"
theString = "kato"
theSet = isp(theString)
print(f"{theString}: {theSet}")