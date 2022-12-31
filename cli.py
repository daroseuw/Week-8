# # This file contains the Command Line Interface (CLI) for
# # the Tic-Tac-Toe game. This is where input and output happens.
# # For core game logic, see logic.py.

from logic import Players, Board, Moves, PlayerType, Human, Bot

# Run the game from the CLI based on logic.py code:
class RunGame:
    """
    Establishes initial variables for gameplay. 
    """
    def __init__(self):
        self.players = Players()
        self.first_player = self.players.get_first_player()
        self.current_player = self.first_player
        self.first_player_name = self.players.get_first_player_name()
        self.get_first_player_type = PlayerType()
        self.get_first_player_type.set_player_type("First")
        self.first_player_type = self.get_first_player_type.player_type
        self.second_player = self.players.get_second_player()
        self.second_player_name = self.players.get_second_player_name()
        self.get_second_player_type = PlayerType()
        self.get_second_player_type.set_player_type("Second")
        self.second_player_type = self.get_second_player_type.player_type
        self.get_type = PlayerType()
        self.gameboard = Board()
        self.board = self.gameboard.new_board()
        self.moves = Moves()
        self.human = Human()
        self.bot = Bot()
        self.gameboard.full = False
        first_player_vars = [self.first_player, self.first_player_type]
        second_player_vars = [self.second_player, self.second_player_type]
        self.player_vars = [first_player_vars, second_player_vars]

    def gameplay(self):
        self.moves.winner = self.moves.check_for_win(self.board)
        self.gameboard.full = self.gameboard.board_full(self.board)
        while self.moves.winner == False and self.gameboard.full == False:
            self.gameboard.print_board()
            # Return current player type:
            self.current_player_type = self.get_type.get_player_type(self.current_player, self.player_vars)
            print(f"It is {self.current_player}'s turn.")
            if self.current_player_type == 'Human':
                self.human.play_move(self.board, self.current_player)
            elif self.current_player_type == 'Bot':
                self.bot.play_move(self.board, self.current_player)
            else:
                print('There is an error with human v. bot play logic')
            # self.moves.play_move(self.board, self.current_player)
            self.moves.winner = self.moves.check_for_win(self.board)
            if self.moves.winner == True:
                break
            self.gameboard.full = self.gameboard.board_full(self.board)
            if self.gameboard.full == True:
                break
            self.current_player = self.moves.advance_turn(self.current_player)
        if self.moves.winner == True:
            self.gameboard.print_board()
            print(f"{self.current_player} won the game!")
        elif self.gameboard.full == True:
            self.gameboard.print_board()
            print("The game resulted in a draw.")


rungame = RunGame()
rungame.gameplay()