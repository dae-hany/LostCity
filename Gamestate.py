import random
from collections import deque

class card:
    def __init__(self, col, val):
        self.color = col
        self.value = val
        #print("creating card", col, val) 
    def __str__(self) :   
       return self.color+self.value
        
class deck:
    def __init__(self, seed=0):
        self.seed=seed
        self.cardsleft = 0
        if seed:
            random.seed(seed)
        #5colors 12of each
        self.cards = deque() 
        for c in ["R", "G", "B", "Y", "W" ]:
            for i in ["2", "3","4","5","6","7","8","9","X","H","H","H"]: 
                 self.cards.append(card(c,i))
                 self.cardsleft += 1
        random.shuffle(self.cards)
        
    def __str__(self):
        r = "Deck: " 
        for card in self.cards:
            r += str(card) + ' ' 
        return r + '(' +str(self.cardsleft) + ')' 
    
    def gettop(self):
        self.cardsleft -= 1
        return self.cards.popleft()
        
    
class playertable:
    def __init__(self):
       self.piles = {'r' :[] , 'w' :[] , 'b' :[] , 'g' :[] , 'y' :[] } 
       
    def playonpile(self, col, card):
       if col not in self.piles.keys():
           raise ValueError('bad color supplied') 
       #if self.piles[col][-1].value
       self.piles[col].append(card) 
    
    def __str__(self):
       r = '' 
       depth = 0
       for k in self.piles.keys():
           r += k.upper() + '  ' 
           if len(self.piles[k]) > depth:
               depth = len(self.piles[k])
       r += '\n'
       
       for d in range(depth):
           for p in self.piles.keys():
               #print(d, 'thin', self.piles[p], r) 
               if len(self.piles[p])-1 < d:
                   r += '  ' 
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
       
class discardarea:
    def __init__(self):
       pass
    
class gamestate:
    def __init__(self):
        pass
       
def deal(deck, p1, p2):
    if deck.cardsleft < 16:
        raise ValueError('not enough cards to deal 8 to each player') 
    for i in range(8):
        p1.add(deck.gettop())
        p2.add(deck.gettop())
        