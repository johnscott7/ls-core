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


def pop_two_from_deck(deck_of_cards):
    dealt_cards = []
    dealt_cards.append(deck_of_cards.pop())
    dealt_cards.append(deck_of_cards.pop())
    return dealt_cards

# Deal a 'new' deck
def initialize_deck():
    current_deck = DECK.copy()
    random.shuffle(current_deck)
    return current_deck

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

deck = initialize_deck()
player_cards = pop_two_from_deck(deck)
print(player_cards)

# print(f"Dealer has {dealer_cards[0]} and ?")
print(f"You have: {player_cards[0]} and {player_cards[1]}, for a total of {total(player_cards)}.")