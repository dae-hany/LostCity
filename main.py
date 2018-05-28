import Player
import AIEngine
from GameObjects import gamestate

p1 = Player.player('Alice')
p2 = Player.player('Berry')

ai1 = AIEngine.LowestCard(p1)
ai2 = AIEngine.LowestCard(p2)

game = gamestate()

game.deal(p1, p2) 


for i in range(2):
   print(p1.hand)
   ai1.taketurn(game)
   print(p1.hand)
   
   print(p2.hand)
   ai2.taketurn(game)
   print(p2.hand)

print('\n---RESULT---\n')  
 
print(game.discardarea)
print('\n')
 
print(p1.table)
print('Score: '+ str(p1.table.getScore())+ '\n')


print(p2.table)
print('Score: '+ str(p2.table.getScore())+ '\n')

exit(0)
