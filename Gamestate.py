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
    
    def getTop(self):
        self.cardsleft -= 1
        return self.cards.popleft()
        
    
class playertable:
    def __init__(self):
       pass
       
class playerhand:
    def __init__(self, name):
       self.cards = []
       self.name = name 
       
    def add(self, card):
       self.cards.append(card)
       
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
        p1.add(deck.getTop())
        p2.add(deck.getTop())
        