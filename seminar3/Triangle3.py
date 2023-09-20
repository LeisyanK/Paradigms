import Shape_abstract

class Triangle3(Shape_abstract):
    def __init__(self, a, b, c):
        self.catet1 = a
        self.catet2 = b
        self.hypotenuse = c

    def get_perimeter(self):
        return self.catet1 + self.catet2 + self.hypotenuse

    def get_area(self):
        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.catet1) * (p - self.catet2) * (p - self.hypotenuse))