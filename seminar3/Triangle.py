import Shape_abstract


class Triangle(Shape_abstract):
    def __init__(self, a, b):
        self.side1 = a
        self.side2 = b

    def get_area(self):  # верный метод
        return self.side1 * self.side2 / 2
    
    @staticmethod # не передаем self, т.к. внутри метода он не используется, передаем только стороны
    def get_area(a, b):
        return a * b / 2

    # второй способ вызова метода - может работать и с переданными значениями, и с внутренними
    def get_area(self, a=None, b=None):
        a_ = a or side1 # если при вызове метода не передали a и b, т.е по факту None, то берутся значения side1 и side2
        b_ = b or side2
        return a_ * b_ / 2

    # проверяем: если все параметры переданы, то используем их; если переданы не все, то используем внутренные параметры
    def get_area(self, a=None, b=None):
        if a:
            return (a * b) / 2
        else:
            return (self.side1 * self.side2) / 2

    def get_perimeter(self):
        return self.side1 + self. side2 + math.sqrt(self.side1 * self.side1 + self.side2 * self.side2)
    
tri = Triangle(2,3)
print(tri.get_area())
print(tri.get_perimeter())
