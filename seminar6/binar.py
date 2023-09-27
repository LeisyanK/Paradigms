def binar(arr, num, start, end):
    center = int((end - start) / 2 + start)
    # print(start, ',', center, ',', end)
    if end < start:
        print(num, 'is not found.')
        # return -1
    else:
        if (arr[center] == num):
            print(num, "is in position", center)
            # return center
        elif (arr[center] > num):
            binar(arr, num, start, center - 1)
        else: 
            binar(arr, num, center + 1, end)
        

array = [1, 2, 4, 6, 7, 10, 16, 25, 26]
print(*array)
binar(array, 8, 0, len(array))
binar(array, 1, 0, len(array))
binar(array, 2, 0, len(array))