
def twoStrings(s1, s2):
    """Compares two strings to find matching substring."""
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"

def twoStrings(s1, s2):
    """Compares two strings to find matching substring using set."""
    a = set(s1) if len(s1 >= s2) else set(s2)
    for i in s1:
        if i in s2:
            return "YES"
    return "NO"

print(twoStrings("abc", "rattle"))
print(twoStrings("bcd", "rattle"))
print(twoStrings("bcd", "battle"))
