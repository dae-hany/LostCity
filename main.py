import player
import Gamestate


a = 1
g = Gamestate.deck()

print(g) 
print('dealing')

p1 = Gamestate.playerhand('a')
p2 = Gamestate.playerhand('b')

Gamestate.deal(g, p1, p2) 

print(p1) 
print(p2) 

print('remaining deck:') 
print(g) 

