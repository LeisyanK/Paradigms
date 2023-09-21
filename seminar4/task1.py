# from typing import List

# def normalization(array: List[int]) -> List[float]:  # с typing будет работать везде
# def normalization(array: list[int]) -> list[float]:  # будет работать в python выше 10 версии (без typing)
def normalization(array):    
    x_min = min(array)
    x_max = max(array)
    return list(map(lambda x: round((x - x_min) / (x_max - x_min), 2), array))

arr = [10,17,15,7,3,24]
print(normalization(arr))