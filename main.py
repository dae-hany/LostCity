import Player
import AIEngine
from GameObjects import gamestate

singleMode = True

gamesetup = {('Alice', AIEngine.LowestCard()),
            ('Berry', AIEngine.RandomCard())}

#Simulate a single game, or a game with 1000 rounds.
if singleMode:
   game = gamestate()

   for name, AI in gamesetup:
      game.addplayer(name, AI)
     
   game.deal() 
   game.flags_printplayerhands = True
   
   while not game.isdone():
       game.nextMove()
   
   
   print(game.narrative)
   
   print('turns', game.turncounter) 
   print('\n---RESULT---\n')  
    
   print(game.discardarea)
   print('\n')
    
   for p in game.players: 
       print(p.table)
       print('Score: '+ str(p.table.getScore())+ '\n')
   
else:
   scores = [0,0]
   
   gamestoplay = 5000
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
   