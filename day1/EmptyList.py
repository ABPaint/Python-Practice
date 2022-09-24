list1 =[]
list2 = [3,5,6]

def checkList(list):
    if len(list) == 0:
        return "Empty"
    else:
        return "Not empty"

print(list1, checkList(list1))
print(list2, checkList(list2))