import Player
import GameObjects
import CalcUtils as Ut
import random

negativeInfinity = -999

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
   #Takes a card and returns its score contribution to the pile.. ie the pile with and without it. 
   def cardContributionToSet(self, game, cardset, card):
      pileWithout = cardset
      pileWith = pileWithout + [card]
      return Ut.scoreSet(pileWith) - Ut.scoreSet(pileWithout)
      
   def taketurn(self, game):
      i = self.getallowedinfo(game)
      story = ''

      #assuming there are 16 valid moves(for each card to table or discard )
      #we need to calculate a expected score for each move, and play the best one.
      eVtable = [float(0)] * 8
      eVdiscard = [float(0)] * 8
      
      #calculate card to table scores
      #Expected value is made of
      #diffence that current card will make to immediate pile score. 
      #cards currently in hand(given enough turns to play)(playability adjusted) 
      #cards future to be picked up from deck (probability adjusted)(playability adjusted) 
      bestcard = None
      bestscore = negativeInfinity-1
      
      for index, card in enumerate(i['hand'].cards):
         tableset = i['table'].piles[card.color] 
        
         #calculate card to table scores 
         card_eV = self.cardContributionToSet(game, tableset, card) 
         #hacks: Without this a H will rarely be led as its calculated to give -40
         if card.value == 'H':
            card_eV = -20
         
         #hand_eV
         inhandset = Ut.selectAbove(Ut.selectColor(i['hand'].cards, card), card)
         hand_eV = float(Ut.scoreSet(inhandset + tableset + [card])-Ut.scoreSet(tableset + [card]))
         
         #deck_eV
         unseenSet = Ut.setUnseenCards(game)
         playableUnseenSet = Ut.selectAbove(Ut.selectColor(unseenSet, card), card) 
         deck_eV = 0
         c_remain = i['cardsleft'] 
         
         #each card is worth its value times probability of getting it played. (pickup, then having enough turns to play it) 
         for c in playableUnseenSet:
             #Calculate the difference this particular card would make...
             c_diff = self.cardContributionToSet(game, inhandset + tableset, c)
             #print(float(len(unseenSet)), float(c_remain)) 
             
             #deck_eV += float(c_diff * ((c_remain / float(len(unseenSet))) * (1/float(c_remain)))) 
             deck_eV += float(c_diff * 0.5)  #This card, and assuming 50-50 chance to pick it up. 
         
         
         eVtable[index] = card_eV + hand_eV + deck_eV
         if not i['table'].legalToPlaceOnTable(card):
            eVtable[index] = negativeInfinity
            #continue
         print("[{}] card:{} hand:{} deck:{:.2f} = {:.2f}".format(card, card_eV, hand_eV, deck_eV, eVtable[index]))
            
       
         #calculate card to discard scores
         eVdiscard[index] = 0
         
         #note card value if highest yet
         if eVtable[index] > bestscore:
             bestscore = eVtable[index]
             bestcard = card
      
      #play best card to best location
      if( not i['table'].legalToPlaceOnTable(bestcard) ):
         story += self.playToDiscard(game, bestcard) 
      else:  
         story += self.playToTable(game, bestcard)
      #refresh hand with new card.
      story += self.pickupFromDeck(game)
      return story
      return 'Calculated. Played [' +str(bestcard) + ']' 
      
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
      
      
   
      
    
    
    
    