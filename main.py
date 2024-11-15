import art
import random

cards = {
    'ACE': 11, 'Q': 10, 'K': 10, 'J': 10,
    1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
    8: 8, 9: 9, 10: 10,
}

available_cards = [1,2,3,4,5,6,7,8,9,10,'ACE', 'Q','K','J']


start = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
print("\n" * 100)
if start == 'n':
    exit()
print(art.logo + "\n")

# Random Card are given to both users and scores have been assigned
user_card = random.sample(available_cards, 2)
computer_card = random.sample(available_cards, 2)
user_score = 0
computer_score = 0

# Functions
def scores(card_name,card_name_score):
    for card in card_name:
        card_name_score += cards[card]
    return card_name_score

def blackjack_check(card_name_1, card_name_2):
    if 'ACE' in card_name_1 and 'ACE' in card_name_2 and (
            'Q' in card_name_1 or 'K' in card_name_1 or 'J' in card_name_1 or 10 in card_name_1) and (
            'Q' in card_name_2 or 'K' in card_name_2 or 'J' in card_name_2 or 10 in card_name_2):
        print("It's a tie!")
        return True

    if ('ACE' in card_name_1 ) and ( 'Q' in card_name_1 or 'K' in card_name_1 or 'J' in card_name_1 or 10 in card_name_1 ):
        print("\n\nYou Win! You have a Blackjack.")
        return True

    if ('ACE' in card_name_2 ) and ( 'Q' in card_name_2 or 'K' in card_name_2 or 'J' in card_name_2 or 10 in card_name_2 ):
        print(f"\n\nComputer Wins with Blackjack! Cards: {card_name_2}")
        return True

    return False

# Displayed the cards and score(s)
user_score = scores(user_card, user_score)
computer_score = scores(computer_card, computer_score)

print(f"Your cards are {user_card}")
print(f"Computers card is [{computer_card[0]}, *]")


#Checking if anyone has BLACKJACK card(ACE + 10/Q/J/K)
if blackjack_check(user_card, computer_card):
    exit()

# Main Game
while True:
    #Comparing The scores and checking if they've ace and 21+ or not
    if user_score > 21:
        if 'ACE' in user_card:
            cards['ACE'] = 1
            user_score = scores(user_card, 0)
            if user_score > 21:
                print("You lose the game!")
                break
        else:
            print("You bust! Game over.")

    if computer_score > 21:
        if 'ACE' in computer_card:
            cards['ACE'] = 1
            computer_score = scores(computer_card, 0)
            if computer_score > 21:
                print("You win the game!")
                break
        else:
            print("You win the game!")

    adding_card = str(input("Do you want to draw a card?'y' or 'n': "))
    if adding_card == 'y':
        user_card.append(random.choice(available_cards))
        user_score = scores(user_card, 0)
        print("\n" * 100)
        print(f"Your cards are {user_card}")
        print(f"Computers card is [{computer_card[0]}, *]")

    else:
        while computer_score < 17:
            computer_card.append(random.choice(available_cards))
            computer_score = scores(computer_card, 0)
            if computer_score > 21:
                print("Computer busts! You win.")
                break
        if computer_score > 21:
            break

        if computer_score == user_score:
            print("It's a tie!")
            print(f"Computers card is {computer_card} \nYour cards are {user_card}")
            break
        elif computer_score > user_score:
            print("You lose!")
            print(f"Computers card is {computer_card} \nYour cards are {user_card}")
            break
        elif computer_score < user_score:
            print("You win!")
            print(f"Your cards are {user_card}\nComputers card is {computer_card}")
            break
        else:
            print("Game error!")
            break
