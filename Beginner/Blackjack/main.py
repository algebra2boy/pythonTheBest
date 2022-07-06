from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_two_cards(deck: list):
    draw_cards(deck)
    draw_cards(deck)

def draw_cards(deck: list):
    global cards
    deck.append(random.choice(cards))

def calculate_score(deck: list) -> int:
    score = 0
    for card in deck:
        score += card
    return score

def Ace_exist(deck: list) -> bool:
    for card in deck:
        if card == 11:
            return True
    return False

def display_scores(user_deck: list, computer_deck: list, final_hand: bool):
    if not final_hand:
        print(f"Your cards: {user_deck}, current score: {calculate_score(user_deck)}")
        print(f"Computer's first card: {computer_deck[0]}")
    else:  # only display when it is the end game
        print(f"Your final hand: {user_deck}, final score: {calculate_score(user_deck)}")
        print(f"Computer's final hand: {computer_deck}, final score: {calculate_score(computer_deck)}")

def continue_drawing(user_deck: list, computer_deck: list):
    draw_cards(user_deck)
    user_score = calculate_score(user_deck)
    if user_score >= 21:
        display_scores(user_deck, computer_deck, True)
    else:
        display_scores(user_deck, computer_deck, False)

def start_game():
    my_deck = []
    computer_deck = []
    # The user and computer should each get 2 random cards
    draw_two_cards(my_deck)
    draw_two_cards(computer_deck)
    display_scores(my_deck, computer_deck, False)

    # calculating each score
    user_score = calculate_score(my_deck)
    computer_score = calculate_score(computer_deck)

    # determining whether the user of computer have a blackjack (ace + 10)
    if user_score == 21:
        print("YOU HAVE A BLACKJACK!!")
        display_scores(my_deck, computer_deck, True)
        return
    elif computer_score == 21:
        print("Computer HAS A BLACKJACK!!")
        display_scores(my_deck, computer_deck, True)
        return

    if user_score > 21:
        if Ace_exist(my_deck):
            Ace_count_as_1 = user_score - 10
            if Ace_count_as_1 > 21:
                display_scores(my_deck, computer_deck, True)
                print("YOU HAVE A BUST!!")
                return
            else:
                while input("Type 'y' to get another card, type 'n' to pass:").lower() == 'y':
                    continue_drawing(my_deck, computer_deck)
        else:
            display_scores(my_deck, computer_deck, True)
            print("YOU HAVE A BUST!!")
            return
    elif user_score < 21:
        while input("Type 'y' to get another card, type 'n' to pass:").lower() == 'y':
            continue_drawing(my_deck, computer_deck)

    # Computer's Turn
    while computer_score < 17:
        draw_cards(computer_deck)
        computer_score = calculate_score(computer_deck)

    display_scores(my_deck, computer_deck, True)
    if computer_score > 21:
        print("COMPUTER HAS A BUST!")
    else:
        if computer_score > user_score:
            print("COMPUTER HAS A HIGHER SCORE THAN YOU!")
        elif computer_score < user_score:
            print("YOU HAVE A HIGHER SCORE THAN COMPUTER!")
        elif computer_score == user_score:
            print("SAME SCORE!!")

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print(logo)
    start_game()
