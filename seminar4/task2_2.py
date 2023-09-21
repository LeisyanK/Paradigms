# на случай, если поле "возраст" пропущено
def filter_by_age(people, age):
    filtered_people = filter(lambda x: x.get('age', -1) > age, people)
    return len(list(filtered_people))

def filter_by_age_1(people, age):
    return sum(map(lambda x: x.get('age', -1) > age, people))

people = [
{'name': 'Alla', 'age': 25},
{'name': 'Ivan', 'age': 40},
{'name': 'Vika', 'age': 35},
{'name': 'Vika1'},
{'name': 'Julia', 'age': 30}
]

count = filter_by_age(people, 30)
print(count)

count_1 = filter_by_age_1(people, 30)
print(count_1)