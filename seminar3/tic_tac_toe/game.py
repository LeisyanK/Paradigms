from board import Board
from person import Person
from comp import Comp
import random

class Game:
    # def __init__(player1, player2):
    #     pass

    def start_game(self):
        print("Start game")
        play = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        # self.board(play)
        # board = Board(play)

        print("""Выберите игроков: 
        #     1. Два бота
        #     2. Два человека
            3. Человек и бот""")
        if int(input()) == 3:
            p = Person()
            c = Comp()
            self.person_bot(p, c, play)


    def person_bot(self, person, bot, play_board):
        board = Board(play_board)
        player = random.randint(1, 2)
        counter = 0
        flag = True
        while flag:
            if player == 1:
                print('Твой ход:')
                x = int(input('Введите х: '))
                while 1 > x or x > 3:
                    x = int(input('Введите верное значение х: '))
                y = int(input('Введите y: '))
                while 1 > y or y > 3:
                    y = int(input('Введите верное значение y: '))
                # player = 2
                if play_board[y-1][x-1] != ' ':
                    print('Поле уже занято')
                else:
                    play_board[y-1][x-1] = 'x'
                    flag = self.check('x', play_board)
                    counter += 1
                    player = 2
                    # board = Board(play)
                    board.paint(play_board)
            else:
                x = random.randint(1, 3)
                y = random.randint(1, 3)
                # print('Ход Бота:', end=' ')  # можно посмотреть все попытки Бота
                # print(x, y)
                if play_board[y-1][x-1] == ' ':
                    print(f'Ход Бота: x = {x}, y = {y}')
                    play_board[y-1][x-1] = '0'
                    flag = self.check('0', play_board)
                    counter += 1
                    player = 1
                    board.paint(play_board)
            if counter == 9 and flag:
                print('ХОДОВ НЕ ОСТАЛОСЬ!')
                flag = False


    def check(self, label, my_list):
        for i in 0, 1, 2:
            if my_list[0][i] == label and my_list[1][i] == label and my_list[2][i] == label:
                return self.answer(label)
            elif my_list[i][0] == label and my_list[i][1] == label and my_list[i][2] == label:
                return self.answer(label)
        else:
            if my_list[0][0] == label and my_list[1][1] == label and my_list[2][2] == label:
                return self.answer(label)
            elif my_list[2][0] == label and my_list[1][1] == label and my_list[0][2] == label:
                return self.answer(label)
            else:
                return True


    def answer(self, label):
        print(f'ВЫИГРАЛИ {label}!')
        return False


game = Game()
game.start_game()
# game.board()