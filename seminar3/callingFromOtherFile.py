from Incupsulation import Square, Curcle, get_area

curcle1 = Curcle(2)
curcle2 = Square(2)
print(get_area(curcle1))
print(get_area(curcle2))

# инкапсуляция в проверке
print(curcle1._radius)  # к protected-значению есть доступ
print(curcle2.__side)   # вывода не будут, т.к. данная переменная недоступна (переименована)
                        # теперь она называется _Square__side
print(curcle2._Square__side)