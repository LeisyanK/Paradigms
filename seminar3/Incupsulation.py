class Shape:
    def __init__(self):  # это конструктор класса
        raise TypeError("Ошибка создания экземпляра абстрактного класса")

    def get_area(self):
        raise TypeError("Ошибка вызова абстрактного метода")

    def get_perimeter(self):
        raise TypeError("Ошибка вызова абстрактного метода")

class Curcle(Shape_abstract):

    def __init__(self, r):  # это конструктор класса
        # super().__init__(r)  # инициализация экземпляра клааса-родителя. Но у нас абстрактный класса, поэтому выдастся ошибка, которую мы сами записали
        # Shape.__init__(self) по факту так вызывается
        self._radius = r  # _radius означает protected

    def get_area(self):
        return pi *  self._radius * self._radius

    def get_perimeter(self):
        return 2 * pi * self._radius

class Square(Shape_abstract):

    def __init__(self, a):  # это конструктор класса
        # super().__init__(r)  # инициализация экземпляра клааса-родителя. Но у нас абстрактный класса, поэтому выдастся ошибка, которую мы сами записали
        # Shape.__init__(self) по факту так вызывается
        self.__side = a  # __side означает private

    def get_area(self):
        return self.__side * self.__side

    def get_perimeter(self):
        return 4 * self.__side

# полиморфный метод - одним методом мы запускаем одно и то же действие для разных объектов
def get_area(obj: Shape):
    return obj.get_area()


curcle1 = Curcle(2)
curcle2 = Square(2)
print(get_area(curcle1))
print(get_area(curcle2))

# инкапсуляция в проверке
print(curcle1._radius)  # к protected-значению есть доступ
print(curcle2.__side)   # вывода не будут, т.к. данная переменная недоступна (переименована)
                        # теперь она называется _Square__side
print(curcle2._Square__side)