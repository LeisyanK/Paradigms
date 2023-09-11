# рекурсивный поиск элемента в массиве (количество)

def search_declarative(target, array, i=0, count=0):
    if i >= len(array):
        return count
    tmp = 0
    if isinstance(array[i], list):
        tmp = search_declarative(target, array[i], i=0, count=0)
    if array[i] == target:
        count += 1
    return search_declarative(target, array, i=i+1, count=count+tmp)

array = [1,2,3,[4,5,6], 7, 8,[9,10,[11,12,13], 14], 15,15,16]
print(search_declarative(15, array))
