import Player
from GameObjects import gamestate

p1 = Player.player('Alice')
p2 = Player.player('Berry')

game = gamestate()

game.deal(p1, p2) 

for i in range(4):
   

print('\n---RESULT---\n')  
 
print(discardarea)
print('\n')
 
print(p1.table)
print('Score: '+ str(p1.table.getScore())+ '\n')


print(p2.table)
print('Score: '+ str(p2.table.getScore())+ '\n')

exit(0)
