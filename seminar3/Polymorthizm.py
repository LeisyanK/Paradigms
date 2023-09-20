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
        self.radius = r

    def get_area(self):
        return pi *  self.radius * self.radius

    def get_perimeter(self):
        return 2 * pi * self.radius

class Square(Shape_abstract):

    def __init__(self, a):  # это конструктор класса
        # super().__init__(r)  # инициализация экземпляра клааса-родителя. Но у нас абстрактный класса, поэтому выдастся ошибка, которую мы сами записали
        # Shape.__init__(self) по факту так вызывается
        self.side = a

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

# полиморфный метод - одним методом мы запускаем одно и то же действие для разных объектов
def get_area(obj: Shape):
    return obj.get_area()


curcle1 = Curcle(2)
curcle2 = Square(2)
print(get_area(curcle1))
print(get_area(curcle2))