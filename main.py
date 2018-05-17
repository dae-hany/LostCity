import player
import Gamestate


a = Gamestate.playertable() 
deck = Gamestate.deck()
print(deck) 
print(a) 

for i in range(5):
    a.playonpile('r',deck.gettop()) 

print('after\n')  
 
print(deck) 
print(a)
exit(0)

print('dealing')

p1 = Gamestate.playerhand('a')
p2 = Gamestate.playerhand('b')

Gamestate.deal(deck, p1, p2) 

print(p1) 
print(p2) 

print('remaining deck:') 
print(g) 

