import random
from collections import deque

import Player

class card:
    def __init__(self, col, score_val, ord_val):
        self.color = col
        self.value = score_val
        self.ordinalval = ord_val
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
            self.cards.append(card(c,'X',10))
            self.cards.append(card(c,'9',9))
            self.cards.append(card(c,'8',8))
            self.cards.append(card(c,'7',7))
            self.cards.append(card(c,'6',6))
            self.cards.append(card(c,'5',5))
            self.cards.append(card(c,'4',4))
            self.cards.append(card(c,'3',3))
            self.cards.append(card(c,'2',2))
            self.cardsleft += 9
            for i in range(3):
                self.cards.append(card(c,'H',1))
                self.cardsleft += 1
        #self.cards.reverse()
        random.shuffle(self.cards)
        
    def __str__(self):
        r = "Deck: " 
        for card in self.cards:
            r += str(card) + ' ' 
        return r + '(' + str(self.cardsleft) + ')' 
    
    def gettop(self):
        self.cardsleft -= 1
        if self.cardsleft < 0:
            raise ValueError('out of cards in deck')
        return self.cards.popleft()
       
class discardarea:
    def __init__(self):
        self.piles = {'R' :[] , 'W' :[] , 'B' :[] , 'G' :[] , 'Y' :[] } 
    
    def play(self, card):
        self.piles[card.color].append(card)
        
    def take(self, color):
        return self.piles[color].pop()
    
    def __str__(self):
       r = 'Discard Area:\n' 
       depth = 0
       for k in self.piles.keys():
           r += ' ' + k.upper() + ' ' 
           if len(self.piles[k]) > depth:
               depth = len(self.piles[k])
       for d in range(depth):
           r += '\n'
           for p in self.piles.keys():
               if len(self.piles[p])-1 < d:           
                   r += '   ' 
               else:    
                   r += ' ' + str(self.piles[p][d]) 
       return r
    
class gamestate:
   def __init__(self):
       self.deck = deck()
       self.discardarea = discardarea()
       self.players = []
       self.engines = []
       self.nextturnpointer = 0
       self.turncounter = 0
       self.narrative = 'Game initialized...\n'
       self.flags_printplayerhands = True
       
   def addplayer(self, name, AIEngine):
       self.narrative += 'Adding player ' + name + '...\n'
       self.players.append(Player.player(name))
       self.engines.append(AIEngine)       
       
   def deal(self):
       self.narrative += 'Dealing...\n'
       if len(self.players) != 2:
           raise ValueError('Unusual number of players, expected exactly two.')
       if self.deck.cardsleft < (len(self.players) * 8):
           raise ValueError('not enough cards to deal 8 to each player.') 
       for i in range(8):
           for p in self.players:
               p.hand.add(self.deck.gettop())

   def nextMove(self):
       self.narrative += 'Turn ' + '{:0>2}'.format(self.turncounter) + ': '
       if self.deck.cardsleft == 0:
           raise ValueError('game is over. last card has already been drawn.')
       
       if self.flags_printplayerhands:
           self.narrative += str(self.players[self.nextturnpointer].hand)
       
       #trigger the engine to make a move.
       self.narrative += str(self.players[self.nextturnpointer]) + ':'
       result = self.engines[self.nextturnpointer].taketurn(self)
       self.narrative += result + '..\n'
       
       #update game 
       self.nextturnpointer += 1
       self.nextturnpointer = self.nextturnpointer % len(self.players)
       self.turncounter += 1
       
   def isdone(self):
       return self.deck.cardsleft <= 0
       
       
       
       
       