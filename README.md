## Alpha-beta Pruning and Hueristic-based Search

### Requisites
All programs contained in this repo must be run using `python 2.7.9` and not compatible with `python 3.x`

### Nim using Alpha-Beta Pruning
In `/alpha-beta` run the nim program using `python nim.py --piles <pile 1 size> <pile 2 size> ... <pile N size> --first-move <human || computer>`
Follow the prompts on how to move, i.e. `<pile to choose from> <number of items to take` as integers delimited by a single space. The game board will be printed between each move to display what options are available.
The program uses alpha-beta pruning to _generate_ a game tree for nim, where the computer will then follow any existing winning strategy in the sub-tree of the current game state.

### Heuristic-based Search
In `/search` run the npuzzle program using `python npuzzle.py`. The settings, which are predetermined, will choose 5 randomly generated n-puzzle states and run A* and Greedy Best First Search on each state using one of three heuristic functions; these are number of tiles out of place, manhattan distance, and euclidean distance. Trial results including the explored and frontier set, and the solution length will be printed to stdout. 