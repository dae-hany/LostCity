import GameObjects

# 플레이어가 보지 못한 카드의 집합을 반환 
def setUnseenCards(game):
    i = (game.nextturnpointer + 1) % len(game.players)
    return list(game.deck.cards) + game.players[i].hand.cards

# 특정 색깔의 카드들만 선택해서 반환 
def selectColor(cardset, card):
    cards = [] 
    for c in cardset:
       if c.color == card.color:
          cards.append(c)
    return cards

# 주어진 카드 위에 놓을 수 있는 카드를 선택하여 반환 
def selectAbove(cardset, card):
    cards = []
    for c in cardset:
       if c.ordinalval > card.ordinalval:
          cards.append(c)
    return cards          

# 카드 집합의 점수를 계산하여 반환 
def scoreSet(cardset):
    if len(cardset) == 0:
       return 0
    score = -20 # 기본 점수 -20 
    multi = 1 
    bonus = 0
       
    for c in cardset:
       if c.color != cardset[0].color:
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
