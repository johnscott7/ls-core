# 1. Initialize deck
# 2. Deal cards to player and dealer
# 3. Player turn: hit or stay
#    - repeat until bust or stay
# 4. If player bust, dealer wins.
# 5. Dealer turn: hit or stay
#    - repeat until total >= 17
# 6. If dealer busts, player wins.
# 7. Compare cards and declare winner.

import random

DECK = [
    ['H', '2'], ['H', '3'], ['H', '4'], ['H', '5'], ['H', '6'], ['H', '7'],
    ['H', '8'], ['H', '9'], ['H', '10'], ['H', 'J'], ['H', 'Q'], ['H', 'K'], ['H', 'A'],
    ['D', '2'], ['D', '3'], ['D', '4'], ['D', '5'], ['D', '6'], ['D', '7'],
    ['D', '8'], ['D', '9'], ['D', '10'], ['D', 'J'], ['D', 'Q'], ['D', 'K'], ['D', 'A'],
    ['C', '2'], ['C', '3'], ['C', '4'], ['C', '5'], ['C', '6'], ['C', '7'],
    ['C', '8'], ['C', '9'], ['C', '10'], ['C', 'J'], ['C', 'Q'], ['C', 'K'], ['C', 'A'],
    ['S', '2'], ['S', '3'], ['S', '4'], ['S', '5'], ['S', '6'], ['S', '7'],
    ['S', '8'], ['S', '9'], ['S', '10'], ['S', 'J'], ['S', 'Q'], ['S', 'K'], ['S', 'A'],
]

def prompt(message):
    print(f'==> {message}')

# Deal a 'new' deck
def initialize_deck():
    current_deck = DECK.copy()
    random.shuffle(current_deck)
    return current_deck

# Calculate total value of cards in hand
def total(cards):
    total_value = 0
    aces = 0

    for card in cards:
        rank = card[1]
        if rank == 'A':
            aces += 1
            total_value += 11
        elif rank in ['K', 'Q', 'J']:
            total_value += 10
        else:
            total_value += int(rank)

    while total_value > 21 and aces > 0:
        total_value -= 10  # make one Ace count as 1 instead of 11
        aces -= 1

    return total_value

# Deal two cards
def pop_two_from_deck(deck_of_cards):
    dealt_cards = []
    dealt_cards.append(deck_of_cards.pop())
    dealt_cards.append(deck_of_cards.pop())
    return dealt_cards

# Check if value of cards in hands exceeds 21
def busted(cards):
    return total(cards) > 21

def detect_result(dealer_cards, player_cards):
    player_total = total(player_cards)
    dealer_total = total(dealer_cards)

    if player_total > 21:
        return 'dealer'
    elif dealer_total > 21:
        return 'player'    
    elif player_total > dealer_total:
        return 'player'
    if player_total < 22 and dealer_total > player_total:
        return 'dealer'
    else:
        return 'draw'

def display_results(dealer_cards, player_cards):
    result = detect_result(dealer_cards, player_cards)

    match result:
        case 'dealer':
            prompt("Sorry. You lose.")
        case 'player':
            prompt("Congratulations. That's a winning hand.")
        case 'draw':
            prompt("That's a draw. Money back.")

def play_again():
    answer = input('Do you want to play again? (y/n) ')
    return answer == 'y'

def display_hand(cards):
    clean_cards = [display_cards(card) for card in cards]

    if len(clean_cards) == 0:
        return ''
    elif len(clean_cards) == 1:
        return clean_cards[0]
    elif len(clean_cards) == 2:
        return f'{clean_cards[0]} and {clean_cards[-1]}'
    else:
        return f'{', '.join(clean_cards[:-1])} and {clean_cards[-1]}'

def display_cards(card):
    suit = card[0]
    value = card[-1]
    card_value_dict = {'A': 'Ace', 'K': 'King',
                 'Q': 'Queen', 'J': 'Jack',
                 '10': 'Ten', '9': 'Nine',
                 '8': 'Eight', '7': 'Seven',
                 '6': 'Six', '5': 'Five',
                 '4': 'Four', '3': 'Three',
                 '2': 'Two'}
    card_value = card_value_dict[value]   
    match suit:
        case 'C':
            return f'{card_value} of Clubs'
        case 'H':
            return f'{card_value} of Hearts'
        case 'D':
            return f'{card_value} of Diamonds'
        case 'S':
            return f'{card_value} of Spades'

while True:
    prompt('Welcome to Twenty-One!')

     # initial deal
    deck = initialize_deck()
    player_cards = pop_two_from_deck(deck)
    dealer_cards = pop_two_from_deck(deck)

    round_over = False

    prompt(f"Dealer has {display_cards(dealer_cards[0])} and ?")
    prompt(f"You have: {display_cards(player_cards[0])} and {display_cards(player_cards[1])}, for a total of {total(player_cards)}.")

    # player turn
    while True:
        player_choice = input("Would you like to (h)it or (s)tay? (Press h/s): ")
        if player_choice not in ['h', 's']:
            prompt("Sorry, must enter 'h' or 's'.")
            continue

        if player_choice == 'h':
            player_cards.append(deck.pop())
            prompt('You chose to hit!')
            prompt(f"Your cards are now: {display_hand(player_cards)}")
            prompt(f"Your total is now: {total(player_cards)}")

        if player_choice == 's' or busted(player_cards):
            break

    if busted(player_cards):
        round_over = True
    else:
        prompt(f"You stayed at {total(player_cards)}")

    # dealer turn
    if not round_over:
        prompt("Dealer's turn...")

        while total(dealer_cards) < 17:
            prompt("Dealer hits!")
            dealer_cards.append(deck.pop())
            prompt(f"Dealer's cards are now: {display_hand(dealer_cards)}")

        if busted(dealer_cards):
            prompt(f"Dealer total is now: {total(dealer_cards)}")
            round_over = True
        else:
            prompt(f"Dealer stays at {total(dealer_cards)}")

    # both player and dealer stays - compare cards!

    print('============')
    prompt(f"Dealer has {display_hand(dealer_cards)}, for a total of: {total(dealer_cards)}")
    prompt(f"Player has {display_hand(player_cards)}, for a total of: {total(player_cards)}")
    print('============')

    display_results(dealer_cards, player_cards)

    if not play_again():
        prompt('Thanks for playing! Come back soon.')
        break