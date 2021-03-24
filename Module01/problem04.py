
def highest_product_of_three(list_of_ints):
    list_of_ints.sort()
    product_1 = list_of_ints[-2] * list_of_ints[-3]
    product_2 = list_of_ints[0] * list_of_ints[1]
    if product_1 > product_2:
        return product_1 * list_of_ints[-1]
    else:
        return product_2 * list_of_ints[-1]

list_of_ints = [-10, -10, 1, 3, 2]

print(f"Product: {highest_product_of_three(list_of_ints)}")
