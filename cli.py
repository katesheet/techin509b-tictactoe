# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board


def check_win(board):
  for row in board:
    if row == ['O','O','O']:
      return "O won"
    elif row == ['X', 'X', 'X']:
      return "X won"
  for k in range(3):
    column = [board[i][k] for i in range(3)]
    # print(column)
    if column == ['O','O','O']:
      return "O won"
    elif column == ['X', 'X', 'X']:
      return "X won"
  diagonal_a = [board[i][i] for i in range(3)]
  diagonal_b = [board[i][2-i] for i in range(3)]
  for diag in [diagonal_a, diagonal_b]:
    if diag == ['O','O','O']:
      return "O won"
    elif diag == ['X', 'X', 'X']:
      return "X won"
  return None

board = [['O', 'O', 'O'],
         ['X', 'X', 'X'],
         ['O', 'O', 'X']]

def print_board(board):
    for i in range(3):
        print(board[i])





# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    # players = ["X","O"]
    p1 = 'X'
    p2 = 'O'
    p = p1
    move_cnt = 0
    while winner == None and move_cnt < 9:
        print("TODO: take a turn!")
        # Show the board to the user.
        print_board(board)
        # TODO: Input a move from the player.
        while True:
            try:
                move_a = input(f"You are {p}! Enter your move in the format of (x,y): ")
                x,y = move_a.split(",")
                x,y = int(x)-1,int(y)-1
            except:
                print('invalid move! please see instruction')
                continue
            
            # TODO: Update the board.
            if x > 2 or x < 0 or y > 2 or y < 0:
                print('invalid move! out of board')
                continue
            if board[x][y] is not None:
                print('invalid move! position taken')
                continue
            else:
                board[x][y] = p
                break
        move_cnt = move_cnt + 1
        # TODO: Update who's turn it is.
        if p == p1:
            p = p2
        else:
            p = p1
        # print_board(board)
        # winner = 'X'  # FIXME
        winner = check_win(board)
    print_board(board)
    if winner is not None:
        print(winner)
    else:
        print("draw")
