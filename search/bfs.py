from npuzzle import Node
from helpers import *
import heapq
import math


def best_first_search(f, initial_state, goal_state):
	'''
	Runs BFS given a valid start state, goal, and evaluation function which
	determines whether the search runs as greedy BFS, A*, etc.

	f: an evaluation function to order the nodes on the frontier s.t.
	f(state) = ~ cost to goal
	inital_state: starting state of the n-puzzle
	goal_state: the state we are attempting to reach through valid moves
	'''
	# use dictionary for O(1)
	explored = dict()
	frontier = []

	initial_node = Node(initial_state, None, None, 0)
	heapq.heappush(frontier, (f(initial_node), initial_node))

	while frontier != []:
		cost, current_node = heapq.heappop(frontier)

		if is_equal(current_node._state, goal_state):
			return frontier, explored, current_node
		for successor in current_node.generate_successors():
			# don't reinvestigate prev. states
			if str(successor._state) not in explored:
				heapq.heappush(frontier, (f(successor), successor))

		explored[str(current_node._state)] = current_node._state

def run_trials(f, initial_states, goal_state, search_type=None, hueristic_type=None):
	'''
	Runs a trial for each state in initial state using the given evaluation function,
	invoking BFS.
	Prints the result of each trial to stdout
	'''
	for trial, initial_state in enumerate(initial_states):
		frontier, explored, node = best_first_search(f, initial_state, goal_state)
		print('TRIAL #{}\n{} - {}'.format(trial+1, search_type, hueristic_type))
		print_path_flat(node)
		print('\npath length: {}, explored set: {}, frontier: {}\n'.format(
			node._path_cost,
			len(explored),
			len(frontier))
		)


# hueristic functions

def manhattan_dist(state, goal_state):
	'''
	Returns the manhatten distance for state => goal state
	'''
	sum = 0
	for tile in reduce(flatten, state):
		if tile != 0:
			x1, y1 = position(state, tile)
			x2, y2 = position(goal_state, tile)
			sum += abs(x2 - x1) + abs(y2 - y1)
	return sum

def tiles_out_of_place(state, goal_state):
	'''
	Returns # tiles in different positions between state and goal_state
	'''
	sum = 0
	for tile in reduce(flatten, state):
		if tile != 0 and position(state, tile) != position(goal_state, tile):
			sum += 1
	return sum

def euclidean_dist(state, goal_state):
	'''
	Returns the sum of stright line distances for tiles in state => goal state
	'''
	sum = 0
	for tile in reduce(flatten, state):
		if tile != 0:
			x1, y1 = position(state, tile)
			x2, y2 = position(goal_state, tile)
			sum += math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
	return sum

def main():
	#define board size and trial info.
	rows, cols = 3, 3
	trials_to_run = 5
	initial_states = []
	goal_state = [
		[1,2,3],
		[4,5,6],
		[7,8,0]
	]

	#hueristic composition
	g = lambda n: n._path_cost
	h_manhatten = lambda n: manhattan_dist(n._state, goal_state)
	h_out_of_place = lambda n: tiles_out_of_place(n._state, goal_state)
	h_euclidean = lambda n: euclidean_dist(n._state, goal_state)


	# generate valid trial states to be used for each hueristic
	while len(initial_states) != trials_to_run:
		state = generate_state(rows, cols)
		if inversion_parity(state) == inversion_parity(goal_state):
			initial_states.append(state)
	
	#hueristic #1 (manhatten distance)
	run_trials(lambda n: g(n) + h_manhatten(n),
		initial_states,
		goal_state,
		'A*',
		'manhattan distance')
	run_trials(lambda n: h_manhatten(n),
		initial_states,
		goal_state,
		'greedy BFS',
		'manhattan distance')

	#hueristic #2 (tiles out of place)
	run_trials(lambda n: g(n) + h_out_of_place(n),
		initial_states,
		goal_state,
		'A*',
		'tiles out of place')
	run_trials(lambda n: h_out_of_place(n),
		initial_states,
		goal_state,
		'greedy BFS',
		'tiles out of place')

	#hueristic #3 (euclidean distance)
	run_trials(lambda n: g(n) + h_euclidean(n),
		initial_states,
		goal_state,
		'A*',
		'euclidean distance')
	run_trials(lambda n: h_euclidean(n),
		initial_states,
		goal_state,
		'greedy BFS',
		'euclidean distance')

if __name__ == '__main__':
	main()


'''
this state => goal should cost 26 moves

initial_state = [
		[7,2,4],
		[5,0,6],
		[8,3,1]
	]

	goal_state = [
		[0,1,2],
		[3,4,5],
		[6,7,8]
	]

'''