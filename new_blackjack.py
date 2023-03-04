import random
import time

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
deck = [{'value': value, 'suit': suit} for suit in suits for value in values]

def shuffle_deck(deck):
    random.shuffle(deck)

def deal_cards(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

def hand_value(hand):
    values = {'Ace': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    ace_count = sum(1 for card in hand if card['value'] == 'Ace')
    total_value = sum(values[card['value']] for card in hand)
    while total_value > 21 and ace_count:
        total_value -= 10
        ace_count -= 1
    return total_value

print("Welcome to Blackjack!")

def place_bet(balance):
    prompt = f"Your balance is {balance}. How much would you like to bet? "
    for letter in prompt:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    while True:
        bet = input()
        if bet.isdigit() and int(bet) <= balance:
            return int(bet)
        print("Invalid bet amount. Please try again.")

def show_hands(player_hand, dealer_hand, hide_dealer_card):
    player_hand_str = ', '.join(card['value'] + ' of ' + card['suit'] for card in player_hand)
    dealer_hand_str = dealer_hand[0]['value'] + ' of ' + dealer_hand[0]['suit'] + ', ???' if hide_dealer_card else ', '.join(card['value'] + ' of ' + card['suit'] for card in dealer_hand)

    print("Player Hand: ", end='')
    for letter in player_hand_str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

    print("Dealer Hand: ", end='')
    for letter in dealer_hand_str:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def get_player_choice():
    while True:
        choice = input("Would you like to Hit or Stay? ").lower()
        if choice in ['hit', 'h', 'stay', 's']:
            return choice
        print("Invalid choice. Please try again.")

def play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n) ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("Invalid choice. Please try again.")

def blackjack():
    player_balance = 100
    while player_balance > 0:
        shuffle_deck(deck)
        player_bet = place_bet(player_balance)
        player_hand, dealer_hand = deal_cards(deck)
        show_hands(player_hand, dealer_hand, True)
        while True:
            choice = get_player_choice()
            if choice in ['hit', 'h']:
                player_hand.append(deck.pop())
                show_hands(player_hand, dealer_hand, True)
                if hand_value(player_hand) > 21:
                    print("Player busts. Dealer wins.")
                    player_balance -= player_bet
                    break
            else:
                while hand_value(dealer_hand) < 17:
                    dealer_hand.append(deck.pop())
                    show_hands(player_hand, dealer_hand, False)
                    if hand_value(dealer_hand) > 21:
                        print("Dealer busts. Player wins.")
                        player_balance += player_bet
                        break
                else:
                    if hand_value(player_hand) > hand_value(dealer_hand):
                        print("Player wins.")
                        player_balance += player_bet
                    elif hand_value(player_hand) < hand_value(dealer_hand):
                        print("Dealer wins.")
                        player_balance -= player_bet
                    else:
                        print("Push.")
                break
        if not play_again():
            break
    print("Thanks for playing!")

blackjack()