import Player
import GameObjects
import CalcUtils as Ut
import random

negativeInfinity = -9999

#class contains utilities methods. 
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
                 
   def playToTable(self, game, card):
      game.players[game.nextturnpointer].table.play(game.players[game.nextturnpointer].hand.playcard(card))
      return 'Played card(' + str(card) + ') to table'
   
   def playToDiscard(self, game, card):
      game.discardarea.play(game.players[game.nextturnpointer].hand.playcard(card))
      return 'Discarded card(' + str(card) + ')'
      
   def pickupFromDeck(self, game):
      newcard = game.deck.gettop()
      game.players[game.nextturnpointer].hand.add(newcard)
      return ', and picked up card(' + str(newcard) + ') from the deck.'
      
   def pickupFromDiscard(self, game, color):
      pickedcard = game.discardarea.take(color)
      game.players[game.nextturnpointer].hand.add(pickedcard)
      return ', and picked up card('+ str(pickedcard) + ') from the discard area.' 
   
class CalculatingAI(AIPlayer):
   def cardContributionToPile(self, game, card):
      pass 

   def taketurn(self, game):
      i = self.getallowedinfo(game)
      story = ''

      #assuming there are 16 valid moves(for each card to table or discard )
      #we need to calculate a expected score for each move, and play the best one.
      eVtable = [0] * 8
      eVdiscard = [0] * 8
      
      #calculate card to table scores
      #Expected value is made of
      #diffence that current card will make to immediate pile score. 
      #cards currently in hand(given enough turns to play)(playability adjusted) 
      #cards future to be picked up from deck (probability adjusted)(playability adjusted) 
      
      for index, card in enumerate(i['hand'].cards):
        
         #calculate card to table scores 
         card_eV = Ut.scoreSet(i['table'].piles[card.color] + [card]) - Ut.scoreSet(i['table'].piles[card.color]) 
         
         #hand_eV
         inhandset = Ut.selectAbove(Ut.selectColor(i['hand'].cards, card), card)
         hand_eV = Ut.scoreSet(inhandset + i['table'].piles[card.color] + [card])-Ut.scoreSet(i['table'].piles[card.color] + [card])
         
         deck_eV = 0
         
         eVtable[index] = card_eV + hand_eV + deck_eV
         if not i['table'].legalToPlaceOnTable(card):
            eVtable[index] = negativeInfinity
            #continue
         print("[{}] card:{} hand:{} deck:{} = total:{}".format(card, card_eV, hand_eV, deck_eV, eVtable[index]))
            
       
         #calculate card to discard scores
         eVdiscard[index] = 0
         
         
      
      #play best card to best location
      RandomCard().taketurn(game)
      return 'Calculated.'
      
class RandomCard(AIPlayer):
   def taketurn(self, game):
      story = 'RandomCard:'
      i = self.getallowedinfo(game)
      cardtoplay = random.choice(i['hand'].cards)
      if( not i['table'].legalToPlaceOnTable(cardtoplay) ):
         story += self.playToDiscard(game, cardtoplay)
      else:  
         story += self.playToTable(game, cardtoplay)
      #refresh hand with new card.
      story += self.pickupFromDeck(game)
      return story
      
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
      
      story += 'Playing ' + str(lowest) + 'as its lowest ' + colorwithmost + ' card that I have. '

      if( not info['table'].legalToPlaceOnTable(lowest) ):
         story += self.playToDiscard(game, lowest)
      else:  
         story += self.playToTable(game, lowest)
      #refresh hand with new card.
      story += self.pickupFromDeck(game)
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
         story += self.playToDiscard(game, lowest)
      else:  
         story += self.playToTable(game, lowest)
      #refresh hand with new card.
      story += self.pickupFromDeck(game)
      return story
      
      
   
      
    
    
    
    