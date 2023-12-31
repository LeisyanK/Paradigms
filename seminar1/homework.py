# imperative
def Partition(array, l, r):
    x = array[r]  # опорный элемент
    begin = l
    for i in range(l, r):
        if(array[i] <= x):
            tmp = array[begin]
            array[begin] = array[i]
            array[i] = tmp
            # for num in array:
            #     print(num, end=" ")
            # print()
            begin = begin + 1
    array[r] = array[begin]
    array[begin] = x
    return begin

def QuickSort(array, l ,r):
    if(l < r):
        q = Partition(array, l, r)
        QuickSort(array, l, q - 1)
        QuickSort(array, q + 1, r)


array = [6, 4, 9, 3, 2, 9, 1, 7]
print("Массив:")
for num in array:
    print(num, end=" ")
print()

# declarative
array2 = sorted(array)
print("Декларативная парадигма:")
for num in array2:
    print(num, end=" ")
print()

# imperative
size = len(array)
if (size > 0):
    QuickSort(array, 0, size - 1)
    print("Императивная парадигма:")
for num in array:
    print(num, end=" ")
print()