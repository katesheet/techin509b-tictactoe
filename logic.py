# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self,symbol) -> None:
        # super().__init__()
        self.symbol = symbol
    
    def all_avaliable_position(self, board):
        available_positions = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] is None:
                    available_positions.append([i, j])
        self.available_positions = available_positions
        return available_positions

    
    @abstractmethod
    def get_move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
    
    def get_move(self, board):
        valid_positions = self.all_avaliable_position(board)
        while True:
            try:
                move_a = input(f"You are {self.symbol}! Enter your move in the format of (x,y): ")
                x,y = move_a.split(",")
                x,y = int(x)-1,int(y)-1
            except:
                print('invalid move! please see instruction')
                continue
            if x > 2 or x < 0 or y > 2 or y < 0:
                print('invalid move! out of board')
                continue
            if [x, y] not in valid_positions:
                print('invalid move! position taken')
                continue
            else:
                return [x,y]


class BotPlayer(Player):
    def __init__(self, symbol) -> None:
        super().__init__(symbol)
    
    def get_move(self, board):
        available_positions = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] is None:
                    available_positions.append([i, j])
        # print(available_positions)
        self.available_positions = available_positions

        random_option = random.choice(available_positions)
        print(f"Bot (as {self.symbol}) select: {random_option[0]+1},{random_option[1]+1}")
        return random_option


class Game:
    def __init__(self,player_amount) -> None:
        self.board = self.make_empty_board()
        if player_amount == 1:
            self.playerX = HumanPlayer('X')
            self.playerO = BotPlayer('O')
        elif player_amount == 2:
            self.playerX = HumanPlayer('X')
            self.playerO = HumanPlayer('O')
            

    def make_empty_board(self):
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    

    def print_board(self):
        for i in range(3):
            print(self.board[i])


    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""
        for row in self.board:
            if row == ['O','O','O']:
                return 'O'
            elif row == ['X', 'X', 'X']:
                return 'X'
        for k in range(3):
            column = [self.board[i][k] for i in range(3)]
            # print(column)
            if column == ['O','O','O']:
                return 'O'
            elif column == ['X', 'X', 'X']:
                return 'X'
        diagonal_a = [self.board[i][i] for i in range(3)]
        diagonal_b = [self.board[i][2-i] for i in range(3)]
        for diag in [diagonal_a, diagonal_b]:
            if diag == ['O','O','O']:
                return 'O'
            elif diag == ['X', 'X', 'X']:
                return 'X'
        return None


    def other_player(self, player):
        """Given the character for a player, returns the other player."""
        # if player == 'X':
        #     player = 'O'
        # else:
        #     player = 'X'
        # return player
        return self.playerO if player == self.playerX else self.playerX

    def game_end(self):
        if self.get_winner() is not None:
            return True
        none_cnt = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    none_cnt += 1
                    return False
        return True

    def play_game(self):
        winner = None
        player = self.playerX
        while not self.game_end():
            self.print_board()
            x,y = player.get_move(self.board) # type: ignore
            self.board[x][y] = player.symbol # type: ignore
            player = self.other_player(player)
        winner = self.get_winner()
        self.print_board()
        if winner is not None:
            print(f'{winner} won')
        else:
            print("It's a draw!")








