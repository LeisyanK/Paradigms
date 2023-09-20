# Абстрактный метод будет возвращать ошибку при создании его экземпляра. можно создавать только потомков

class Shape:
    def __init__(self):  # это конструктор класса
        raise TypeError("Ошибка создания экземпляра абстрактного класса")

    def get_area(self):
        raise TypeError("Ошибка вызова абстрактного метода")

    def get_perimeter(self):
        raise TypeError("Ошибка вызова абстрактного метода")

    @staticmethod
    def get_pi():
        return 3.14

a = Shape()
a.get_area  # Shape.get_area(a)