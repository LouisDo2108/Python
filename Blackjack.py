import random
from IPython.display import clear_output
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
suits = {"clubs", "spades", "diamonds", "hearts"}
special_cards_value = {'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Cards():

    """
    Build a standard 52 cards deck
    """

    def __init__(self, deck=[]):
        self.deck = deck
        for s in suits:
            for r in ranks:
                self.deck.append((s, r))

    # show the deck(if needed)
    def __str__(self):
        for each_card in range(0, 53):
            print(self.deck[each_card])

    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)


class Bet():

    """
    Ask for the player's balance and bet
    """

    def __init__(self, balance=100, win_bet_value=0, lose_bet_value=0):
        self.balance = balance
        self.lose_bet_value = lose_bet_value
        self.win_bet_value = win_bet_value

    # ask the player win and lose bet value
    def ask(self):
        while(self.win_bet_value <= 0):
            self.win_bet_value = int(input("Please enter your win bet value: "))
        while(self.lose_bet_value <= 0):
            self.lose_bet_value = int(input("Please enter your lose bet value: "))
        return self.win_bet_value, self.lose_bet_value


class Game_Setup():
    """
    Basic functions of the game
    """
    def __init__(self):
        pass

        # Ask if the player want to draw a card
    def hit_or_stand(self):
        """
        next or stop
        """
        hit = input("You want to hit or stand?  Answer:")
        if hit == "Y" or hit == "y":
            return True
        else:
            return False

    # return if the player is busted or not :))
    def bust_or_not(self, point):
        if point > 21:
            return True
        else:
            return False

    # Ask the player if he/she want to reveal a card from the dealer's deck
    def ask_to_show(self, dealer_deck):
        try:
            print("The dealer's available card index are: {}".format(list(range(0, len(dealer_deck)-1))))
            user_answer = int(input("Which card do you want to reveal from the dealer? "))
        except:
            print("You didn't want to reveal the dealer's card")
            print("You can still be able to reveal in your next hit")
            return -1, True
        else:
            return user_answer, False

    # Ask if the player wish to continue
    def continue_game(self, inputs):
        self.inputs = inputs
        if self.inputs == "y" or self.inputs == "Y":
            return True
        else:
            return False


class Hand(Game_Setup):

    """
    Calculate the hand of the player and the dealer.
    """

    def __init__(self, point=0, card_drawn=()):
        self.point = point
        self.card_drawn = card_drawn

    # Just draw a card
    def draw_a_card(self, deck):
        self.deck = deck
        self.card_drawn = self.deck.pop()
        return self.card_drawn

    # Get the value from the card
    def get_value(self, drawn_card):
        self.drawn_card = drawn_card
        if type(self.drawn_card[1]) == int:
            return self.drawn_card[1]
        elif self.drawn_card[1] == "Ace":
            if 21 - self.point > 10:
                return 10
            else:
                return 1
        else:
            return special_cards_value[self.drawn_card[1]]

    # Add to player's point
    def add_to_point(self, value):
        self.value = value
        self.point += self.value
        return 0

    # show the player's deck
    def show_player(self, player_deck):
        self.player_deck = player_deck
        print("Your card is {}:{}".format(self.player_deck[0][0], self.player_deck[0][1]))
        for index in range(1, len(self.player_deck)):
            print("             {}:{}".format(self.player_deck[index][0], self.player_deck[index][1]))
        print("Your current point is: {}".format(self.point))
        return

    def show_dealer(self, player_deck):
        self.player_deck = player_deck
        print("The dealer card is {}:{}".format(self.player_deck[0][0], self.player_deck[0][1]))
        for index in range(1, len(self.player_deck)):
            print("                   {}:{}".format(self.player_deck[index][0], self.player_deck[index][1]))
        print("The dealer current point is: {}".format(self.point))
        return
    # player draw a card

    def player_hit(self):
        self.add_to_point(self.get_value(self.draw_a_card(deck.deck)))
        return


def Game():
    """
    This is where the game start
    """
    # ***Setting up the game***

    # Variables declaration
    print("Use Y or y to hit or any other key to stand.")
    print("Enter the number of the card you want to reveal from the dealer, enter any other key to refuse.")
    print("Have fun ^^")
    player_deck = []
    dealer_deck = []
    deck.shuffle()
    dealer = Hand()
    player = Hand()
    stand_counter = 0
    ats = True

    # Game initialization
    player_bet = Bet()
    player_bet.ask()
    clear_output()
    dealer.player_hit()
    dealer_deck.append(dealer.card_drawn)
    player.player_hit()
    player_deck.append(player.card_drawn)
    dealer.player_hit()
    dealer_deck.append(dealer.card_drawn)
    player.player_hit()
    player_deck.append(player.card_drawn)
    player.show_player(player_deck)

    # Iteration between each player's phase
    while True:

        if player.hit_or_stand():
            stand_counter = 0
            player.player_hit()
            player_deck.append(player.card_drawn)
            clear_output()
            player.show_player(player_deck)
            if dealer.point >= 17:
                pass
            else:
                dealer.player_hit()
                dealer_deck.append(dealer.card_drawn)
        else:
            if dealer.point >= 17:
                pass
            else:
                dealer.player_hit()
                dealer_deck.append(dealer.card_drawn)
            stand_counter += 1

        while ats:
            a, ats = player.ask_to_show(dealer_deck)
            if a >= 0:
                print("The dealer's card is {}:{}".format(dealer_deck[a][0], dealer_deck[a][1]))
                break
            else:
                break
        print("Do you still want to hit?")
        if stand_counter >= 1 and dealer.point >= 17:
            print("Next phase if you still stand, we will start conclude the game!")
        if stand_counter == 2:
            break

    clear_output()
    player.show_player(player_deck)
    dealer.show_dealer(dealer_deck)

    if (dealer.bust_or_not(dealer.point) and player.bust_or_not(player.point)) or \
        dealer.point == player.point:
        print("Deuce")
    elif player.bust_or_not(player.point) and (dealer.bust_or_not(dealer.point) is False):
        print("You are busted, the dealer win.")
        player_bet.balance -= player_bet.lose_bet_value
        print("Your current balance is {}".format(player_bet.balance))
    elif dealer.bust_or_not(dealer.point) and (player.bust_or_not(player.point) is False):
        print("The dealer is busted, you win")
        player_bet.balance += player_bet.win_bet_value
        print("Your current balance is {}".format(player_bet.balance))
    elif dealer.point > player.point:
        print("The dealer win.")
        player_bet.balance -= player_bet.lose_bet_value
        print("Your current balance is {}".format(player_bet.balance))
    else:
        print("You win.")
        player_bet.balance += player_bet.win_bet_value
        print("Your current balance is {}".format(player_bet.balance))
    if player.continue_game(input("Do you want to do another round?  Answer: ")):
        clear_output()
        Game()
    else:
        return print("Thank you for your time!")


deck = Cards()
Game()
