#create a board
# from IPython.display import clear_output # can only work with Jupyter Notebook

import random
from random import randint

def game_board(board):
  #clear_output()
  print('*******  CONNECT FOUR  *******\n')
  print(f'  1   2   3   4   5   6   7  ')
  print(f'| {board[1]} | {board[2]} | {board[3]} | {board[4]} | {board[5]} | {board[6]} | {board[7]} |')
  print('-----------------------------')
  print(f'  8   9  10  11  12  13  14  ')
  print(f'| {board[8]} | {board[9]} | {board[10]} | {board[11]} | {board[12]} | {board[13]} | {board[14]} |')
  print('-----------------------------')
  print(f' 15  16  17  18  19  20  21  ')
  print(f'| {board[15]} | {board[16]} | {board[17]} | {board[18]} | {board[19]} | {board[20]} | {board[21]} |')
  print('-----------------------------')
  print(f' 22  23  24  25  26  27  28  ')
  print(f'| {board[22]} | {board[23]} | {board[24]} | {board[25]} | {board[26]} | {board[27]} | {board[28]} |')
  print('-----------------------------')
  print(f' 29  30  31  32  33  34  35  ')
  print(f'| {board[29]} | {board[30]} | {board[31]} | {board[32]} | {board[33]} | {board[34]} | {board[35]} |')
  print('-----------------------------')
  print(f' 36  37  38  39  40  41  42  ')
  print(f'| {board[36]} | {board[37]} | {board[38]} | {board[39]} | {board[40]} | {board[41]} | {board[42]} |')
  print('-----------------------------')

# test the board
# board = [' '] * 43
# board[22] = 'O'
# board[23] = 'O'
# board[24] = 'O'
# board[25] = 'O'
# game_board(board)

# choose Symbol

def choose_symbol():
  symbol = 'hey'
  while symbol not in ['X','O']:
    symbol = input('Enter X or O\t').upper()
    if symbol not in ['X','O']:
      print('Choose only X or O')
  else:
    if symbol == 'X':
      return ('X','O')
    else:
      return ('O','X')

# choose_symbol()

# choose player

def choose_player():
  player = randint(1,2)
  if player == 1:
    return 'Player 1'
  else:
    return 'Player 2'


def choose_players(player1, player2):
  players = [player1, player2]
  return random.choice(players)

# choose_player()

# check if position if full

def check_position(board, position):
  if board[position] == ' ':
    return True
  else:
    return False

# check if board is full
 
def board_full(board):
  for i in range(1,43):
    if board[i] == ' ':
    #   return True
    # else:
    #   return False
      return False
  else:
    return True

# board_full(board)

# choose board position

def player_position(board):
  position = 0
  while position not in range(1,43) or not check_position(board, position):
    position = int(input('Enter the position between 1 and 42\t'))

  return position

# player_position(board)

# place market function

def place_marker(board, position, symbol):
  board[position] = symbol

# place_marker(board, 31, 'O')

# game_board(board)

# win check

def win_check(board, symbol):
  # Horizontal 1st row
  # flag = 0
  for i in range(1,40):
    if board[i] == symbol and board[i+1] == symbol and board[i+2] == symbol and board[i+3] == symbol:
      # flag = 1 # Horizontal check true set flag to 1
      return True

  #if flag == 0:
  #else:  
  for i in range(1,22):
    if board[i] == symbol and board[i+7] == symbol and board[i+7*2] == symbol and board[i+7*3] == symbol:
      return True

  return False

# win_check(board, 'O')

# replay game

def replay():
  option = ''
  while option not in ['y','n']:
    option = input('Do you want to play again? Enter Y or N\t')

  else:  
    if option[0].lower() == 'y':
      return True
    else:
      return False

# replay()

# # game creation
# print('INSTRUCTIONS: The Symbols are to be placed from bottom to top on the board\n')
# print('i.e. starting from the last row towards the top\n')
# print('******* Game Begins *******\n')

# while True:
#   #create the game board
#   board = [' '] * 43
#   game_board(board) # display the board
#   player1_marker, player2_marker = choose_symbol()

#   # choose who plays first
#   player_turn = choose_player()
#   print(f'Player 1 --> {player1_marker}')
#   print(f'Player 2 --> {player2_marker}')
#   print(f'{player_turn} plays first')

#   is_game_running = input('Do you want to continue?\t')
#   if is_game_running[0].upper() == 'Y':
#     is_game_running = True
#   else:
#     is_game_running = False

#   while is_game_running:
#     if player_turn == 'Player 1':
#       play_position = player_position(board)
#       place_marker(board, play_position, player1_marker)
#       game_board(board) #display board

#       if win_check(board, player1_marker):
#         game_board(board)
#         print(f'Congratulations! {player_turn}, you won!')
#         print('Well played both')
#         is_game_running = False

#       else:
#         if board_full(board):
#           print('Awww Snap!, it is a tie!')
#           game_board(board)
#           break
          
#         else:
#           player_turn = 'Player 2'
              
#     else:
#       play_position = player_position(board)
#       place_marker(board, play_position, player2_marker)
#       game_board(board) #display board

#       if win_check(board, player2_marker):
#         game_board(board)
#         print(f'Congratulations! {player_turn}, you won!')
#         print('Well played both')
#         is_game_running = False

#       else:
#         if board_full(board):
#           print('Awww Snap!, it is a tie!')
#           game_board(board)
#           break
          
#         else:
#           player_turn = 'Player 1'

#   if not replay():
#     break


# Game creation with player names
 
print('INSTRUCTIONS: The Symbols are to be placed from bottom to top on the board\n')
print('i.e. starting from the last row towards the top\n')
print('******* Game Begins *******\n')
 
while True:
  #create the game board
  board = [' '] * 43
  #game_board(board) # display the board
 
  #create players
  player1 = input('Player1, Enter your name\t\n')
  player2 = input('Player2, Enter your name\t\n')
  
  #assign symbol
  player1_marker, player2_marker = choose_symbol()
 
  # choose who plays first
  player_turn = choose_players(player1, player2)
  print(f'{player1} --> {player1_marker}')
  print(f'{player2} --> {player2_marker}')
  print(f'{player_turn} plays first')
 
  is_game_running = input('Do you want to continue?\t')
  if is_game_running[0].upper() == 'Y':
    is_game_running = True
  else:
    is_game_running = False
 
  while is_game_running:
    if player_turn == player1:
      game_board(board)
      print(f'{player1} your turn') 
      play_position = player_position(board)
      place_marker(board, play_position, player1_marker)
      game_board(board) #display board
 
      if win_check(board, player1_marker):
        game_board(board)
        print(f'Congratulations! {player_turn}, you won!')
        print('Well played both')
        is_game_running = False
 
      else:
        if board_full(board):
          print('Awww Snap!, it is a tie!')
          game_board(board)
          break
          
        else:
          player_turn = player2
              
    else:
      game_board(board)
      print(f'{player2} your turn')
      play_position = player_position(board)
      place_marker(board, play_position, player2_marker)
      game_board(board) #display board
 
      if win_check(board, player2_marker):
        game_board(board)
        print(f'Congratulations! {player_turn}, you won!')
        print('Well played both')
        is_game_running = False
 
      else:
        if board_full(board):
          print('Awww Snap!, it is a tie!')
          game_board(board)
          break
          
        else:
          player_turn = player1
 
  if not replay():
    break