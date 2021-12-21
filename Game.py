from TicTacToe import TicTacToe

print("Choose the game to play: \n 1- TicTacToe")
GameChoice = input()
if int(GameChoice) == 1:
    Game = TicTacToe()
    Game.InitializeGame()
