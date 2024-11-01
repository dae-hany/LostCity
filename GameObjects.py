import random
from collections import deque

import AIPlayer

# 카드 클래스 
class card:
    def __init__(self, col, score_val, ord_val):
        self.color = col # 색깔
        self.value = score_val # 점수 
        self.ordinalval = ord_val # 카드의 순서 
        #print("creating card", col, val) 
    def __str__(self) :   
       return self.color+self.value
        
class deck:
    def __init__(self, seed=0):
        self.seed=seed # 랜덤 시드 
        self.cardsleft = 0 # 덱에서 남은 카드의 수 
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
    
    # 덱에서 가장 위에 있는 카드를 가져오고, 남은 카드 수 감소 
    def gettop(self):
        self.cardsleft -= 1
        if self.cardsleft < 0:
            raise ValueError('out of cards in deck')
        return self.cards.popleft()
       
class discardarea:
    def __init__(self):
        self.piles = {'R' :[] , 'W' :[] , 'B' :[] , 'G' :[] , 'Y' :[] } 
    
    # 카드를 폐기 영역에 추가 
    def play(self, card):
        self.piles[card.color].append(card)
    
    # 폐기 영역에서 카드 하나 가져오기 
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

# 게임 전체 상태 관리 
class gamestate:
   def __init__(self):
       self.deck = deck()
       self.discardarea = discardarea()
       self.players = [] # 게임에 참여하는 플레이어 목록 저장 
       self.engines = [] # 각 플레이어에 대한 ai 엔진 목록 저장 
       self.nextturnpointer = 0 # 다음 차례의 플레이어를 가리키는 인덱스
       self.turncounter = 0 # 게임 턴 수 
       self.narrative = 'Game initialized...\n'
       self.flags_printplayerhands = True # 플레이어의 손을 출력할지 여부 결정 
    
   # 플레이어를 게임에 추가 
   def addplayer(self, name, AIEngine):
       self.narrative += 'Adding player ' + name + '...\n'
       self.players.append(AIPlayer.AIplayer(name))
       self.engines.append(AIEngine)       
    
   # 플레이어에게 카드를 배분 
   def deal(self):
       self.narrative += 'Dealing...\n'
       if len(self.players) != 2:
           raise ValueError('Unusual number of players, expected exactly two.')
       if self.deck.cardsleft < (len(self.players) * 8):
           raise ValueError('not enough cards to deal 8 to each player.') 
       for i in range(8):
           for p in self.players:
               p.hand.add(self.deck.gettop())
    # 현재 턴의 다음 단계를 진행 
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
       
   # 게임이 끝났는지 여부 확인 
   def isdone(self):
       return self.deck.cardsleft <= 0
       
       
       
       
       