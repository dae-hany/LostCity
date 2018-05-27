import GameObjects

class playertable:
    def __init__(self, name):
       self.piles = {'R' :[] , 'W' :[] , 'B' :[] , 'G' :[] , 'Y' :[] } 
       self.name = name
    
    def play(self, card):
       if card.color not in self.piles.keys():
           raise ValueError('bad color supplied in playtotable')
       
       
       self.piles[card.color].append(card)
    
    def getScore(self):
       pass
    
    def __str__(self):
       r = 'Name:' + self.name
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
       self.hand = playerhand(name )
       self.table = playertable(name)
       self.name = name
       