# методу необходимо передать сам объект. Для статических методов не нужно передавать - они обозначаются декоратором @
class Shape:
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

    @staticmethod
    def get_pi():
        return 3.14

a = Shape()
a.get_area  # Shape.get_area(a) на самом деле происходит такой вызов