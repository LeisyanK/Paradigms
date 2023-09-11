import random

def find_imperative(array, target):
    for num in array:
        if num == target:
            return True
    return False

array = []
for i in range(10):
    array.append(random.randint(-10, 10))
print(array)

print(find_imperative(array, 5))