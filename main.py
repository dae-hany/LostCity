import Player
import AIEngine
from GameObjects import gamestate

import CalcUtils as Ut

# singleMode가 True이면 한 게임만 시뮬레이션
# singleMode가 False이면 여러 게임 반복 
singleMode = True

# 변수 및 게임 설정 
gamesetup = {('Alice', AIEngine.CalculatingAI()),
            ('Berry', AIEngine.RandomCard())}


#Simulate a single game, or a game with 1000 rounds.
if singleMode:
   game = gamestate()
   
   #check util functions
#   card = game.deck.cards.pop()
#   print(card)
#   print(map(str, Ut.selectColor(game.deck.cards, card)))
#   print(map(str, Ut.selectAbove(Ut.selectColor(game.deck.cards, card), card)))
#   exit(0)

   for name, AI in gamesetup:
      game.addplayer(name, AI)
     
   game.deal() 
   game.flags_printplayerhands = True
   
   while not game.isdone():
       game.nextMove()
       print(game.players[0].table)
       print(game.players[1].table) 
       if game.turncounter % 3 == 0:
           print('unknown cards') 
           print(map(str, Ut.setUnseenCards(game)) ) 
   
   #print(game.narrative)
   
   print('turns', game.turncounter) 
   print('\n---RESULT---\n')  
    
   print(game.discardarea)
   print('\n')
    
   for p in game.players: 
       print(p.table)
       print('Score: '+ str(p.table.getScore())+ '\n')
   
else:
   scores = [0,0]
   
   gamestoplay = 4000
   for i in range(gamestoplay):
      game = gamestate()
   
      for name, AI in gamesetup:
         game.addplayer(name, AI)
      
      game.deal() 
      game.flags_printplayerhands = True
      
      while not game.isdone():
         game.nextMove()
      
      scores[0] += game.players[0].table.getScore() 
      scores[1] += game.players[1].table.getScore() 
   
   for i in scores:
      print('AverageScore' + str( i / gamestoplay ))
   