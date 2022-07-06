from game_data import data
from art import logo, vs
import random
# Generate a random account from the game data.
def get_random_account() -> dict:
    return random.choice(data)
# Format account data into printable format.
def format_data(single_data: dict) -> str:
    name = single_data['name']
    description = single_data['description']
    country = single_data['country']
    return f"{name}, a {description}, from {country}."

def check_answer(guess: str, a_follwers: int, b_follwers: int) -> bool:
    if a_follwers > b_follwers:
        return guess == 'a'
    else:
        return guess == 'b'

def start_game():
    print(logo)
    score = 0
    guess_wrong = False
    item_A = get_random_account()
    item_B = get_random_account()

    while not guess_wrong:
        # switching
        item_A = item_B
        item_B = get_random_account()

        # make sure that they are not the same
        while item_A == item_B:
            account_b = get_random_account()

        follower_A = item_A['follower_count']
        follower_B = item_B['follower_count']

        print("Compare A: " + format_data(item_A) + "\n")
        print(vs)
        print("Against B: " + format_data(item_B))
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(choice, follower_A, follower_B)

        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            guess_wrong = True
            print(f"Sorry, that's wrong. Final score: {score}")

start_game()
