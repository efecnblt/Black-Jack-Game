import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {calculate_score(computer_cards)}")
    if user_score == computer_score:
        return "Game draw  \U0001F91D"
    elif user_score > 21:
        return "You went over. You lose! \U0001F62D"
    elif computer_score > 21:
        return "You went over. You won! \U0001F92A"
    elif user_score > computer_score:
        return "You went over. You won! \U0001F92A"
    elif user_score < computer_score:
        return "You went over. You lose! \U0001F62D"


game_over = True
os.system("clear")

while game_over:
    choice = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    if choice == "y":
        os.system("clear")
        print(logo)
        print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"\tComputer's first card: [{computer_cards[0]}]")
        while calculate_score(computer_cards) < 17:
            computer_cards.append(deal_card())

        while True:
            get_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if get_card == "y" or get_card == "Y":
                user_cards.append(deal_card())
                if calculate_score(user_cards) < 21:
                    print(f"\tYour cards: {user_cards}, current score: {calculate_score(user_cards)}")
                    print(f"\tComputer's first card: {computer_cards[0]}")
                else:
                    break
            elif get_card == "n" or get_card == "N":
                break
            else:
                print("Please enter a valid value!")
        print(compare(calculate_score(user_cards), calculate_score(computer_cards)))
    else:
        game_over = False






