# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
    """Determines the winner of the given board.
    Returns 'X', 'O', or None."""
    for row in board:
        if row == ['O','O','O']:
            return 'O'
        elif row == ['X', 'X', 'X']:
            return 'X'
    for k in range(3):
        column = [board[i][k] for i in range(3)]
        # print(column)
        if column == ['O','O','O']:
            return 'O'
        elif column == ['X', 'X', 'X']:
            return 'X'
    diagonal_a = [board[i][i] for i in range(3)]
    diagonal_b = [board[i][2-i] for i in range(3)]
    for diag in [diagonal_a, diagonal_b]:
        if diag == ['O','O','O']:
            return 'O'
        elif diag == ['X', 'X', 'X']:
            return 'X'
    return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    # if player == 'X':
    #     player = 'O'
    # else:
    #     player = 'X'
    # return player
    return 'O' if player == 'X' else 'X'

def play_game(board):
    winner = None
    # players = ["X","O"]
    player = 'X'
    move_cnt = 0
    while winner == None and move_cnt < 9:
        print("TODO: take a turn!")
        # Show the board to the user.
        print_board(board)
        # Input a move from the player.
        while True:
            try:
                move_a = input(f"You are {player}! Enter your move in the format of (x,y): ")
                x,y = move_a.split(",")
                x,y = int(x)-1,int(y)-1
            except:
                print('invalid move! please see instruction')
                continue
            
            # Update the board.
            if x > 2 or x < 0 or y > 2 or y < 0:
                print('invalid move! out of board')
                continue
            if board[x][y] is not None:
                print('invalid move! position taken')
                continue
            else:
                board[x][y] = player
                break
        move_cnt = move_cnt + 1
        # Update who's turn it is.
        player = other_player(player)
        winner = get_winner(board)
    print_board(board)
    if winner is not None:
        print(f'{winner} won')
    else:
        print("draw")


def print_board(board):
    for i in range(3):
        print(board[i])





