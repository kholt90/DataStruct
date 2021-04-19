
def ugly_number(n=1, a=2, b=3, c=4):
    ugly_list = []
    aa, bb, cc = 1, 1, 1
    for i in range(n):
        x = a * aa
        y = b * bb
        z = c * cc
        if x <= y and x <= z:
            print(f"index: {i}, value x: {x}")
            ugly_list.append(x)
            aa += 1
        elif y <= x and y <= z:
            print(f"index: {i}, value y: {y}")
            ugly_list.append(y)
            bb += 1
        elif z <= x and z <= y:
            print(f"index: {i}, value z: {z}")
            ugly_list.append(z)
            cc += 1
    print(ugly_list)
    return ugly_list[-1]

print(ugly_number(5, 4, 7, 6))
