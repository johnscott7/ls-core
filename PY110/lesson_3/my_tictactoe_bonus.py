# Tic-Tac-Toe
# 
# play = True
# While play is True:
    # Build an empty 3x3 board
    # result = None
    # While result is None:
        # display current board
        # player_choice = input("Please select a square (1-9): ")
        # Update board with player_choice
        # check for result (win/tie/ongoing)
            # Set result = 'User' or result = 'Tie' (or do not set result)
        # if result is not None:
            # break
        # computer_choice = choose a square
        # update board with computer_choice
        # check for result (win/tie/ongoing)
            # # Set result = 'Computer' or result = 'Tie' (or do not set result)    
    # Display final board    
    # If result == 'User'
        # print('User wins!')
    # If result == 'Computer'
        # print('Computer wins!')
    # If result == 'Tie'
        # print('It is a tie!')
    # play_again = input("Do you want to play again? Y/N")
    # If play_again not in ['Y', 'Yes']
        # play = False

import random

PLAYER_MARKER = 1
COMPUTER_MARKER = -1
EMPTY_SQUARE = 0

def demo_board():
    print('''
        __1__|__2__|__3__
        __4__|__5__|__6__
          7  |  8  |  9
          ''')

def empty_board():
    print('''    
        ____|____|____
        ____|____|____
            |    |  
          ''')

def display_board(game_list):
    box = ['_', '_', '_', '_', '_', '_', '_', ' ',' ', ' ']
    for idx in range(1, 10):
        if game_list[idx] == PLAYER_MARKER:
            box[idx] = 'X'
        elif game_list[idx] == COMPUTER_MARKER:
            box[idx] = 'O'          
    print(f'''
        __{box[1]}__|__{box[2]}__|__{box[3]}__
        __{box[4]}__|__{box[5]}__|__{box[6]}__
          {box[7]}  |  {box[8]}  |  {box[9]}  
          ''')

WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

def empty_squares(game_list):
    return [idx for idx, val in enumerate(game_list) if val == EMPTY_SQUARE and idx > 0]

def check_victor(game_list):
    for a, b, c in WINNING_LINES:
        square1, square2, square3 = game_list[a], game_list[b], game_list[c]
        if square1 != 0 and square1 == square2 == square3:
            return square1
    if 0 not in game_list[1:]:
        return 'Tie'
    return None

def find_at_risk_square(game_list, marker):
    for a, b, c in WINNING_LINES:
        line = [game_list[a], game_list[b], game_list[c]]
        marker_count = 0
        empty_pos = None
        for idx, value in enumerate(line):
            if value == marker:
                marker_count += 1
            elif value == EMPTY_SQUARE:
                empty_pos = idx
        if marker_count == 2 and empty_pos is not None:
            return [a, b, c][empty_pos]
    return None

def choose_computer_move(game_list, smart_prob=0.9):
    smart_move = find_at_risk_square(game_list, COMPUTER_MARKER)
    if smart_move is None:
        smart_move = find_at_risk_square(game_list, PLAYER_MARKER)
    if smart_move is None:
        smart_move = find_setup_move(game_list)
    if smart_move is not None and random.random() < smart_prob:
        return smart_move
    return random.choice(empty_squares(game_list))

def score_move(game_list, move, marker):
    game_list[move] = marker
    score = 0
    for a, b, c in WINNING_LINES:
        square1, square2, square3 = game_list[a], game_list[b], game_list[c]
        if marker == COMPUTER_MARKER:
            opponent = PLAYER_MARKER
        else:
            opponent = COMPUTER_MARKER
        if (square1 != opponent and square2 != opponent and square3 != opponent):
            count_marker = (square1 == marker) + (square2 == marker) + (square3 == marker)
            if count_marker == 2:
                score += 5
            elif count_marker == 1:
                score += 1
    game_list[move] = EMPTY_SQUARE
    return score

def find_setup_move(game_list):
    open_sq = empty_squares(game_list)
    preferred = [5, 1, 3, 7, 9, 2, 4, 6, 8]
    open_sq_sorted = [i for i in preferred if i in open_sq]
    best_move = None
    best_score = -1
    for move in open_sq_sorted:
        s = score_move(game_list, move, COMPUTER_MARKER)
        if s > best_score:
            best_score = s
            best_move = move
    return best_move

def announce_outcome(result):
    if result == PLAYER_MARKER:    
        print('You win. \n'
              'I let you win that time.')
    elif result == COMPUTER_MARKER:
        print('Computer wins!')
    elif result == 'Tie':
        print('It is a tie!') 

print("Hi. Let's play Tic Tac Toe!")
print("You will be X. I will be O.")
print('You will select board locations '
       'based on the following numbers:')
demo_board()
play = True
game_state = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
player_choice = 0
while play is True:
    print("Let's begin! \n")
    empty_board()
    result = None
    while result is None:
        while True:
            try:
                player_choice = int(input("Please select a square (1-9): "))
                if player_choice not in range(1, 10):
                    print("Please choose a number from 1 to 9.")
                elif player_choice not in empty_squares(game_state):
                    print("Try again. That square is taken.")
                else:
                    break
            except ValueError:
                print("Invalid input, please enter a number.")
        game_state[player_choice] += PLAYER_MARKER
        outcome = check_victor(game_state)
        if outcome is not None:
            result = outcome
            display_board(game_state)
            announce_outcome(result)
            break
        computer_choice = choose_computer_move(game_state, smart_prob=0.9)
        game_state[computer_choice] += COMPUTER_MARKER
        display_board(game_state)
        outcome = check_victor(game_state)
        if outcome is not None:
            result = outcome
            announce_outcome(result)
            break
    play_again = input('Do you want to play again? (y/n) ').lower()
    while play_again not in ['y', 'n', 'no', 'yes']:
        play_again = input("Please type either 'yes' or 'no': ").lower()
    if play_again not in ['y', 'yes']:
        print('Thanks for playing!')
        play = False
    else:
        game_state = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]