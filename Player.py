import GameObjects
import CalcUtils

# 플레이어 테이블 관리, 색깔별로 카드 더미 유지 
class playertable:
    def __init__(self, name):
       self.piles = {'R' :[] , 'W' :[] , 'B' :[] , 'G' :[] , 'Y' :[] } 
       self.name = name
    
    # table에 카드를 둘 수 있는지 확인 
    def legalToPlaceOnTable(self, card):
       if len(self.piles[card.color]) == 0:       
           return True
       else:
           if self.piles[card.color][-1].ordinalval > card.ordinalval:
               return False
           else:
               return True
    
    # table에 카드를 두기 
    def play(self, card):
       if card.color not in self.piles.keys():
           raise ValueError('bad color supplied in playtotable')
       if len(self.piles[card.color]) == 0:       
           self.piles[card.color].append(card)
       else:
           if self.piles[card.color][-1].ordinalval > card.ordinalval:
               raise ValueError('Illegal move('+self.name+') Card below has a greater value.')
           else:
               self.piles[card.color].append(card)
    
    # 카드 더미의 점수 계산 
    def getPileScore(self, color):
       if len(self.piles[color]) == 0:
          return 0
       else:
          return CalcUtils.scoreSet(self.piles[color]) 
       
    # 모든 색깔의 카드 더미의 점수를 합산
    def getScore(self):
       table_score = 0
       for p in self.piles.keys():
          table_score += self.getPileScore(p)
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

# 플레이어의 손에 있는 카드를 관리 
class playerhand:
    def __init__(self, name):
       self.cards = [] # 내 손에 있는 카드
       self.name = name  # 플레이어 이름 저장 
       
    # 카드를 손에 추가 
    def add(self, card):
       self.cards.append(card)
    
    # 주어진 카드를 손에서 제거하고 반환 
    def playcard(self, card):
       self.cards.remove(card)
       return card
    
    def __str__(self):
       r = '' 
       for card in self.cards:
           r += str(card) + ' ' 
       return r

# 개별 플레이어  
class player:
    def __init__(self, name):
       self.hand = playerhand(name) # 손 패
       self.table = playertable(name) # 테이블 
       self.name = name  # 이름 
    
    def __str__(self):
       return self.name
    

