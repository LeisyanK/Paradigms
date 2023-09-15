# imperative
def Partition(array, l, r):
    print("----")
    x = array[r]  # опорный элемент
    begin = l
    for i in range(r+1):
        if(array[i] <= x):
            tmp = array[begin]
            array[begin] = array[i]
            array[i] = tmp
            for num in array:
                print(num, end=" ")
            print()
            begin = begin + 1
        
        # print(begin)
    begin = begin - 1
    array[r] = array[begin]
    array[begin] = x
    return begin

def QuickSort(array, l ,r):
    if(l < r):
        q = Partition(array, l, r)
        QuickSort(array, l, q - 1)
        QuickSort(array, q + 1, r)


array = [6, 4, 9, 3, 2, 9, 1, 7]
# declarative
# array2 = sorted(array)
# for num in array2:
#     print(num)

# imperative
size = len(array)
if (size > 0):
    QuickSort(array, 0, size - 1)