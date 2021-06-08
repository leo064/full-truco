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
    """function that give the cards to respective players by slice"""
    p_decks = []
    p_decks.append(t[0:3])
    p_decks.append(t[3:6])
    p_decks.append(t[6:9])
    p_decks.append(t[9:12])
    return p_decks
print()

def give_turn_numcards(t_n):
    """function that give the cards to respective players by slice in numeric format"""
    p_decks_n = []
    p_decks_n.append(t_n[0:3])
    p_decks_n.append(t_n[3:6])
    p_decks_n.append(t_n[6:9])
    p_decks_n.append(t_n[9:12])
    return p_decks_n
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
    return shackle

all_pcards = []
def who_won(c_p, t_of, a_s, n_p):
    """function to sort the cards, smallest to biggest.
    cp = card played
    t_of = turn of
    a_s = active_shackle
    n_p = num of players    
    """
    print(c_p[0])
    if c_p == a_s:
        c_p = 14 #máx. strong.
        
    if c_p == 1:
        c_p = 11
    if c_p == 2:
        c_p = 12
    if c_p == 3:
        c_p = 13
    pcard = c_p, t_of
    all_pcards.append(pcard)

    """Bubble Sort"""
    if t_of == n_p:
        for i in range(0,3):
            for j in range(0,3):
                if (all_pcards[j] >= all_pcards[j+1]):
                    aux = all_pcards[j]
                    all_pcards[j] = all_pcards[j+1]
                    all_pcards[j+1] = aux
    
    return all_pcards

"""define players' turn"""

turn_value = 0
turn_of = 0
card_played = False
rejected_truco = False

sts = "Null"
team_points = [0, 0];
continue_match = True
continue_round = True
c_played = 0;
md = 0
while continue_match:

    if team_points[0] >= 12 or team_points[1] >= 12:
        continue_match = False
    
    print("Reiniciando ...")
    """Define the round' turn"""
    turn_numcards = [] #reinitialize the turn_numcards if round is over.
    turn = take_turncards(amount_ofcards)
    print()
    players_deck = give_turncards(turn)
    players_deck_n = give_turn_numcards(turn_numcards)
    print(players_deck[0])
    print(players_deck[1])
    print(players_deck[2])
    print(players_deck[3])
    
    print(players_deck_n[0])
    print(players_deck_n[1])
    print(players_deck_n[2])
    print(players_deck_n[3])
    
    active_shakle = take_shakleturn(turn)
    print("the SHACKLE is ...", active_shakle)
    print("")
    continue_round = True
    rejected_truco = False
    md = 0
    while continue_round:
        md+=1
        print("Round",md)
        print()
        all_played_cards = []
        
        for turn_of in range(0, num_players):
            """Define the players' turn"""
            card_isplayed = False
            sts = "Null"

            if rejected_truco == True:
                continue_round = False
                break
            
            while (card_isplayed == False):
                print()
                print("turn of... player", turn_of+1)
                print(players_deck[turn_of])
                action = int(input("What is your action? [1/2/3/4(truco)] :"))
                
                if action > 4 or action <= 0:
                    print("input a valid value, son of bitch!")
                    print(":")
                    continue
                if action == 4:
                    print("TRUUUUUUUUUUUUUUUUUUUCO WIDGEON")
                    if turn_of == 1 or turn_of == 3:
                        sts = input("Players 2 and 4, accept TRUCO? [Y/N]")
                    else:
                        sts = input("Players 1 and 3, accept TRUCO? [Y/N]")

                    if sts == "Y":
                        print("go down!")
                        turn_value = 3
                        rejected_truco = False
                    elif sts == "N":
                        card_isplayed = True
                        rejected_truco = True
                        print("we run!")
                    elif sts == "Null": continue
                    else:
                        print("invalid answer, try again!")

                else:
                    c_played = players_deck_n[turn_of][action-1]
                    print()
                    turn_cards_played = who_won(c_played, turn_of, active_shakle, num_players-1)
                    card = action
                    print("player {} played: {}".format(turn_of+1, players_deck[turn_of][card-1]))
                    rejected_truco = "Null"
                    card_isplayed = True

        print("Turn cards played: ",turn_cards_played)
                

                    



    
    
    

