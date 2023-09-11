# доля положит, отр чисел и нуля
def proportion(array) -> float:
    size = len(array)
    if size == 0:
        # print("Массив пустой")
        # return 
        raise ValueError("Пустой массив")
    else:
        poz = 0
        neg = 0
        zero = 0
        for num in array:
            if num > 0:
                poz += 1
            elif num < 0:
                neg += 1
            else: 
                zero += 1
        # print($"Доля положительных чисел: {poz/size} + ", отрицательных чисел: " + neg/size + ", нулей: " + zero/size)
        return poz/size, neg/size, zero/size

array = [1,2,3,-6,0, -7,4, 8, -9, 7]
# array = []
print(proportion(array))