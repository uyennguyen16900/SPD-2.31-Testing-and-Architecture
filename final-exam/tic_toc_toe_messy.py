# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html. 

import random

def drawBoard(board):
    """
    Prints out the board that it was passed.
    
            Parameters:
                    board: a list of 10 strings representing the board (ignore index 0)
    """

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def inputPlayerLetter():
    """
    Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    """
    
    # Lets the player type which letter they want to be.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    return ['O', 'X']

def whoGoesFirst():
    """Randomly choose the player who goes first."""
    if random.randint(0, 1) == 0:
        return 'computer'
    return 'player'

def playAgain():
    """Returns True if the player wants to play again, otherwise it returns False."""
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    """Enter letter to board"""
    board[move] = letter

def isWinner(bo, le):
    """
    Given a board and a player’s letter, this function returns True if that player has won.

            Parameters:
                    bo: board
                    le (string): a player's letter
    """
    win_state = [[bo[7], bo[8], bo[9]],
                 [bo[4], bo[5], bo[6]],
                 [bo[1], bo[2], bo[3]],
                 [bo[7], bo[4], bo[1]],
                 [bo[8], bo[5], bo[2]],
                 [bo[9], bo[6], bo[3]],
                 [bo[7], bo[5], bo[3]],
                 [bo[9], bo[5], bo[1]]]

    return [le, le, le] in win_state
    
def getBoardCopy(board):
    """Make a duplicate of the board list and return it the duplicate."""
    dupeBoard = []

    for item in board:
        dupeBoard.append(item)

    return dupeBoard

def isSpaceFree(board, move):
    """Return true if the passed move is free on the passed board."""
    return board[move] == ' '

def getPlayerMove(board):
    """Let the player type in their move."""
    next_move = ' '
    while next_move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(next_move)):
        print('What is your next move? (1-9)')
        next_move = input()
    return int(next_move)

def chooseRandomMoveFromList(board, movesList):
    """
    Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move.
    """
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if possibleMoves: 
        return random.choice(possibleMoves)
    return None

def getComputerMove(board, computerLe): 
    """
    Given a board and the computer's letter, determine where to move and return that move.
    """
    if computerLe == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, CELL_NUMS):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLe, i)
            if isWinner(copy, computerLe):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, CELL_NUMS):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move is not None: 
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    """
    Return True if every space on the board has been taken. Otherwise return False.
    """
    for i in range(1, CELL_NUMS):
        if isSpaceFree(board, i):
            return False
    return True

def play(theBoard, turn, letter):
    """Make a move depending on whose turn it is."""
    if turn == 'player':
        # Player’s turn.
        drawBoard(theBoard)
        move = getPlayerMove(theBoard)
    else:
        # Computer's turn
        move = getComputerMove(theBoard, letter)
    makeMove(theBoard, letter, move)

def check_current_state(theBoard, turn, letter):
    """
    Returns: 
            x (string): winner if there is one, otherwise None
            y (string): Done if there is a winner, Draw if there is a tie, otherwise Not done
    """
    if isWinner(theBoard, letter):
        if turn == 'player':
            return 'player', 'Done'
        return 'computer', 'Done'

    elif isBoardFull(theBoard):
        return None, 'Draw'
    
    return None, 'Not done'

def print_current_state(winner, state):
    """Prints the current board state."""
    if winner:
        if winner == 'player':
            print('Hooray! You have won the game!')
        else:
            print('The computer has beaten you! You lose.')
        
    if state == 'Draw':
        print('The game is a tie!')

def resetBoard():
    """Resets the board"""
    print('Welcome to Tic Tac Toe!')
    theBoard = [' '] * CELL_NUMS 
    players = inputPlayerLetter()
    turn = whoGoesFirst()
    player_index = 0
    if turn == 'player':
        letter = players[0]
    else:
        letter = players[1]
        player_index = 1
        
    print('The ' + turn + ' will go first.')
    winner = None
    while winner is None:
        play(theBoard, turn, letter)
        winner, state = check_current_state(theBoard, turn, letter)
        print_current_state(winner, state)
        if state in ('Done', 'Draw'):
            drawBoard(theBoard)
            if playAgain():
                resetBoard()
            else:
                break
        else:
            if turn == 'player':
                turn = 'computer'
            else:
                turn = 'player'
            player_index ^= 1
            letter = players[player_index]

if __name__ == "__main__":
    CELL_NUMS = 10
    resetBoard()