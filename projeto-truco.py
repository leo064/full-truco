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
print(turn)
print("")

"""'array list' (matriz) that gives the cards to respectives players"""
player_deck = []
first = 0
last = 3
for i in range(1, 5):
    player = []
    for j in range(first,last):
        player.append(turn[j])

    player_deck.append(player)

    first = last
    last+=3

"""
print(player_deck[0])
print(player_deck[1])
print(player_deck[2])
print(player_deck[3])
"""
side = turn_numcards[12]
print("side is ...", turn[12])

if side[0]+1 == 8: shackle = "Q"
elif side[0]+1 == 9: shackle = "J"
elif side[0]+1 == 10: shackle = "K"
else: shackle = side[0]+1
print("so... THE SHACKLE IS A: ", shackle)


    
    
    

