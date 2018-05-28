import Player
import GameObjects

class AIPlayer:
   def __init__(self, player):
	     self.player = player
	
   def getinfo(self, game):
      return {'hand' : self.player.hand,
              'table' :self.player.table, 
              'discardarea' :game.discardarea, 
              'cardsleft' :game.deck.cardsleft} 
     
class LowestCard(AIPlayer):
   def taketurn(self, game):
      s = self.getinfo(game)
      #determine lowest card so that we can play it. 
      lowest = None
      lowestvalue = 10
      for c in s['hand'].cards:
         if c.ordinalval < lowestvalue:
             lowestvalue = c.ordinalval
             lowest = c
             
      #Once loop completes we will have the lowest card, now play it.
      self.player.table.play(self.player.hand.playcard(lowest))
      self.player.hand.add(game.deck.gettop())
      
   
      
    
    
    
    