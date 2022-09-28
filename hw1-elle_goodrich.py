# CS1210 Homework1
#
# This file should contain only your own work; there are no partners
# assigned or permitted for Homework assignments.
#
# I certify that the entirety of this file contains only my own work.
# I have not shared the contents of this file with anyone in any form,
# nor have I obtained or included code from any other source aside
# from the code contained in the original homework template file.
from random import randint
from string import printable

######################################################################
# Edit the following function definition so it returns a tuple
# containing a single string, your hawkid.
#
# THE AUTOGRADER WILL FAIL TO ASSIGN A GRADE IF YOUR HAWKID IS NOT
# PROPERLY INCLUDED IN THIS FUNCTION. CAVEAT EMPTOR.
######################################################################
def hawkid():
    return(["eggoodrich"])

######################################################################
# createDeck(ncards, suits) takes an integer, ncards, and a sequence,
# suits, and produces a new, cannonically ordered, ncards*len(suits)
# card deck, where the standard deck would have ncards=13 and the four
# default suits. Note that suits can be any sequence type, including a
# string, tuple, or list.
#
# A deck is implemented as a list of cards: each card is a tuple, (v,
# s), where 0 < v <= ncards is the (integer) value of the card and s
# is the (string) suit of the card. The list representing the new deck
# is returned in the cannonical order (that is, ordered by suit, and
# within suit by card value).
#
# Example:
#   >>> createDeck(3)
#   [(1, '♠'), (2, '♠'), (3, '♠'), (1, '♡'), (2, '♡'), (3, '♡'), (1, '♢'), (2, '♢'), (3, '♢'), (1, '♣'), (2, '♣'), (3, '♣')]
#   >>> createDeck(1, 'AB')
#   [(1, 'A'), (1, 'B')]
#   >>> createDeck(4, 'A')
#   [(1, 'A'), (2, 'A'), (3, 'A'), (4, 'A')]
# The deck is always returned in cannonical order, defined above.
#
# Note: use a comprehension.
#
def createDeck(ncards=13, suits=('\u2660','\u2661','\u2662','\u2663')):
    return(tuple([(x, y) for y in suits for x in range(1,ncards+1)]))
    

######################################################################
# scramble(D) takes a list, D, and modifies it to shuffle the order of
# the elements. There is a significant literature on constructing "fair"
# shuffles of a sequence; what we are after here is simple to
# implement but may not be entirely fair (for an example of a fair
# shuffling algorithm, see the Fisher-Yates-Knuth algorithm).
#
# scramble(D) steps through the input list starting with the last
# element and moving down. At each step, it randomly swaps the current
# element with itself (no change) or one of the elements that
# currently preceeds it in D. So, for example, on the third iteration,
# it randomly swaps element -3 with any element starting form 0 up to
# and including -3. The algorithm terminates after one downward sweep
# of the list, and returns the modified list. It should be obvious
# that the list we are likely to be scrambling in this homework is a
# deck from createDeck().
#
# Your code will need to use the randint() function, which has been
# imported for you from the random module at the top of this file
# (careful! unlike most Python functions, this function uses "inclusive"
# indexing: check the Python documentation).
#
# Note: you must modify D, not create new structure.
#
def scramble(D):
    D = list(D)
    for i in reversed(D):
        a = randint(0, ((len(D))-(len(D)-D.index(i)-1)-1))
        b = D[a]
        c = D.index(i)
        D[a] = D[c]
        D[c] = b
    return(D)



######################################################################
# dealTables(sizes, deck) takes a list of sizes and a deck (such as
# one constructed by createDeck() and shuffled by scramlble()) and
# returns a new list of lists, where the length of each sublist is the
# same as the corresponding integer element of size. You should "deal"
# these representations by taking cards destructively from the deck
# and placing them in the appropriate sublist, or "table" in Trash
# terms.
#
# Since the input deck has been shuffled, it doesn't matter how you
# choose to deal the cards. You may choose to deal all of one player's
# table to their corresponding list at once, or you may choose to deal
# to each player in turn as is commonly done when playing cards. Do
# whatever is easier, remembering that as the game progresses, players
# will be dealt different numbers of cards on their respective tables.
#
# Note: Your code must destructively alter the deck to ensure no
# card is dealt to more than one person.
#
def dealTables(sizes, deck):
    t = []
    t2 = []
    for i in sizes:
        for j in range(0,i):
            t += [[False, deck[0][-1]]]
            del deck[0][-1]
        t2 += [t]
        t = []
    return(t2)

######################################################################
# unfilledTable(T) returns True if there are any unfilled slots in
# table T. Recall unfilled slots are slots where the card is facing
# down, that is, has not been revealed. Returns True or False.
#
# Example:
#   >>> unfilled([[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]])
#   True
#   >>> unfilled([[True, (1, 'C')], [True, (2, 'C')], [True, (3, 'B')]])
#   False
#
def unfilled(T):
    return(bool([x for x in T if False in x]))

######################################################################
# displayCard(c) returns the representation of a given card suitable
# for printing.
#
# Example:
# >>> displayCard((11, 'C'))
# 'C11'
# >>> displayCard((3, 'B'))
# 'B3'
#
# Note: the order in the printed representation is reversed with
# respect to the order in the underlying tuple.
#
def displayCard(c):
    return(str(c[1]+str(c[0])))

######################################################################
# showTable(T) takes a list, T, representing some player's "table"
# (the cards laid out before him/her) and returns the printed
# representation as a string. Internally, a table is represented as a
# list of lists, where the length of the list corresponds to the size
# of the table, and the elements of the list (which are, themseleves,
# also lists) consist of two values, a Boolean (True if facing up,
# False if facing down) and a card (a tuple).
#
# So, a 3-element table with only the second element showing might
# look like:
#   [[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]]
# and we want the returned value to look like:
#   '  1[ ] 2[C2] 3[ ]'
# note the spaces, including the leading spaces, and the blanks for
# locations where cards that are "hidden" (i.e., have False as their
# first value).
#
# Here, we will make use of a "hidden helper function" showEntry(S)
# that takes a table location (again, a list of a Boolean and a card)
# and returns either a blank character (if the Boolean is False) or a
# string representing the card at that location (if the Boolean is
# True).
#
def showTable(T):
    x = []
    def showEntry(E):
        if E[0] != True:
            E = '[ ]'
        else:
            E = '[' + str(displayCard(E[1])) + ']'
        return(E)
    for i in T:
        x += (' ' + str(T.index(i)+1)+str(showEntry(i)))
        x = ''.join(x)
    return(str(x))


######################################################################
# showScores(nplayers, S) takes nplayers, an integer, and S, a list of
# integer values representing the current score in the game, and
# produces a string suitable for printing that represents the current state.
#
# For example:
#    >>> showScores(3, [10, 44, 13])
#    '1:10, 2:44, 3:13'
#    >>> showScores(4, [10, 44, 13, 0])
#    '1:10, 2:44, 3:13, 4:0'
# Pay close attention to the spacing and punctuation.
#
# Note: you will need to use a comprehension.
# 
def showScores(nplayers, S):
    return(', '.join(([str([b for b in range(1,nplayers+1)][z])+ ':' + str([a for a in S][z]) for z in range(nplayers)])))

######################################################################
# playTurn(c, T) takes a card, c, and applies it to the specified
# table, T, returning the last unplayed card.
#
# Recall that in Trash, a turn involves drawing a card, and then using
# it to replace hidden cards on the table. The hidden cards are then,
# in turn, used to represent other hidden cards until no more
# replacements can be made. At this point, the last unplayed card is
# discarded.
#
# playTurn(C, T) should continue to place cards on the table as long
# as the cards remain playable. This inolves (i) making modifications
# to T (destructive operations) to reflect a card being placed and the
# fact that it is now face up, as well as printing out messages
# describing the turn as it unfolds.
#
# Example:
#   >>> playTurn((3, 'B'), [[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]])
#   Playing B3 on location 3
#   Playing C1 on location 1
#   Discarding A3
#   1[C1] 2[C2] 3[B3]
#   (3, 'A')
# where the last (3, 'A') is the value returned and correponds to the
# card to be added to the discard pile.
#
# Note that, after this turn, the player's table will have been
# modified to read:
#   [[True, (1, 'C')], [True, (2, 'C')], [True, (3, 'B')]
#

def playTurn(c, T):
    if len(c) == 1:
        c = (c[0][0],c[0][1])
        print(c)
    else:
        c = (c[0],c[1])
    c = list([True, c])
    print(c[1][0])
    if (c[1][0]) <= len(T):       
        if True in T[(c[1][0])-1]:
            print("Discarding " + displayCard(c[1]))
        else:

            while False in T[(c[1][0])-1]:
               b = T[c[1][0]-1]
               x = T.index(b)
               print('Playing ' + displayCard(c[1]) + ' on location ' + str(x+1))
               T[(c[1][0])-1] = c
               c = b
               c[0] = True 
               if (c[1][0]) > len(T):
                   break
            print("Discarding " + displayCard(c[1]))
            
    else:
        print("Discarding " + displayCard(c[1]))
    print(showTable(T))
    discard = c[1]
    print(discard)
    return(discard)

        
######################################################################
# drawCard(deck, discard, size, T) is the function that actually makes
# the only decision a player needs to make: whether to draw from the
# deck or the discard pile. The arguments to drawCard() are deck, a
# list representing the remaining cards; discard, a list representing
# the discard pile; size, an integer representing the size of the
# (implicit) player's table; and T, a list representing the player's
# table's state (see playTurn() or showTable() for details).
#
# The decision is simple. If the last card in the discard pile can be
# played on table T (meaning the corrsponding location in T is a
# hidden card), then draw from the discard pile. Otherwise, draw from
# the deck. Your function should modify either the discard list or the
# deck list and it should return the corresponding card drawn from
# whichever of these is modified.
#
# Example:
#    >>> drawCard([(2, 'A'), (4, 'A'), (2, 'C')], [(1, 'A'), (5, 'C'), (3, 'B')], 3, [[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]])
#    Drawing B3 from discard
#    (3, 'B')
# where the (3, 'B') is the value returned, and the printed message is
# meant to inform the player of how the game is evolving. Note that
# in this case, the discard pile has been modified to yield:
#    [(1, 'A'), (5, 'C')]
# Another example:
#    >>> drawCard([(2, 'A'), (4, 'A'), (2, 'C')], [(1, 'A'), (5, 'C'), (2, 'B')], 3, [[False, (3, 'A')], [True, (2, 'C')], [False, (1, 'C')]])
#    Drawing C2 from deck
#    (2, 'C')
# Here, the deck is modified to yield:
#    [(2, 'A'), (4, 'A')]
# in both cases, cards are drawn from the end of the list.
#
def drawCard(deck, discard, size, T):
    discard = list(discard)

    if len(discard) == 0 or discard[-1][0] >= len(T[0]):
        b = deck[0][-1]
        print("Drawing " + displayCard(b) + " from deck.")
        deck = deck[0][:-1]
        return (b)
    elif ((discard[-1][0])-1) <= len(T[0]):
        print("elif")
        if True in T[(discard[-1][0])-1]:
            b = deck[0][-1]
            print("Drawing " + displayCard(b) + " from deck.")
            deck = deck[0][:-1]
            return(b)
        else:
            b = deck[0][-1]
            print("Drawing " + displayCard(b) + " from deck.")
            deck = deck[0][:-1]
            return (b)
    else:
        print('else')
        b = discard[-1]
        print("Drawing " + displayCard(b) + " from discard.")
        discard = discard[:-1]
        return(b)


######################################################################
# newGame(nplayers, nrounds) creates and returns a dictionary that is
# used to hold the state of the game. The game playing engine modifies
# the dictionary to reflect how 
# The dictionary initially has seven key/value pairs:
#   nplayers = integer number of players (from signature)
#   sizes = list of integer table sizes, initially all nrounds (from signature)
#   scores = list of integer scores, one per player, initially all 0
#   suits = integer number of suits in the deck, set to nplayers+2
#   cardinality = integer number of cards per suit, set to nrounds+3
#   round = an integer round counter, initially 1
#   current = a random integer 0 <= current < nplayers, indicating starting player.
#
# Example:
#   >>> newGame(1, 3)
#   {'nplayers': 1, 'round': 1, 'scores': [0], 'sizes': [3], 'suits': 3, 'cardinality': 6, 'current': 0}
#   >>> newGame(3, 4)
#   {'nplayers': 3, 'round': 1, 'scores': [0, 0, 0], 'sizes': [4, 4, 4], 'suits': 5, 'cardinality': 7, 'current': 1}
#
# You will be adding additional key/value pairs to this dictionary later.
# 
def newGame(nplayers, nrounds):
    dict = {'nplayers': nplayers, 'round': 1, 'scores': [0]*nplayers, 'sizes':[nrounds]*nplayers, 'suits':nplayers+2, 'cardinality':nrounds+3, 'current':randint(0,nplayers-1)}
    return(dict)

######################################################################
# viewGame(G, i) takes a game description G (a dictionary of the type
# produced by newGame()) and an integer player index i and returns a
# string that, when printed, describes the state of the game from
# player i's perspective.
#
# Example:
#   >>> viewGame(G, 1)
#   '\nPlayer2 to play (score=0):\n  1[ ] 2[ ] 3[ ]'
#
# Note the spacing and explicit newlines, and the fact that the player
# numbers use 1-based indexing even though internally the game data
# structures use Pythonic 0-based indexing.
#
def viewGame(G, i):
    return('Player' + str((i+1)) + ' to play (score=' + str(G['scores'][i])  +')')

######################################################################
# Plays the game until a winner emerges. By default, generates a new
# game with all default values for, e.g., deck size and suits.
#
# Here, the code is provided for you, with a few missing elements
# described with the FIXME: comment.
#
def play(nplayers=1, nrounds=5):
    
    # Create and initialize the game.
    G=newGame(nplayers, nrounds)
    # Print out a banner so everyone knows which player is to begin.
    print('Player{} will start the game.\n'.format(G['current']+1))

    # This is the "outer loop." It will keep looping which there is no
    # player who has managed to work the size of their table down to
    # 0, which can only happen if they win nrounds number of
    # rounds. When a player hits 0 size for the next round, the game
    # ends, and that player is declared the winner.
    while 0 not in G['sizes']:
        # Announce the new round. Remember, rounds are 1-indexed
        # because they are just counters used to tell the world what's
        # going on. This value is never used to index another data
        # structure!
        print('Round{}:'.format(G['round']))

        # Each round also starts with an empty discard pile.
        G['discard'] = []
        # FIXME: Each round starts with a freshly scrambled
        # deck. Because the number of suits may exceed 4, you can't
        # use the default value of suits which gives the traditional
        # hearts, spades, etc. Instead, know that printable[36:52] is
        # the string 'ABCDE...Z', a portion of which will do fine as
        # artificial suits.
        G['deck'] = [scramble(createDeck(nrounds + 3, printable[36:(36+nplayers+2)]))]
        # FIXME: Each round starts with a fresh set of tables of
        # appropriate size and from the deck just created.
        G['tables'] = dealTables(G['sizes'], G['deck'])

        # This is the "inner loop." One time through the loop
        # corresponds to an entire round. It's an infinite loop, which
        # can only be exited explicitly, which only occurs when a
        # player has filled or completed his/her table with cards
        # facing up.
        while True:
            # FIXME: print out a representation of the game from the
            # perspective of the current player.
            print(viewGame(G, G['current']))

            # Next, draw a card for the current player, play it, and
            # append the player's discarded card to the discard pile.
            card = [drawCard(G['deck'], G['discard'], G['sizes'][G['current']], G['tables'][G['current']])]
            del G['deck'][0][-1]
            G['discard'].append(playTurn(card,G['tables'][G['current']]))

            # FIXME: Check for termination conditions. The round ends
            # if the current player manages to fill their table.
            if False == unfilled(G['tables'][G['current']]):
                # We've got a winner for this round; decrement their next table size.
                G['sizes'][G['current']] -= 1

                # Calculate score penalty for non-winners.
                for i in range(G['nplayers']):
                    if i != G['current']:
                        # Add in values of face down cards.
                        G['scores'][i] += sum([ G['tables'][i][j][1][0] for j in range(G['sizes'][i]) if not G['tables'][i][j][0] ])

                # Round is over, exit while loop to go on to next one.

                break

            # FIXME: Round still incomplete: increment the current
            # player in G and continue.
            if G['current'] == nplayers-1:
                G['current'] = 0
            else:
                G['current'] = G['current']+1

        print("Round{} complete: player {} wins the round.".format(G['round'], G['current']+1))
        print("Current scores: {}".format(showScores(G['nplayers'], G['scores'])))
        print("=============================================")
        # Go on to next round; winning player gets to start the round.
        G['round'] = G['round'] + 1

    # Exit from while loop means that someone is a winner!
    print("The winner is Player{}, with a final score of {}.".format(G['current']+1, G['scores'][G['current']]))
