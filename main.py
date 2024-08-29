class Game():
    def __init__(self):
        self.grids = [self.creategrid() for i in range(9)]
        self.grid = self.grids[4]
        self.biggrid = [' ' for _ in range(9)]
        self.running = True
        self.player = False #False – p1, True – p2
        self.gridnum = 4
        self.wongrids = []
        self.wins = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 7))
        self.minigrid = [' ', ' ', ' ', 
                         ' ', '@', ' ', 
                         ' ', ' ', ' ']
        self.main()

    def main(self):
        self.outputgrids()
        while self.running:
            self.outputgrids()
            while self.gridnum in self.wongrids:
                outwongrids = []
                for i in self.wongrids:
                    outwongrids.append(i + 1)
                self.gridnum = int(input(f"Ведите номер поля от 1 до 9 (кроме {', '.join(list(map(str, outwongrids)))}): ")) - 1
            else:
                self.outputgrids()
            self.grid = self.grids[self.gridnum]
            
            self.move()
            self.checkwin()
            self.checkwinbig()
        self.outputgrids()
        if self.player:
            print("Победил X")
        else:
            print("Победил O")

    def creategrid(self):
        return [[' '] * 3 for i in range(3)]

    def output(self):
        print('+—————+—————+—————+')
        for row in self.grid:
            print('|', end='')
            for col in row:
                print(' ', col, ' |', end='')
            print('')
            print('+—————+—————+—————+')
    
    def outputgrids(self):
        print("    1   2   3     1   2   3     1   2   3  ")
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        out1 = f"1 | {' | '.join(self.grids[0][0])} | | {' | '.join(self.grids[1][0])} | | {' | '.join(self.grids[2][0])} |"
        out2 = f"2 | {' | '.join(self.grids[0][1])} | | {' | '.join(self.grids[1][1])} | | {' | '.join(self.grids[2][1])} |"
        out3 = f"3 | {' | '.join(self.grids[0][2])} | | {' | '.join(self.grids[1][2])} | | {' | '.join(self.grids[2][2])} |"
        out4 = f"1 | {' | '.join(self.grids[3][0])} | | {' | '.join(self.grids[4][0])} | | {' | '.join(self.grids[5][0])} |"
        out5 = f"2 | {' | '.join(self.grids[3][1])} | | {' | '.join(self.grids[4][1])} | | {' | '.join(self.grids[5][1])} |"
        out6 = f"3 | {' | '.join(self.grids[3][2])} | | {' | '.join(self.grids[4][2])} | | {' | '.join(self.grids[5][2])} |"
        out7 = f"1 | {' | '.join(self.grids[6][0])} | | {' | '.join(self.grids[7][0])} | | {' | '.join(self.grids[8][0])} |"
        out8 = f"2 | {' | '.join(self.grids[6][1])} | | {' | '.join(self.grids[7][1])} | | {' | '.join(self.grids[8][1])} |"
        out9 = f"3 | {' | '.join(self.grids[6][2])} | | {' | '.join(self.grids[7][2])} | | {' | '.join(self.grids[8][2])} |"
        print(out1)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out2)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out3)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print("    1   2   3     1   2   3     1   2   3  ")
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out4)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out5)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out6)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print("    1   2   3     1   2   3     1   2   3  ")
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out7)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out8)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print(out9)
        print("  +———+———+———+ +———+———+———+ +———+———+———+")
        print()

        print("+———+———+———+")
        for num, tile in enumerate(self.minigrid, 1):
            print(f"| {tile} ", end='')
            if num % 3 == 0:
                print("|")
                print("+———+———+———+")

        print()
        print("+———+———+———+")
        for num, tile in enumerate(self.biggrid, 1):
            print(f"| {tile} ", end='')
            if num % 3 == 0:
                print("|")
                print("+———+———+———+")

    def checkwin(self):
        if self.checkwincols() or self.checkwindiag() or self.checkwinrows():
            if self.player:
                self.grid = [['\033[1;36mX\033[0m', ' ', '\033[1;36mX\033[0m'],
                            [' ', '\033[1;36mX\033[0m', ' '],
                            ['\033[1;36mX\033[0m', ' ', '\033[1;36mX\033[0m']]
                self.grids[self.wongrids[-1]] = self.grid
            else:
                self.grid = [['\033[1;35mO\033[0m', '\033[1;35mO\033[0m', '\033[1;35mO\033[0m'],
                            ['\033[1;35mO\033[0m', ' ', '\033[1;35mO\033[0m'],
                            ['\033[1;35mO\033[0m', '\033[1;35mO\033[0m', '\033[1;35mO\033[0m']]
                self.grids[self.wongrids[-1]] = self.grid
        else:
            self.wongrids.pop()

    def checkwinrows(self):
        for row in self.grid:
            if len(set(row)) == 1:
                if row[0] != ' ':
                    return row[0]

    def checkwincols(self):
        grid = [list(i) for i in zip(*self.grid)]
        for row in grid:
            if len(set(row)) == 1:
                if row[0] != ' ':
                    return row[0]

    def checkwindiag(self):
        if ((self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ') or
            (self.grid[2][0] == self.grid[1][1] == self.grid[0][2] != ' ')):
            return self.grid[0][0]
        
    def checkwinbig(self):
        for win in self.wins:
            if all([self.biggrid[i] if self.biggrid[i] != ' ' else False for i in win]) and len(set([self.biggrid[i] if self.biggrid[i] != ' ' else False for i in win])) == 1:
                self.running = False
                # if self.player:
                #     print('X WIN')
                # else:
                #     print('Y WIN')

    def move(self):
        self.wongrids.append(self.gridnum)
        print(self.grid, self.gridnum, self.wongrids)
        y, x = map(int, input().split())
        self.gridnum = y - 1 + (x - 1) * 3
        self.minigrid = [' ' for _ in range(9)]
        self.minigrid[self.gridnum] = '@'
        while self.grid[x - 1][y - 1] != ' ':
            y, x = map(int, input().split())

        if self.player:
            self.grid[x - 1][y - 1] = 'O'
        else:
            self.grid[x - 1][y - 1] = "X"
        self.player = not self.player


a = Game()