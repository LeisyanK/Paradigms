def filter_by_age(people, age):
    filtered_people = filter(lambda x: x['age'] > age, people)
    return len(list(filtered_people))

people = [
{'name': 'Alla', 'age': 25},
{'name': 'Ivan', 'age': 40},
{'name': 'Vika', 'age': 35},
{'name': 'Julia', 'age': 30}
]

count = filter_by_age(people, 30)
print(count)


len(a) # -> a.__len__()
print(dir([])) # функции, которые есть у объекта
print(dir(map(int,[1,2,3])))