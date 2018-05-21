import Player
import GameObjects

class LowestCard:
   def __init__(self, player):
	   self.p = player
	
   def taketurn(self, gamestate):
	   hand = self.p.hand
      table = self.p.table
      discardarea = gamestate.discardarea
      cardsleft = gamestate.deck.cardsleft
      pass