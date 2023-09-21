def filter_persons(persons: list[str], border_age: int) -> list[str]:
    return list(filter(lambda person: int(person.split("; ")[1]) > border_age, persons))
#  split() убирает справа и слева невидимые символы табуляции, пробела, переноса строки

def filter_persons_1(persons: list[str], border_age: int) -> list[str]:
    return filter(lambda person: int(person.split(";")[1].strip()) > border_age, persons)

persons_lst = ["Иванов И.И.; 20", "Петров П.П.; 35", "Мухаммедова Э.З.; 45"]

print(persons_lst)
print(filter_persons(persons_lst, 30))
print(*filter_persons_1(persons_lst, 30))

a = " \n\t 123 \t\n\n\t"

print([a])
print([a.strip()])
print([a.lstrip()])
print([a.rstrip()])