# JumpBotMuyBien
## JumpSturdy KI
### The best bot out there!!!!

### !!! Disclaimer: Die angegebene Anzahl an Commits und Umfang der Commits sind nicht aussagekräftig über die Menge an absolvierter Arbeit pro Contributor, da das JetBrains - PyCharm Feature "Code Together" benutzt wurde !!!

## Meilenstein 1 (Dummy KI):
### Anforderungen:
* Zuggenerator: Alle Positionen getten, für diese Positionen gültige Richtungen ermittlen, Anzahl der Steps ermitteln
    * `get_all_positions()`
    * `get_valid_directions()`
    * `get_steps()`
- [ ] Same Size Array
- [X] Min-Max Algorythm
- [X] Alpha-Beta Algorythm
- [X] Visualizer (maybe later)
- [X] Unit Tests
- [X] Benchmarks

## Alpha-Beta-KI:
## Board Evalutation Criteria
1. turn => positive points, other => negative points 
2. pieces = 1 point, tower = 3 points  --> check if element.length is bigger 1
3. more points as you go forward and in the middle  --> from early match looking, forward +, middle +
4. and give points per move one can make --> count(getAllMoves() (From the same starting point))

## Game ending conditions:
1. A player that cannot make a legal move loses
2. Making the same move 3 times (remis) (for later)
3. Reaching the other end
4. no more pieces

## Minimax algorithm
1. red is max Player
2. blue is min Player

## TODO: 
- implement automatic max player and min player call 
- Maybe new Tree Structure idk
- Benchmarks verbessern (Unterschiede in Anzahl der untersuchten Stellungen zeigen)
- Projektwiki aktualisieren

## Erweiterte KI:
- 3-5 weitere KI Techniken implementieren (darunter 1-2 komplexe)

Komplexe Beispiele:
- Aspiration Windows
- Board durch Bitboard ersetzen (Quelle: https://github.com/cglouch/snakefish)
  - sehr sinnvoll, weil wir eine sehr schlechte Laufzeit haben
- Transposition Table scheint mir auch sehr sinnvoll

Weniger Komplexe:
- Zugsortierung
- Erweitern der Bewertungsfunktion (Zentrumskontrolle, Piece Square Tables, Mobilität/Felderkontrolle, vllt TWOCOLTOEWR noch mehr Punkte geben)
- Verbesserung des Inserts (vllt auch concurrency beim Tree create/insert?)
- zufällige Auswahl von moves, falls es einen anderen move mit der gleichen eval Punktzahl existiert
- 3 Fache Wiederholung erkennen
- vielleicht noch Effizienzerhöhung durch
  (# Precompute the KING_MOVES array at import time
KING_MOVES = np.fromiter(
    (compute_king_moves(i) for i in range(64)),
    dtype=np.uint64,
    count=64
)) aus snakefish

Screencast:
Deliverables:
1. ein kurzer Report:
- Welche KI-Techniken haben Sie umgesetzt, wie haben Sie sie implementiert?(Begründete Designentscheidungen)
- tabellarische Präsentation der Performancetests. Unbedingt auch Ihre Rechnerkonfiguration spezifizieren. 
- Wie hat sich die Bewertungsfunktion über den bisherigen Verlauf des Semesters entwickelt?
- Was planen Sie für den 4. Meilenstein?
2. Screencast, der demonstriert, wie Sie Ihre Performancetests durchführen, z.B. durch recording der Konsole.
3. Dokumentation der Performance Ihrer aktuellen KI im Wiki.



## aspiration windows tests
- without: 5642
- 2 move to win tree took 3.7085649967193604
- 3 moves to win took: 0.037438154220581055 seconds C5-C6 --> res: C5-C6

- with: 
BitBoard Dokumentation
- 

## optimierte KI:
- benchmark Tests sauber implementieren (so umschreiben, dass man alphabeta und minimax laufen lassen kann und bitboard und 2D array auch in einem)
- bitboards optimieren
- Ruhesuche parameter überarbeiten -> zugsortierung
- aspiration windows fix (maybe)
- Tree optimieren (vielleicht durch Parallelisierung)
- Zeitmanagement
