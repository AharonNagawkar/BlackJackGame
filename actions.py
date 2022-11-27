import random


def shuffle_deck(current_cards):
    if len(current_cards) <= 52:
        cards_list = [num for num in range(1, 12) for _ in range(8)]
        for _ in range(16):
            cards_list.append(10)
        random.shuffle(cards_list)
        return cards_list
    return current_cards


def pull_card(cards):
    return cards.pop()


def black_jack(cards):
    if 11 in cards:
        return True
    else:
        return False
