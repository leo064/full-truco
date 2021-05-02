import random

"""array of all cards: (matriz)"""
allcards = []
for i in range(4):  #4 suit's
    cards = []
    for j in range(1, 13):  #12 num's
        cards.append(j)
    allcards.append(cards)

"""function to take the 12 random cards."""
def take_turncards():
    turn_cards = []
    for numcard in range(1, 13):
        suit = random.randrange(1, 4)
        number = random.randrange(1, 13)
        
        if number == 10:
            number_name = "Q"
        elif number == 11:
            number_name = "J"
        elif number == 12:
            number_name = "K"
        else:
            number_name = number
        
        if suit == 0: suit_name = 'clubs'
        elif suit == 1: suit_name = 'hearts'
        elif suit == 2: suit_name = 'spades'
        else: suit_name = 'diamonds'
        
        show = suit_name, number_name
        turn_cards.append(show)
    return turn_cards
    
turn = take_turncards()
#print(turn)

"""list (matriz) that gives the cards to respectives players"""
player_array = []
first = 0
last = 3
for i in range(1, 5):
    player = []
    for j in range(first,last):
        player.append(turn[j])

    player_array.append(player)

    first = last
    last+=3

print(player_array[0])
print(player_array[1])
print(player_array[2])
print(player_array[3])


    
    
    

