from random import randint
class Board:
    def __init__(self, r):
        self.board = [] 
        for i in range(r):
            self.board.append(["O", "O", "O", "O", "O", "O"])

    def printBoard(self):
        for i in range(len(self.board)):
            print(" ".join(self.board[i]))

    def randomRow(self):
        self.row =  randint(0, 4)
        return self.row

    def randomCol(self):
        self.col =  randint(0, 4)
        return self.col

    def setHidden(self):
        self.row = self.randomRow()
        self.col = self.randomCol()
        self.hiddenPos = [self.row, self.col]

class Player:
    def __init__(self):
        self.chosen = []
        self.turn = 0
    
    def turnCounter(self):
        self.turn += 1

    def choose(self):
        self.turnCounter()
        self.chosenRow = int(input("Enter a row: "))
        self.chosenCol = int(input("Enter a column: "))
        self.passedRow = self.chosenRow
        self.passedCol = self.chosenCol

        if (self.chosenRow >= 5 and self.chosenCol >= 5):
            self.chosenPos = [-1, -1]
        else:
            self.chosenPos = [self.passedRow, self.passedCol]

def play():
    guesser.choose()
    if (guesser.turn == 4):
        print("You've lost, 4/4 guesses used.")
    elif (guesser.chosenPos == game.hiddenPos):
        print("You sank the ship. You win!")
    elif(guesser.passedRow >= 5 and guesser.passedCol >= 5):
        print("Your target position were off the board. No targets hit.")
        game.printBoard()
        play()
    else:
        print("Guesser missed! Guess again.")
        #game.board[guesser.chosenRow][guesser.chosenCol] = "X"
        game.board[guesser.passedRow][guesser.passedCol] = "X"
        game.printBoard()
        play()
        #guesser.choose()

game = Board(5)
game.setHidden()

guesser = Player()

print("Hidden position... ", game.hiddenPos)
play()
