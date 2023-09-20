from player import Player

class Comp(Player):
    def __init__(self):
        pass

    def next_step(self):
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        # x = random.randint(9) # 0..8
        # if check(x):
        #     board()
        # else:
        #     self.next_step()