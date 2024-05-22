# JumpBotMuyBien
## JumpSturdy KI
### The best bot out there!!!!

## Meilenstein 1 (Dummy KI):
### Anforderungen:
* Zuggenerator: Alle Positionen getten, für diese Positionen gültige Richtungen ermittlen, Anzahl der Steps ermitteln
    * `get_all_positions()`
    * `get_valid_directions()`
    * `get_steps()`
- [ ] Same Size Array
- [ ] Concurrency
- [ ] Min-Max Algorythm
- [ ] Alpha-Beta Algorythm
- [ ] Visualizer (maybe later)
- [ ] Unit Tests
- [ ] Benchmarks

Blau ist negative bei EVAL

## Board Evalutation Criteria
1. turn => positive points, other => negative points 
2. pieces = 1 point, tower = 3 points  --> check if element.length is bigger 1
3. more points as you go forward and in the middle  --> from early match looking, forward +, middle +
4. and give points per move one can make --> count(getAllMoves() (From the same starting point))

## Game ending conditions:
1. A player that cannot make a legal move loses
2. Making the same move 3 times
3. Reaching the other end
4. no more pieces
5. 


