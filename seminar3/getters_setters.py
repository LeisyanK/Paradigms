class A:
    __m = 55

    @property
    # def get_m(self):
    def m(self):
        return self.__m

    @m.setter # для отмены изменения _m1 убираем setter
    # def set_m(self, value):
    def m(self, value):
        # можно добавить проверку при необходимости
        if isinstance(value, int) and (value > 0):
            self.__m = value
        else:
            self.__m = value
    
    @m.getter
    # def get_value(self):
    def m(self):
        return self.__m

a = A()

a.m = 13

print(a.m)