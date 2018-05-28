import Player
import AIEngine
from GameObjects import gamestate

game = gamestate()

game.addplayer('Alice', AIEngine.LowestCard())
game.addplayer('Berry', AIEngine.LowestCard())

game.deal() 

for i in range(22*2):
    game.nextMove()

print(game.narrative)
print('\n---RESULT---\n')  
 
print(game.discardarea)
print('\n')
 
for p in game.players: 
    print(p.table)
    print('Score: '+ str(p.table.getScore())+ '\n')

exit(0)
