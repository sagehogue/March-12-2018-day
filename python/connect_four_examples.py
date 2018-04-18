import os
import colorful


class Tile:
    def __init__(self, edges="[{}]"):
        self.token = None
        self.edges = edges

    def display_token(self):
        if self.token:
            if self.token.lower() == 'b':
                return colorful.blue(self.edges.format(self.token))
            elif self.token.lower() == 'r':
                return colorful.red(self.edges.format(self.token))
        else:
            return colorful.white(self.edges.format(' '))

    def __str__(self):
        return self.edges.format(self.token or ' ')


class Board:
    def __init__(self):
        self.board = self.create_board()

    def create_board(self):
        return {y_coo: {a: Tile() for a in range(7)} for y_coo in range(6)}

    def display(self):
        # os.system('cls' if os.name=='nt' else 'clear')
        print()
        print('*' * 21)
        print(" {}  {}  {}  {}  {}  {}  {} ".format(1, 2, 3, 4, 5, 6, 7))
        for i in self.board:
            print('{}{}{}{}{}{}{}'.format(
                self.board[i][0].display_token(), self.board[i][1].display_token(),
                self.board[i][2].display_token(), self.board[i][3].display_token(),
                self.board[i][4].display_token(), self.board[i][5].display_token(),
                self.board[i][6].display_token()
            ))
        print('*' * 21)
        print()

    def place_token(self, player, column):
        for i in range(len(self.board)):

            if self.board[i][column].token:
                try:
                    self.board[i - 1][column].token = player
                except KeyError:
                    return False
                return True
            elif i == 5 and not self.board[i][column].token:
                self.board[i][column].token = player
                return True
        return False

    def check_vertical(self):
        for y in range(len(self.board[0])):
            check = ''
            for i in range(len(self.board)):
                if self.board[i][y].token:
                    check += self.board[i][y].token.lower()
                else:
                    check += ' '
            if 'rrrr' in check:
                return True, 'Red'
            elif 'bbbb' in check:
                return True, 'Blue'
        return False, None

    def check_horizontal(self):
        for y in range(len(self.board)):
            check = ''.join([' ' if not p.token else p.token.lower() for p in self.board[y].values()])
            if 'rrrr' in check:
                return (True, 'Red')
            elif 'bbbb' in check:
                return (True, 'Blue')
        return (False, None)

    def check_diagonal(self):
        for x in range(len(self.board[0]) - 4):
            for y in range(len(self.board) - 4):
                check = '{}{}{}{}'.format(
                    self.board[y][x].token or ' ',
                    self.board[y + 1][x + 1].token or ' ',
                    self.board[y + 2][x + 2].token or ' ',
                    self.board[y + 3][x + 3].token or ' '
                ).lower()
                if 'rrrr' in check:
                    return (True, 'Red')
                elif 'bbbb' in check:
                    return (True, 'Blue')
        for x in range(4, len(self.board[0])):
            for y in range(4, len(self.board)):
                check = '{}{}{}{}'.format(
                    self.board[y][x].token or ' ',
                    self.board[y - 1][x - 1].token or ' ',
                    self.board[y - 2][x - 2].token or ' ',
                    self.board[y - 3][x - 3].token or ' '
                ).lower()
                print(check)
                if 'rrrr' in check:
                    return (True, 'Red')
                elif 'bbbb' in check:
                    return (True, 'Blue')
        return (False, None)

    def check_win(self):
        vert = self.check_vertical()
        horz = self.check_horizontal()
        diag = self.check_diagonal()
        if vert[0]:
            return vert
        elif horz[0]:
            return horz
        elif diag[0]:
            return diag
        else:
            return (False, None)


class ConnectFour:
    def __init__(self):
        self.board = Board()


def ask_collumn():
    asking = True
    error_text = 'Pleace enter a number from 1 to 7 to place your token.'
    while asking:
        try:
            q = int(input('{}\'s turn. Enter the collumn number you wish to place your token: '.format(i)))
            if q > 7 or q < 1:
                print(error_text)

                continue
            return q
        except ValueError:
            print(error_text)
            continue


b = ConnectFour()
players = ['R', 'B']

while True:
    for i in players:
        b.board.display()
        q = ask_collumn()
        b.board.place_token(i, q - 1)
        win = b.board.check_win()
        if win[0]:
            b.board.display()
            print('{} Wins!'.format(win[1]))
            exit()
