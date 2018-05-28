import Player
import GameObjects

class AIPlayer:
   def __init__(self):
	   pass 	
   def getallowedinfo(self, game):
      pindex = game.nextturnpointer
      opponentplayerindex = (pindex+1)%2
      return {'pix' : game.nextturnpointer,
              'hand' : game.players[pindex].hand,
              'table' : game.players[pindex].table, 
              'othertable' : game.players[opponentplayerindex].table,
              'discardarea' : game.discardarea, 
              'cardsleft' : game.deck.cardsleft,
              'turncounter' : game.turncounter} 
     
class LowestCard(AIPlayer):
   def taketurn(self, game):
      info = self.getallowedinfo(game)
      story = ''
      #determine lowest card so that we can play it. 
      lowest = None
      lowestvalue = 10
      for c in info['hand'].cards:
         if c.ordinalval < lowestvalue:
             lowestvalue = c.ordinalval
             lowest = c
             
      #Once loop completes we will know which is the lowest card, now play it.
      #if it fits on our table, then there, else to the discardarea. 
      if( not info['table'].legalToPlaceOnTable(lowest) ):
         info['discardarea'].play(info['hand'].playcard(lowest))
         story +=  'Played card(' + str(lowest) + ') to discard area'
      else:  
         info['table'].play(info['hand'].playcard(lowest))
         story += 'Played card(' + str(lowest) + ') to table'
      #refresh hand with new card.
      newcard = game.deck.gettop()
      info['hand'].add(newcard)
      story += ' then, picked up card(' + str(newcard) + ').'
      return story
      
      
   
      
    
    
    
    