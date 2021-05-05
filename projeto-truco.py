import random

num_players = int(input("How many people will play TRUCO? (maximum of 6 peoples!)"))
amount_ofcards = num_players*3

turn_numcards = [] #<-- global list of nums, no names.
def take_turncards(n):
    """function to take the random cards. + side card"""
    turn_cards = []
    numcard = 0
    while numcard < n+1:
        numcard += 1
        suit = random.randrange(0, 4)
        number = random.randrange(1, 11)
        shownum = number, suit
        if shownum in turn_numcards:
            numcard -= 1
            continue
        else:
            turn_numcards.append(shownum)
            
            if number == 8: number_name = "Q"
            elif number == 9: number_name = "J"
            elif number == 10: number_name = "K"
            else: number_name = number
      
            if suit == 0: suit_name = 'diamonds'
            elif suit == 1: suit_name = 'spades'
            elif suit == 2: suit_name = 'hearts'
            else: suit_name = 'clubs'
            
            show = number_name, suit_name
            turn_cards.append(show)
            
    return turn_cards

def give_turncards(t):
    """function that gives the cards to respectives players by list comprehension"""
    p_decks = []
    first, last = 0, 3
    for i in range(1, num_players+1):
        """add the line j of turn to p_decks"""
        p_decks.append([(t[j])for j in range(first, last)])
        first=last
        last+=3
    return p_decks

print()

def take_shakleturn(t):
    """define shakle of the turn:"""
    last = amount_ofcards
    print("side is ...", t[last]) # <--- side (last card) randomized in begin.
    side = turn_numcards[last]
    if side[0]+1 == 8: shackle = "Q"
    elif side[0]+1 == 9: shackle = "J"
    elif side[0]+1 == 10: shackle = "K"
    elif side[0]+1 == 11: shakle = "A"
    else: shackle = side[0]+1
    print("so... THE SHACKLE IS A: ", shackle)
    print("")
    return shackle

def who_won(c_played):
    """function to sort the cards, biggest to smallest."""
    return c_played

"""define the players' turn"""

turn_value = 0
turn_of = 1
card_played = False
rejected_truco = False

sts = "Null"

for md3 in range (1, 3+1):
    turn = take_turncards(amount_ofcards)
    players_deck = give_turncards(turn)
    active_shakle = take_shakleturn(turn)
    if rejected_truco == True:
        continue
    print("Round",md3)
    print()
    for turn_of in range(1, num_players+1):
        card_played = False
        while (card_played == False):
            print("turn of... player", turn_of)
            print(players_deck[turn_of-1])
            action = int(input("What is your action? [1/2/3/4(truco)] :"))
            if action > 4 or action <= 0: continue
            if action == 4:
                print("TRUUUUUUUUUUUUUUUUUUUCO WIDGEON")
                if turn_of == 1 or turn_of == 3:
                    sts = print(input("Players 2 and 4, accept TRUCO? [Y/N]"))
                else:
                    sts = print(input("Players 1 and 3, accept TRUCO? [Y/N]"))

                #useless
                if sts == "Y":
                    print("go down!")
                    turn_value = 3
                    rejected_truco = False
                elif sts == "N":
                    card_played = True
                    rejected_truco = True
                    print("we run!")
                else:
                    print("invalid answer, try again!")
                    continue
            else:
                card = action
                print("player {} played: {}".format(turn_of, players_deck[turn_of-1][card-1]))
                print()
                card_played = True



    
    
    

