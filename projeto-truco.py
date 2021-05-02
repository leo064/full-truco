import random
"""
##Rules:
- in turn, three cards per player.
- one "shackle" (manilha)

(?)create a list that "save" the 40 cards of truco.
create a function that take the cards of each turn.

list.remove --> could be utilize in moment that player play a card in table. For example, the played card go to the first position
of list, and then, is remove because it was played.

or, I create a list for each player, contained three cards in each list.
However, I think that this idea is "fail" because him don't give me total control for the cards.

"""

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
print(turn)

#tests
player1 = []
player1.append(turn[0])
player1.append(turn[1])
player1.append(turn[2])

print(player1)
player2 = turn[3],turn[4],turn[5]
player3 = turn[6],turn[7],turn[8]
player4 = turn[9],turn[10],turn[11]


    
    
    

