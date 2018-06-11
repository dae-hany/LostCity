import GameObjects

# Returns the set of unseen cards from the perspective of player. 
def setUnseenCards(game):
    i = (game.nextturnpointer + 1) % len(game.players)
    return list(game.deck.cards) + game.players[i].hand.cards

# Returns a set of cards that have the color
def selectColor(cardset, card):
    cards = [] 
    for c in cardset:
       if c.color == card.color:
          cards.append(c)
    return cards

# Returns a set of cards(from another set) that would be legal to play on top of the given card
def selectAbove(cardset, card):
    cards = []
    for c in cardset:
       if c.ordinalval > card.ordinalval:
          cards.append(c)
    return cards          

# Returns the score of a set of cards. 
def scoreSet(cardset):
    if len(cardset) == 0:
       return 0
    score = -20
    multi = 1
    bonus = 0
       
    for c in cardset:
       if c.color <> cardset[0].color:
           raise ValueError('scoring more than one color') 
       if c.value == 'H':
           multi += 1
       elif c.value == 'X':
           score += 10
       else:
           score += c.ordinalval
    
    if len(cardset) >= 8:
       bonus = 20
    
    return float((score * multi) + bonus)
