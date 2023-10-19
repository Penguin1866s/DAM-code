def union(list1 , list2):
    for i in list2:
        if list2.index(i) != 0:
            list1.append(i)
        else:
            continue
    return list1 , list2

a = [1 , 2 , 3]
b = [2 , 4 , 6]
print(union(a , b))
