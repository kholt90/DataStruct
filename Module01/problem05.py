
import math

def get_products_of_all_ints_except_at_index(list_of_ints):
    product = 1
    list_of_products = []
    for i in list_of_ints:
        for j in list_of_ints:
            if i != j:
                product *= j
        list_of_products.append(product)
        product = 1
    return list_of_products

def get_products_of_all_ints_except_at_index(list_of_ints):
    list_of_products = []
    for i, el in enumerate(list_of_ints):
        product = math.prod(list_of_ints[:i] + list_of_ints[i+1:])
        list_of_products.append(product)
    return list_of_products

# list_of_ints = [1, 7, 3, 4]
list_of_ints = [-10, -10, 1, 3, 2, 0]

print(get_products_of_all_ints_except_at_index(list_of_ints))
