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
              
class BiggestSetLowCard(AIPlayer):
   def taketurn(self, game):
      info = self.getallowedinfo(game)
      story = ''
      
      #count how many of each color, play the lowest card of the set you have the most of.
      colorcounts = {'R':0, 'G':0, 'B':0, 'Y':0, 'W':0 }
      for c in info['hand'].cards:
         colorcounts[c.color] += 1
      colorwithmost = None
      highcolorcount=0
      for i in colorcounts.keys():
         if colorcounts[i] > highcolorcount:
            colorwithmost = i
            highcolorcount = colorcounts[i]
               
      lowest = None
      lowestvalue = 10
      for c in info['hand'].cards:
         if c.color != colorwithmost:
            continue
         if c.ordinalval < lowestvalue:
            lowestvalue = c.ordinalval
            lowest = c
      
      story += 'Playing ' + str(lowest) + 'as its lowest ' + colorwithmost + ' card that I have, '

      if( not info['table'].legalToPlaceOnTable(lowest) ):
         info['discardarea'].play(info['hand'].playcard(lowest))
         story +=  'it went to discard area'
      else:  
         info['table'].play(info['hand'].playcard(lowest))
         story += 'it went to table'
      #refresh hand with new card.
      newcard = game.deck.gettop()
      info['hand'].add(newcard)
      story += ' then, picked up card(' + str(newcard) + ').'
      return story
      
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
      
      
   
      
    
    
    
    