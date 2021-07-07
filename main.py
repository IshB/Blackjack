import pydealer as pd

values_1 = {
    "Ace": 11,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

values_2 = {
    "Ace": 1,
    "King": 10,
    "Queen": 10,
    "Jack": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}


def ace_in_deck(hand):
    for card in hand:
        if card.value == "Ace":
            return True
    return False


def hand_value(hand, ace=False):
    if ace == True:
        val = 0
        for card in hand:
            val += values_2[card.value]
        return val
    else:
        val = 0
        for card in hand:
            val += values_1[card.value]
        return val


class Player:
    def __init__(self, name, chips=500):
        self.name = name
        self.player_hand = pd.Stack()
        self.player_hand_2 = pd.Stack()
        self.chips = chips
        deal = deck.deal(2)
        self.player_hand.add(deal)

    def __str__(self):
        return ('''
\n
################################
            HELLO {}        
          YOU HAVE: {} CHIPS    
################################
'''.format(self.name.upper(), self.chips))

    def hit_me(self, hand):
        dealt_cards = deck.deal(1)
        hand.add(dealt_cards)

    def player_choice_1(self, hand):
        choice = ""
        ask = input(
            """DO YOU WANT TO:

                    - h: HIT

                    - s: SPLIT (only if card value is the same)

                    - n: STAY\n""")
        if ask.upper() == "S":
            temp = self.player_hand.empty(return_cards=True)
            self.player_hand.add(temp[0])
            self.player_hand_2.add(temp[1])
            choice = "split"
        elif ask.upper() == "N":
            return "stay", hand_value(hand)
        elif ask.upper() == "H":
            self.hit_me(hand)
            print("\n CARD RECEIVED: {}".format(hand[-1]))
            print("Your current cards are:")
            for card in hand:
                print(card)
            choice = "hit"

        else:
            print("""
            #####################  PLEASE TRY AGAIN  #####################
            ############################################################## """)

        return choice, hand_value(hand)

    def player_choice_2(self, choice, hand):
        choice_2 = ""
        if choice == "stay":
            return "stay"
        else:
            ask = input(
                """DO YOU WANT TO:
    
                        - h: HIT
    
    
                        - n: STAY\n""")

            if ask.upper() == "N":
                choice_2 = "stay"
            elif ask.upper() == "H":
                self.hit_me(hand)
                print("\n CARD RECEIVED: {}".format(hand[-1]))
                print("Your current cards are:")
                for card in hand:
                    print(card)
                choice_2 = "hit"

            else:
                print("""
                #####################  PLEASE TRY AGAIN  #####################
                ############################################################## """)

        return choice_2, hand_value(hand)


class Dealer:

    def __init__(self):
        self.dealer_hand = pd.Stack()
        deal = deck.deal(2)
        self.dealer_hand.add(deal)

    def __str__(self):
        return ('''Hello I'm the dealer.
The house always wins!!''')

    def hit_me(self):

        deal_cards = deck.deal(1)
        self.dealer_hand.add(deal_cards)

    def dealer_turn(self):
        dealer_hand_var = self.dealer_hand
        hand_value(dealer_hand_var)
        while hand_value(dealer_hand_var) < 17:
            self.hit_me()

        if hand_value(dealer_hand_var) == 21:
            print("\n\n-----BLACKJACK-----")
            print("Dealers hand value is:" + str(hand_value(dealer_hand_var)))
        elif hand_value(dealer_hand_var) > 21:
            print("\n\n-----BUST-----")
            print("Dealers hand value is:" + str(hand_value(dealer_hand_var)))
        else:
            print("\n\nDealers hand value is:\n\n" + str(hand_value(dealer_hand_var)))
        print("\n\nThe dealer's cards are:\n\n")
        for card in self.dealer_hand:
            print(card)

        return hand_value(dealer_hand_var)

    def show_card(self):
        print('''
#######################################
####    DEALER'S TOP CARD IS:   ####\n''' +
              "####   " + str(self.dealer_hand[0]) + "              ####"
                                                     '''\n######################################\n'''
              )

deck = pd.Deck()
deck.shuffle()


player_name = input("\n PLEASE ENTER YOUR NAME\n")

loop = "Y"
while loop == "Y":
    deck = pd.Deck()
    deck.shuffle()
    # create player instance
    player1 = Player(player_name)
    #empty hand
    player1.player_hand.empty()
    player1.player_hand_2.empty()

    # create player instance
    player1 = Player(player_name)

    print(player1)
    print('''
    #######################################
    ####    -----PLAY GAME-----        ####
    ######################################
    ''')

    # create a dealer for this game
    dealer1 = Dealer()
    print(dealer1)


    # show the dealer's top card
    dealer1.show_card()

    # player plays now
    player_hand_vals = []
    # show player's first two cards
    print(player1.player_hand)
    player_turn = True
    choice1, hand_val = player1.player_choice_1(player1.player_hand)

    if choice1 == "hit":
        choice2 = ""
        while hand_val <= 21:
            choice2, hand_val = player1.player_choice_2(choice1, player1.player_hand)
            if choice2 == "stay":
                break

        ace = ace_in_deck(player1.player_hand)
        if hand_val>21 and ace:
            hand_val_ace = hand_value(player1.player_hand, ace = True)
            while hand_val_ace < 21:
                choice3, kachra = player1.player_choice_2(choice2, player1.player_hand)
                hand_val_ace = hand_value(player1.player_hand, ace=True)
                hand_val = hand_val_ace
                if choice3 == "stay":
                    break
        print('\n\nYour hand value is:\n\n', hand_val)
        player_hand_vals.append(hand_val)



    elif choice1 == "split":
        print("\n Playing through your first hand : {}\n".format(player1.player_hand))
        choice_s1, hand_val = player1.player_choice_2(choice1, player1.player_hand)
        if choice_s1 == "hit":
            choice2 = ""
            while hand_val <= 21:
                choice2, hand_val = player1.player_choice_2(choice1, player1.player_hand)
                if choice2 == "stay":
                    break

            ace = ace_in_deck(player1.player_hand)
            if hand_val > 21 and ace:
                hand_val_ace = hand_value(player1.player_hand, ace=True)
                while hand_val_ace < 21:
                    choice3, kachra = player1.player_choice_2(choice2, player1.player_hand)
                    hand_val_ace = hand_value(player1.player_hand, ace=True)
                    hand_val = hand_val_ace
                    if choice3 == "stay":
                        break
            print('\n\nYour hand value is:\n\n', hand_val)
            player_hand_vals.append(hand_val)

        print("\n Playing through your second hand : {}\n".format(player1.player_hand_2))
        choice_s2, hand_val = player1.player_choice_2(choice1, player1.player_hand_2)
        if choice_s2 == "hit":
            choice2 = ""
            while hand_val <= 21:
                choice2, hand_val = player1.player_choice_2(choice1, player1.player_hand_2)
                if choice2 == "stay":
                    break

            ace = ace_in_deck(player1.player_hand_2)
            if hand_val > 21 and ace:
                hand_val_ace = hand_value(player1.player_hand_2, ace=True)
                while hand_val_ace < 21:
                    choice3, kachra = player1.player_choice_2(choice2, player1.player_hand_2)
                    hand_val_ace = hand_value(player1.player_hand_2, ace=True)
                    hand_val = hand_val_ace
                    if choice3 == "stay":
                        break
            print('\n\nYour hand value is:\n\n', hand_val)
            player_hand_vals.append(hand_val)

    else:
        print("\n\nyou have chosen stay\n\n")
        player_hand_vals.append(hand_value(player1.player_hand))


    # play through the dealer's turn
    dealer_hand_val = dealer1.dealer_turn()

    #comapre hand_values
    num_of_hands = len(player_hand_vals)
    if num_of_hands == 1:
        if player_hand_vals[0]>21:
            print("\n\nloser\n\n\n")
        elif dealer_hand_val>21:
            print("\n\nwinner\n\n")

        elif dealer_hand_val == 21:
            print("\n loser \n")

        else:
            if player_hand_vals[0] > dealer_hand_val:
                print("winner")
            elif player_hand_vals[0]<dealer_hand_val:
                print("loser")
            else:
                print(" draw")
    elif num_of_hands==2:
        print("\nfor hand 1:\n")

        if player_hand_vals[0] > 21:
            print("\n\nloser\n\n\n")
        elif dealer_hand_val > 21:
            print("\n\nwinner\n\n")

        elif dealer_hand_val == 21:
            print("\n loser \n")

        else:
            if player_hand_vals[0] > dealer_hand_val:
                print("winner")
            elif player_hand_vals[0] < dealer_hand_val:
                print("loser")
            else:
                print(" draw")

        print("\nfor hand 2:\n")

        if player_hand_vals[1]>21:
            print("\n\nloser\n\n\n")
        elif dealer_hand_val>21:
            print("\n\nwinner\n\n")

        elif dealer_hand_val == 21:
            print("\n loser \n")

        else:
            if player_hand_vals[1] > dealer_hand_val:
                print("winner")
            elif player_hand_vals[1]<dealer_hand_val:
                print("loser")
            else:
                print(" draw")


    ask = input("do you wanna play again")
    if ask.upper() == "N":
        loop = "N"
print("---End---")
