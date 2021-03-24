
def reverse_string(char_list):
    # for i, el in enumerate(char_list):
    i = 0
    while i <= len(char_list) / 2:
        j = len(char_list) - i - 1
        i += 1
        print(char_list[i] + ", " + char_list[j])
    print()

a = ["a"]
b = ["a", "b", "c", "d"]
c = ["a", "b", "c", "d", "e"]

reverse_string(a)
reverse_string(b)
reverse_string(c)

print(a)
print(b)
print(c)