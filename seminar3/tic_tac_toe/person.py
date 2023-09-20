from player import Player

class Person(Player):
    def __init__(self):
        pass

    def next_step(self):
        print("Выберите координаты поля: ")
        x = input()
        y = input()