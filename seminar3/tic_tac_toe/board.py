# рисует доску 
class Board:
    def __init__(self, play_board):
        self.paint(play_board)

    def paint(self, board_list):
        print('   | X1| X2| X3|')
        print('----------------')
        for i in 0, 1, 2:
            print(f'Y{i + 1} |', end='')
            for j in 0, 1, 2:
                print(f' {board_list[i][j]} |', end='')
                # print(f' {i,j} |', end='')
            print()
            print('----------------')