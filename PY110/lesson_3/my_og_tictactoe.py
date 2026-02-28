# Tic-Tac-Toe
# Final implementation

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
        if game_list[idx] == 1:
            box[idx] = 'X'
        elif game_list[idx] == -1:
            box[idx] = 'O'          
    print(f'''
        __{box[1]}__|__{box[2]}__|__{box[3]}__
        __{box[4]}__|__{box[5]}__|__{box[6]}__
          {box[7]}  |  {box[8]}  |  {box[9]}  
          ''')

def check_victor(game_list):
    if game_list[1] == 1:
        if game_list[2] == 1 and game_list[3] == 1:
            return 1
        if game_list[4] == 1 and game_list[7] == 1:
            return 1
        if game_list[5] == 1 and game_list[9] == 1:
            return 1
    if game_list[1] == -1:
        if game_list[2] == -1 and game_list[3] == -1:
            return -1
        if game_list[4] == -1 and game_list[7] == -1:
            return -1
        if game_list[5] == -1 and game_list[9] == -1:
            return -1
    if game_list[5] == 1:
        if game_list[2] == 1 and game_list[8] == 1:
            return 1
        if game_list[4] == 1 and game_list[6] == 1:
            return 1
        if game_list[3] == 1 and game_list[7] == 1:
            return 1
    if game_list[5] == -1:
        if game_list[2] == -1 and game_list[8] == -1:
            return -1
        if game_list[4] == -1 and game_list[6] == -1:
            return -1
        if game_list[3] == -1 and game_list[7] == -1:
            return -1
    if game_list[6] == 1:
        if game_list[3] == 1 and game_list[9] == 1:
            return 1
        if game_list[4] == 1 and game_list[5] == 1:
            return 1
    if game_list[6] == -1:
        if game_list[3] == -1 and game_list[9] == -1:
            return -1
        if game_list[4] == -1 and game_list[5] == -1:
            return -1
    if game_list[7] == 1 and game_list[8] == 1 and game_list[9] == 1:
        return 1
    if game_list[7] == -1 and game_list[8] == -1 and game_list[9] == -1:
        return -1
    if 0 not in game_list[1:]:
        return 'Tie'
    else:
        return None

def announce_outcome(result):
    if result == 1:    
        print('You win. \n'
              'I let you win that time.')
    elif result == -1:
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
        player_choice = 0
        while player_choice == 0:
            try:
                player_choice = int(input("Please select a square (1-9): "))
                if player_choice not in range(1, 10):
                    print("Please choose a number from 1 to 9.")
                    continue
                break
            except ValueError:
                print("Invalid input, please try again.")      
        game_state[player_choice] += 1
        while game_state[player_choice] in [2, 0]:
            game_state[player_choice] -= 1
            player_choice = int(input("Try again. That square is taken: "))
            game_state[player_choice] += 1
        outcome = check_victor(game_state)
        if outcome is not None:
            result = outcome
            display_board(game_state)
            announce_outcome(result)
            break
        computer_choice = random.randint(1, 9)
        game_state[computer_choice] -= 1
        while game_state[computer_choice] in [-2, 0]:
            game_state[computer_choice] += 1
            computer_choice = random.randint(1, 9)
            game_state[computer_choice] -= 1
        display_board(game_state)
        outcome = check_victor(game_state)
        if outcome is not None:
            result = outcome
            announce_outcome(result)
            break
    play_again = input('Do you want to play again? (y/n) ')
    while play_again.lower() not in ['y', 'n', 'no', 'yes']:
          play_again = input("Please type either 'yes' or 'no': ")  
    if play_again not in ['Y', 'y', 'yes']:
        print('Thanks for playing!')
        play = False
    else:
        game_state = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]