import Player
import GameObjects

p1 = Player.player('Alice')
p2 = Player.player('Berry')

deck = GameObjects.deck()
discardarea = GameObjects.discardarea()
GameObjects.deal(deck, p1, p2) 

for i in range(5r):
    #a.playonpile('R',deck.gettop()) 
    p1.table.play(deck.gettop())
    p2.table.play(deck.gettop())
    deck.gettop()
    #discardarea.play(deck.gettop())

print('\n---RESULT---\n')  
 
print(discardarea)
print('\n')
 
print(p1.table)
print('Score: '+ str(p1.table.getScore())+ '\n')


print(p2.table)
print('Score: '+ str(p2.table.getScore())+ '\n')

exit(0)
