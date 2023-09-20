import Shape_abstract
from math import pi as PI

class Curcle(Shape_abstract):

    def __init__(self, r):  # это конструктор класса
        # super().__init__(r)  # инициализация экземпляра клааса-родителя. Но у нас абстрактный класса, поэтому выдастся ошибка, которую мы сами записали
        # Shape.__init__(self) по факту так вызывается
        self.radius = r

    def get_area(self):
        return PI *  self.radius * self.radius

    def get_perimeter(self):
        return 2 * PI * self.radius

curcle1 = Curcle(2)
print("Площадь: ", curcle1.get_area())
print(curcle1.get_perimeter())