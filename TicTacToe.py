import re
import time
import random

class TicTacToe:
    def __init__(self):
        self.GameMode = 0
        self.Turn = 1
        self.board  = {
            0 : [" "," "," "],
            1 : [" "," "," "],
            2 : [" "," "," "]
        }
        self.players = {
            1: " ",
            2: " "
        }
        self.NumberOfValues = 0

    def InitializeGame(self):
        print('Welcome to Tic Tac Toe!')
        while True:
            self.SetGameMode()
            self.ResetGame()
            self.Set_Players()
            self.StartGame()
            if not self.PlayAgain():
                break
        print('Thank You for playing!')

    def SetGameMode(self):
        self.GameMode = input("Set the Game Mode (1- Single Player, 2- Multi Player): ")
        while True:
            try:
                self.GameMode = int(self.GameMode)
                if self.GameMode == 1 or self.GameMode == 2:
                    break
                else:
                    self.GameMode = input("Invalid Input!! Set the Game Mode (1- Single Player, 2- Multi Player)")
            except:
                self.GameMode = input("Invalid Input!! Set the Game Mode (1- Single Player, 2- Multi Player)")

    def ResetGame(self):
        self.board  = {
            0 : [" "," "," "],
            1 : [" "," "," "],
            2 : [" "," "," "]
        }

        self.players = {
            1: " ",
            2: " "
        }
        self.NumberOfValues = 0

    def display_board(self):
        print("\n" * 100)
        print("----------------")
        for i in range(len(self.board)):
            print(self.board[i])
        print("----------------")

    def Player_Turn(self):
        if self.GameMode == 1 and self.Turn == 2:
            while True:
                x = random.randint(0,2)
                y = random.randint(0,2)
                if self.board[int(x)][int(y)] == " ":
                    self.board[x][y] = self.players[self.Turn]
                    self.NumberOfValues += 1
                    break
        else:
            print("Player", self.Turn, "Turn, Enter the coordinates (x,y): ")
            coor = input()
            while True:
                if re.search("[0-2],[0-2]", coor): 
                    x = coor[0]; y = coor[2]
                    if self.board[int(x)][int(y)] == " ":
                        self.board[int(x)][int(y)] = self.players[self.Turn]
                        self.NumberOfValues += 1
                        break
                    else:
                        print("You Cannot play in non empty square!! Player", self.Turn, "Turn", "Enter the coordinates (x,y): ")
                        coor = input()    
                else: 
                    print("Invalid Input!! Player", self.Turn, "Turn", "Enter the coordinates (x,y): ")
                    coor = input()

    def WinCheck(self):
        if ( self.board[0][0] == self.board[0][1] == self.board[0][2] == self.players[self.Turn] or
            self.board[1][0] == self.board[1][1] == self.board[1][2] == self.players[self.Turn] or
            self.board[2][0] == self.board[2][1] == self.board[2][2] == self.players[self.Turn] or
            self.board[0][0] == self.board[1][0] == self.board[2][0] == self.players[self.Turn] or
            self.board[0][1] == self.board[1][1] == self.board[2][1] == self.players[self.Turn] or
            self.board[0][2] == self.board[1][2] == self.board[2][2] == self.players[self.Turn] or
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.players[self.Turn] or
            self.board[2][0] == self.board[1][1] == self.board[0][2] == self.players[self.Turn] ):
            print("Player", self.Turn, "Wins!!")
            return True
        elif self.NumberOfValues == 9:
            print("DRAW!!")
            return True
        else:
            return False


    def Set_Players(self):
        self.players[1] = input("Player 1: Please choose X or O: ")
        while True:
            if self.players[1] == "X" or self.players[1] == "O":
                break
            else:
                self.players[1] = input("Invalid Input!! Player 1: Please choose X or O")
        if self.players[1] == "X":
            self.players[2] = "O"
        else:
            self.players[2] = "X"
        print("Player1 is play with " + self.players[1] + " and Player2 is playing with " + self.players[2])
        # print("Game is Looding...", end="")
        # time.sleep(2)
        # print("...", end ="")
        # time.sleep(2)
        # print("...", end ="")
        # time.sleep(2)

    def StartGame(self):
        self.Turn = 1
        self.display_board()
        while True:
            self.Player_Turn()
            self.display_board()
            if self.WinCheck() == True: break
            self.Turn = 2 if self.Turn == 1 else 1
                
    def PlayAgain(self):
        Again = input("Do you wanna play again (y/n):")
        while True:
            if Again == "y" or Again == "n" or Again == "Y" or Again == "N":
                break
            else:
                Again = input("Invalid Input!! Do you wanna play again (y/n):")
        if Again == "y" or Again == "Y":
            return True
        else:
            return False


