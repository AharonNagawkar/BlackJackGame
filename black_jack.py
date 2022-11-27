from actions import *
from art import logo

deck_cards = []


def init_game():
    player_init = []
    dealer_init = []
    player_init.append(pull_card(deck_cards))
    player_init.append(pull_card(deck_cards))
    dealer_init.append(pull_card(deck_cards))
    dealer_init.append(pull_card(deck_cards))
    return player_init, dealer_init


def player_turn(cards):
    global deck_cards
    if sum(cards) >= 21:
        return cards
    answer = input("Would you like to hit another card? y/n\n")
    while answer == 'y' and sum(cards) < 21:
        cards.append(pull_card(deck_cards))
        print(f"Your cards are: {cards}, current score: {sum(cards)}\n")
        if sum(cards) >= 21:
            return cards
        answer = input("Would you like to hit another card? y/n\n")
    return cards


def dealer_turn(cards):
    global deck_cards
    if sum(cards) >= 17:
        print(f'Dealer cards: {cards}: current score: {sum(cards)}\n')
        return cards
    while sum(cards) < 17:
        cards.append(pull_card(deck_cards))
        print(f'Dealer cards: {cards}: current score: {sum(cards)}\n')
    return cards


def play_game():
    global deck_cards
    deck_cards = shuffle_deck(deck_cards)
    player_cards, dealer_cards = init_game()
    print(f"Your cards are: {player_cards}, current score: {sum(player_cards)}\n")
    print(f"The Dealer's first card is {dealer_cards[0]}")
    player_cards = player_turn(player_cards)

    if sum(player_cards) == 21 and black_jack(player_cards):
        return player_cards, dealer_cards

    dealer_cards = dealer_turn(dealer_cards)

    if sum(deck_cards) == 21 and black_jack(dealer_cards):
        return player_cards, dealer_cards

    return player_cards, dealer_cards


def final_score(player_deck, dealer_deck):
    if sum(player_deck) == sum(dealer_deck):
        return "It's a Draw"
    elif sum(player_deck) == 21:
        if black_jack(player_deck):
            return "You WON - Black Jack"
        elif sum(dealer_deck) < 21:
            return "You won the game 😁"
    elif sum(dealer_deck) == 21:
        if black_jack(dealer_deck):
            return "You Lost- Dealer has Black Jack"
        elif sum(player_deck) < 21:
            return "You lost the game 😥"
    elif sum(player_deck) > 21:
        return "You lost 😥"
    elif sum(dealer_deck) > 21:
        return "You won 😁"
    elif sum(player_deck) > sum(dealer_deck):
        return "You won 😁"
    else:
        return "You lost 😥"


# Starting the Game:
answer_main = 'y'
while answer_main == 'y':
    print(f"{logo}\n")
    player, dealer = play_game()
    print(final_score(player, dealer))
    answer_main = input("Would you like to play Black Jack? y/n\n")
