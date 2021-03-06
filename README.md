## Alpha-beta Pruning and Hueristic-based Search

### Requisites
All programs contained in this repo must be run using `python 2.7.9` and not compatible with `python 3.x`

### Nim using Alpha-Beta Pruning
In `/alpha-beta` run the nim program using 
`python nim.py --piles <pile 1 size> <pile 2 size> ... <pile N size> --first-move <human || computer>`
Follow the prompts on how to move, i.e. `<pile to choose from> <number of items to take` as integers delimited by a single space. The game board will be printed between each move to display what options are available.
The program uses alpha-beta pruning to _generate_ a game tree for nim, where the computer will then follow any existing winning strategy in the sub-tree of the current game state.

### Heuristic-based Search
In `/search` run the npuzzle program using `python npuzzle.py`. The settings, which are predetermined, will choose 5 randomly generated 8-puzzle states and run A* and Greedy Best First Search on each state using one of three heuristic functions; these are number of tiles out of place, manhattan distance, and euclidean distance. Trial results including the explored and frontier set size, and the solution length will be printed to stdout. Each randomly generated state is ensured to belong to the same subset of n-puzzle states as the goal state.

### Approximating the Knapsack Problem with Genetic Algorithms
In `/genetic-algorithms` run the knapsack approximation program using `python knapsack.py`. The tuning parameters that can be altered are found in main and inlclude: population size; number of generations to run; maximum weight allowed in the knapsack; fitness function; etc. To use your own knapsack, or item/weight combinations, define it in `pregenerated_bags.py` following the convention used within this file then change the import line in the main program to `from pregenerated_bags import <yourknapsack> as knapsack`.

_write up to be added later_
