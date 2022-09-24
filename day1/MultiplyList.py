from itertools import product


list1 = [2,2,2]

def multiplyList(list):
    result = 1
    for x in list:
        result = result * x
    return result


product = multiplyList(list1)
print(product)