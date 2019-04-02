# Connect 4
import random

# This function prints out the board that it was passed.
def drawBoard(board):
# "board" is a list of 10 strings representing the board (ignore index 0)
 #print(len(board))
 #print(len(board[0]))
 for i in range(0,6):
  for j in range(0,7):
   print(' ' + board[i][j], end=' | ')
  if(i != 6):
   print('\n---------------------------------------')
 print()
 '''
 print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' ' + board[0][5] + ' | ' + board[4][5] + ' | ' + board[5][5])
 print('------------------------------------------------------------------------------------------------------------------------------')
 print(' ' + board[0,4] + ' | ' + board[1,4] + ' | ' + board[2,4] + ' ' + board[3,4] + ' | ' + board[4,4] + ' | ' + board[5,4]+ ' | ' + board[6,4])
 print('------------------------------------------------------------------------------------------------------------------------------')
 print(' ' + board[0,3] + ' | ' + board[1,3] + ' | ' + board[2,3] + ' ' + board[3,3] + ' | ' + board[4,3] + ' | ' + board[5,3]+ ' | ' + board[6,3])
 print('------------------------------------------------------------------------------------------------------------------------------')
 print(' ' + board[0,2] + ' | ' + board[1,2] + ' | ' + board[2,2] + ' ' + board[3,2] + ' | ' + board[4,2] + ' | ' + board[5,2]+ ' | ' + board[6,2])
 print('------------------------------------------------------------------------------------------------------------------------------')
 print(' ' + board[0,1] + ' | ' + board[1,1] + ' | ' + board[2,1] + ' ' + board[3,1] + ' | ' + board[4,1] + ' | ' + board[5,1]+ ' | ' + board[6,1])
 print('------------------------------------------------------------------------------------------------------------------------------')
 print(' ' + board[0,0] + ' | ' + board[1,0] + ' | ' + board[2,0] + ' ' + board[3,0] + ' | ' + board[4,0] + ' | ' + board[5,0]+ ' | ' + board[6,0])
 '''
def inputPlayerLetter():
# Lets the player type which letter they want to be.
# Returns a list with the player’s letter as the first item, and the computer's letter as the second.
 letter = ''
 while not (letter == 'X' or letter == 'O'):
  print('Do you want to be X or O?')
  letter = input().upper()
# the first element in the list is the player’s letter, the second is the computer's letter.
 if letter == 'X':
  return ['X', 'O']
 else:
  return ['O', 'X']

def whoGoesFirst():
# Randomly choose the player who goes first.
 if random.randint(0, 1) == 0:
  return 'computer'
 else:
  return 'player'

def playAgain():
# This function returns True if the player wants to play again, otherwise it returns False.
 print('Do you want to play again? (yes or no)')
 return input().lower().startswith('y')

def makeMove(board, letter, column):
 for i in range(5,-1,-1):
  if(isSpaceFree(board, i, column)):
   board[i][column] = letter
   break

def isWinner(bo, le):
# Given a board and a player’s letter, this function returns True if that player has won.
# We use bo instead of board and le instead of letter so we don’t have to type as much.
 for i in range(0,3):
  for j in range(0,7):
    if(bo[i][j] == le and bo[i+1][j] == le and bo[i+2][j] == le and bo[i+3][j] == le):
        return True
 for i in range(0, 6):
   for j in range(0, 4):
     if(bo[i][j] == le and bo[i][j+1] == le and bo[i][j+2] == le and bo[i][j+3] == le):
       return True

 for i in range(0, 3):
   for j in range(0, 4):
     if (bo[i][j] == le and bo[i+1][j+1] == le and bo[i+2][j+2] == le and bo[i+3][j+3] == le):
       return True
 for i in range(0, 3):
   for j in range(3, 7):
     if (bo[i][j] == le and bo[i-1][j-1] == le and bo[i-2][j-2] == le and bo[i-3][j-3] == le):
       return True
 return False

def getBoardCopy(board):
# Make a duplicate of the board list and return it the duplicate.
 dupeBoard = []
 for i in range(0,6):
    board_row = []
    for j in range(0,7):
        board_row.append(board[i][j])
    dupeBoard.append(board_row)
 return dupeBoard

def isSpaceFree(board, row, column):
# Return true if the passed move is free on the passed board.
 return board[row][column] == ' '

def getPlayerMove(board):
# Let the player type in their move.
 move = ' '
 while move not in '0 1 2 3 4 5 6'.split() or not isSpaceFree(board, 0,int(move)):
  print('What is your next move? (0-6)')
  move = input()
 return int(move)

def chooseRandomMoveFromList(board, movesList):
# Returns a valid move from the passed list on the passed board.
# Returns None if there is no valid move.
 possibleMoves = []
 for column in movesList:
  for row in range(5, -1, -1):
   if isSpaceFree(board, row, column):
    possibleMoves.append(column)
    break
 if len(possibleMoves) != 0:
  return random.choice(possibleMoves)
 else:
  return None

def getComputerMove(board, computerLetter):
# Given a board and the computer's letter, determine where to move and return that move.
 if computerLetter == 'X':
  playerLetter = 'O'
 else:
  playerLetter = 'X'

# Here is our algorithm for our Tic Tac Toe AI:
# First, check if we can win in the next move
 for column in range(0, 7):
  for row in range(5,-1,-1):
   copy = getBoardCopy(board)
   if isSpaceFree(copy, row, column):
    makeMove(copy, computerLetter, column)
    if isWinner(copy, computerLetter):
     return column
    break

# Check if the player could win on their next move, and block them.
 for column in range(0, 7):
  for row in range(5,-1,-1):
   copy = getBoardCopy(board)
   if isSpaceFree(copy, row, column):
    makeMove(copy, playerLetter, column)
    if isWinner(copy, playerLetter):
     return column
    break

# Try to take one of the corners, if they are free.
 move = chooseRandomMoveFromList(board, [0, 1, 2, 3, 4, 5, 6])
 if move != None:
  return move
'''
# Try to take the center, if it is free.
 if isSpaceFree(board, 5):
  return 5
# Move on one of the sides.
 return chooseRandomMoveFromList(board, [2, 4, 6, 8])
'''
def isBoardFull(board):
# Return True if every space on the board has been taken. Otherwise return False.
 for i in range(0, 7):
  if isSpaceFree(board, 0, i):
   return False
 return True

print('Welcome to Connect 4!')

while True:
# Reset the board 7lie 6hang
 #theBoard = [['Z','Z','Z','Z','Z','Z'],['Z','Z','Z','Z','Z','Z'],['Z','Z','Z','Z','Z','Z'],['Z','Z','Z','Z','Z','Z'],['Z','Z','Z','Z','Z','Z'],['Z','Z','Z','Z','Z','Z'],['Z','Z','Z','Z','Z','Z']]
 theBoard = []
 row = 6
 column = 7
 for i in range(row):
  board_row = []
  for j in range(column):
   board_row.append(' ')
  theBoard.append(board_row)
 playerLetter, computerLetter = inputPlayerLetter()
 turn = whoGoesFirst()
 print('The ' + turn + ' will go first.')
 gameIsPlaying = True

 while gameIsPlaying:
  if turn == 'player':
   # Player’s turn.
   drawBoard(theBoard)
   move = getPlayerMove(theBoard)
   makeMove(theBoard, playerLetter, move)

   if isWinner(theBoard, playerLetter):
    drawBoard(theBoard)
    print('Hooray! You have won the game!')
    gameIsPlaying = False
   else:
    if isBoardFull(theBoard):
     drawBoard(theBoard)
     print('The game is a tie!')
     break
    else:
     turn = 'computer'
  else:
 # Computer’s turn.
   move = getComputerMove(theBoard, computerLetter)
   makeMove(theBoard, computerLetter, move)

   if isWinner(theBoard, computerLetter):
    drawBoard(theBoard)
    print('The computer has beaten you! You lose.')
    gameIsPlaying = False
   else:
    if isBoardFull(theBoard):
     drawBoard(theBoard)
     print('The game is a tie!')
     break
    else:
     turn = 'player'

 if not playAgain():
  break