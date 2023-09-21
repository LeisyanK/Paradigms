list1 = [1,2,3,4,5,6,7,5,3]
list2 = list(set(list1))
list1.remove(list2)
for elem in list2:
    list1.remove(elem)
print(*list1)

