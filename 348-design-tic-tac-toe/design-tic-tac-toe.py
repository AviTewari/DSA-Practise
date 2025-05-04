class TicTacToe:

    def __init__(self, n: int):
        self.r = defaultdict(int)
        self.c = defaultdict(int)
        self.rd = 0
        self.ld = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        number = 0
        if player == 1:
            number = -1
        else:
            number = 1
        self.r[row]+=number
        self.c[col]+=number
        if row == col:
            self.ld += number
        if row + col == self.n - 1:
            self.rd += number
        if abs(self.r[row]) == self.n:
            return player
        elif abs(self.c[col]) == self.n:
            return player
        elif abs(self.rd) == self.n:
            return player
        elif abs(self.ld) == self.n:
            return player
        else:
            return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)