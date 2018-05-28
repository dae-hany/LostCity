import Player
import GameObjects

class AIPlayer:
   def __init__(self, player):
	     self.player = player
	
   def getinfo(self, gamestate):
      hand = self.player.hand
      table = self.player.table
      discardarea = gamestate.discardarea
      cardsleft = gamestate.deck.cardsleft
      return {'hand' : hand, 'table' :table, 'discardarea' :discardarea, 'cardsleft' :cardsleft} 
     
class LowestCard(AIPlayer):
   def taketurn(self, state):
      s = self.getinfo(state)
      lowest = None
      lowestvalue = 10
      for c in s['hand'].cards:
         if c.ordinalval < lowestvalue:
             lowestvalue = c.ordinalval
             lowest = c
      return c
    
    
    
    
    