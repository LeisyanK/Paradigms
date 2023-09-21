#1
def find_duplicates(lst: list[int]) -> set[int]:
    return set(filter(lambda x: lst.count(x) > 1, lst)) #)))
    # return filter(lambda x: lst.count(x) > 1, lst)

lst_in = [1, 2, 5, 3, 2, 4, 5, 6, 7]

print(lst_in)
print(list(find_duplicates(lst_in)))


#2
num = [3, 5, 3, 6, 43, 4, 4, 9, 34, 6, 88, 32, 55]
print(list(set(filter(lambda x: num.count(x) > 1, num))))

#3
from typing import List
from random import randint


def double_search(lst: List[int]) -> List[int]:
    return list(set(filter(lambda x: lst.count(x) > 1, lst)))


data_list = [randint(0, 10) for i in range(10)]
print(data_list)
print(double_search(data_list))

#4
def search_duplicates(arr):
    uniq_set = set()
    return list(filter(lambda x: x in uniq_set or uniq_set.add(x), arr))

arr = [2, 3, 4, 2, 1, 5, 6, 4, 7, 8, 3, 1]

duplicates = search_duplicates(arr)
print(duplicates)


#5
def search_duplicates(arr):
    count_items = {}
    for item in arr:
        count_items.setdefault(item, 0)
        count_items[item] += 1
    return list(filter(lambda x: count_items[x] > 1, count_items))

arr = [8, 4, 7, 0, 4, 0, 10, 4, 7, 4]

duplicates = search_duplicates(arr)
print(duplicates)