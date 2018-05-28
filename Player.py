import GameObjects

class playertable:
    def __init__(self, name):
       self.piles = {'R' :[] , 'W' :[] , 'B' :[] , 'G' :[] , 'Y' :[] } 
       self.name = name
    
    def play(self, card):
       if card.color not in self.piles.keys():
           raise ValueError('bad color supplied in playtotable')
       if len(self.piles[card.color]) == 0:       
           self.piles[card.color].append(card)
       else:
           if self.piles[card.color][-1].ordinalval > card.ordinalval:
               raise ValueError('Illegal move('+self.name+')')
           else:
               self.piles[card.color].append(card)
    
    def getScore(self):
       table_score = 0
       for p in self.piles.keys():
          pile_score=-20
          pile_mulitplier = 1
          if len(self.piles[p]) == 0:
              pile_score = 0
          for c in self.piles[p]:
              if c.value == 'H':
                  pile_mulitplier += 1
              elif c.value == 'X':
                  pile_score += 10
              else:
                  pile_score += c.ordinalval
          pile_score *= pile_mulitplier
          table_score += pile_score
       return table_score
    
    def __str__(self):
       r = 'Table of ' + self.name + ':\n'
       depth = 0
       for k in self.piles.keys():
           r += ' ' + k.upper() + ' ' 
           if len(self.piles[k]) > depth:
               depth = len(self.piles[k])
       r += '\n'
       
       for d in range(depth):
           for p in self.piles.keys():
               if len(self.piles[p])-1 < d:           
                   r += '   ' 
               else:    
                   r += ' ' + str(self.piles[p][d]) 
           r += '\n' 
       return r
       
class playerhand:
    def __init__(self, name):
       self.cards = []
       self.name = name 
       
    def add(self, card):
       self.cards.append(card)
    
    def playcard(self, card):
       self.cards.remove(card)
       return card
       
    def __str__(self):
       r = 'Hand of ' + self.name + ': ' 
       for card in self.cards:
           r += str(card) + ' ' 
       return r
       
class player:
    def __init__(self, name):
       self.hand = playerhand(name)
       self.table = playertable(name)
       self.name = name
       
