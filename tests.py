import unittest
from logic import Game, HumanPlayer, BotPlayer



class TestLogic(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.board_list = [
        [['X', 'X', 'X'],
        ['O', 'X', 'O'],
        ['O', 'O', 'X'],],
        [['X', 'O', 'X'],
        ['O', 'O', 'O'],
        ['O', 'X', 'X'],],
        [['O', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'O', 'O'],],
        [['X', 'O', 'X'],
        ['O', 'X', 'O'],
        ['O', 'X', 'O'],],
        [['X', 'O', 'X'],
        ['X', None, None],
        ['X', None, None],],
        [['X', 'O', 'O'],
        [None, 'O', None],
        [None, 'O', None],],
        [['X', None, 'O'],
        [None, None, 'O'],
        ['O', None, 'O'],],
        [[None, None, None],
        [None, None, None],
        [None, None, None],],
        [['X', None, 'X'],
        [None, 'X', 'O'],
        ['X', 'O', 'X'],],
        [['O', 'X', 'O'],
        [None, 'O', 'O'],
        ['X', 'X', 'O'],]
        ]

    # 1. The game is initialized with an empty board
    def test_game_initialization(self):
        game = Game(1)
        empty_board = [[None, None, None],[None, None, None],[None, None, None]]
        self.assertEqual(game.board, empty_board)
        game = Game(2)
        self.assertEqual(game.board, empty_board)
    
    # 2. The game is initialized with either 2 players (human-human) or 1 player (human-bot)
    def test_player_amount(self):
        game = Game(1)
        self.assertEqual(type(game.playerX),HumanPlayer)
        self.assertEqual(type(game.playerO),BotPlayer)
        game = Game(2)
        self.assertEqual(type(game.playerX),HumanPlayer)
        self.assertEqual(type(game.playerO),HumanPlayer)

    # 3. Players are assigned a unique piece to play: X or O
    def test_player_symbol(self):
        game = Game(1)
        self.assertEqual(game.playerX.symbol,'X')
        self.assertEqual(game.playerO.symbol,'O')
        game = Game(2)
        self.assertEqual(game.playerX.symbol,'X')
        self.assertEqual(game.playerO.symbol,'O')

    # 4. After one player plays, the other player has a turn
    def test_other_player(self):
        game = Game(1)
        self.assertEqual(game.other_player(game.playerX), game.playerO)
        self.assertEqual(game.other_player(game.playerO), game.playerX)
        game = Game(2)
        self.assertEqual(game.other_player(game.playerX), game.playerO)
        self.assertEqual(game.other_player(game.playerO), game.playerX)

    # 5. All winning end of the games detected, and draw games are identified 
    def test_game_end(self):
        game_end_list = [True, True, True, True, True, True, True, False, True, True]
        for i, board in enumerate(self.board_list):
            game = Game(2)
            game.board = board # type: ignore
            self.assertEqual(game.game_end(), game_end_list[i])

    # 6. Players can play only in viable spots
    def test_valid_move(self):
        game = Game(1)
        game.board = [['O', 'X', None], ['X', 'X', None], [None, None, 'O']]
        game.playerX.all_avaliable_position(game.board)
        self.assertEqual(game.playerX.available_positions, [[0, 2], [1, 2], [2, 0], [2, 1]] ) # type: ignore
        game.playerO.all_avaliable_position(game.board)
        self.assertEqual(game.playerO.available_positions, [[0, 2], [1, 2], [2, 0], [2, 1]] ) # type: ignore
        
    # 7. The correct game winner, if one exists, is detected
    def test_get_winner(self):
        game_winner_list = ['X', 'O', 'O', None, 'X', 'O', 'O', None, 'X', 'O']
        for i, board in enumerate(self.board_list):
            game = Game(2)
            game.board = board # type: ignore
            self.assertEqual(game.get_winner(), game_winner_list[i])
        

if __name__ == '__main__':
    unittest.main()
