"""
Building a Tic Tac Toe Class
"""

class TicTacToe():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns 
        self.matrix = [[ '_' for i in range(rows)] for j in range(columns)]

    def display_board(self): 
        return self.matrix

    def edit_board(self, player, i, j): 
        if self.matrix[i][j] == '_':
            self.matrix[i][j] = player
        else:
            print(f'({i},{j}) is already taken! Please make a different move on an open spot')
        display_tt = []
        for row in self.matrix:
            display_tt.append(row)
        return display_tt

    def check_winner_row(self):
        for row in self.matrix:
            print(f'row is {row}')
            if len(set(row)) == 1:
                return 'winner!'

    def check_winner_column(self):
        for row in self.matrix:
            for column in row:
                if len(set(column)) == 1:
                    return 'winner!'

    # def check_winner_diagnol(self):
    #     for row in self:

tt = TicTacToe(3, 3) 
print(tt.display_board())   
print(tt.edit_board('x', 0, 0))
print(tt.edit_board('x', 1, 1))
print(tt.edit_board('x', 2,2)) 
print(tt.check_winner_row())
print(tt.check_winner_column())