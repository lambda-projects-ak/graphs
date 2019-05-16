hint, randomness can help, it can make it harder to debug
when you're in a room, you always pick a direction
that will ensure every time you get to a dead end
you know what path to move back to an unexplored room

```
this could work but you need to track which rooms you have visited before

def move(current_room):
  exits = current_room.getExits()
  if 'n' in exits:
    return 'n'
  elif 'e' in exits:
    return 'e'
  elif 's' in exits:
    return 's'
  elif 'w' in exits:
    return 'w'


```

1. pick a direction, you need to go somewhere
2. start by going north, then north

when there is only one way to go, you are at a dead end
start heading in one direction until you hit a room with an unexplored room
then pick a new direction

what kind of search did Brady demo? DFS

once you hit a dead end, you move back to the nearest room with an unexplored room.
count how many rooms have been visited, 500 means you're done
or you can make a map and track exits, when all exits are explored you are done
when there is an exit in your current room, you set those values as ?
then you move a direction

pick a random path until you hit a dead end (dfs using a queue)
when you hit a dead end, backtrack to the nearest room with an unexplored direction
bfs to nearest room with unexplored rooms

# how would we solve this

dft until you find a room with no unexplored exits
then bfs to search for the nearest room with an unexplored exit, and return a path
use that path to move to nearest unexplored room
repeat until there are no more unexplored exits
