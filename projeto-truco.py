import random

turn_numcards = [] #<-- global list of nums, no names.
def take_turncards():
    """function to take the 12 random cards. + side card"""
    turn_cards = []
    numcard = 0
    while numcard < 13:
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
      
            if suit == 0: suit_name = 'clubs'
            elif suit == 1: suit_name = 'hearts'
            elif suit == 2: suit_name = 'spades'
            else: suit_name = 'diamonds'
            
            show = number_name, suit_name
            turn_cards.append(show)
            
    return turn_cards

turn = take_turncards()

def give_turncards():
    """'array list' (matriz) that gives the cards to respectives players"""
    p_decks = []
    first = 0
    last = 3
    for i in range(1, 5):
        player = []
        for j in range(first,last):
            player.append(turn[j])

        p_decks.append(player)

        first = last
        last+=3

    return p_decks

player_deck = give_turncards()

"""define shakle of the turn:"""
print("side is ...", turn[12]) # <--- side (last card) randomized in begin.
side = turn_numcards[12]
if side[0]+1 == 8: shackle = "Q"
elif side[0]+1 == 9: shackle = "J"
elif side[0]+1 == 10: shackle = "K"
elif side[0]+1 == 11: shakle = "A"
else: shackle = side[0]+1
print("so... THE SHACKLE IS A: ", shackle)

print(player_deck[0])
print(player_deck[1])
print(player_deck[2])
print(player_deck[3])
print()

"""define the player's turn"""
for turn_of in range (4):
    card_played = False
    while (card_played == False):
        print(player_deck[turn_of])
        card1 = player_deck[turn_of][0]
        card2 = player_deck[turn_of][1]
        card3 = player_deck[turn_of][2]
        card = input("What card you play? [1/2/3] :")
        print("player {} played: ".format(turn_of+1))
        if card == '1':
            print(card1)
        elif card == '2':
            print(card2)
        elif card == '3':
            print(card3)
        else:
            print("invalid value!, try again!")
            continue
        print()
        card_played = True



    
    
    

