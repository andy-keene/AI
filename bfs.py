from npuzzle import Node
from helpers import *
import heapq


def best_first_search(f, initial_state, goal_state):
	'''
	Runs BFS given a valid start state, goal, and evaluation function which
	determines whether the search runs as greedy BFS, A*, etc.

	f: an evaluation function s.t. f(state) = ~ cost to goal
	inital_state: starting state of the n-puzzle
	goal_state: the state we are attempting to reach through valid moves
	'''
	explored = []
	frontier = []
	initial_node = Node(initial_state, None, None, 0)
	heapq.heappush(frontier, (f(initial_node), initial_node))

	while frontier != []:
		cost, current_node = heapq.heappop(frontier)
		if is_equal(current_node._state, goal_state):
			print_path(current_node)
			print('explored set: {}, frontier: {}'.format(len(explored), len(frontier)))
			return
		for successor in current_node.generate_successors():
			## add the following
			if successor._state not in explored:
				heapq.heappush(frontier, (f(successor), successor))
		explored.append(current_node._state)


def manhattan_dist(state, goal_state):
	'''
	Calculates the manhatten distance for state => goal state
	'''
	sum = 0
	for tile in reduce(flatten, state):
		if tile != 0:
			x1, y1 = position(state, tile)
			x2, y2 = position(goal_state, tile)
			sum += abs(x2 - x1) + abs(y2 - y1)
	return sum


def main():
	rows, cols = 3, 3	#define 3x3 board

	g = lambda n: n._path_cost
	h = lambda n: manhattan_dist(n._state, goal_state) 
	f = lambda n: g(n) + h(n)

	initial_state = generate_state(rows, cols)
	goal_state = [
		[1,2,3],
		[4,5,6],
		[7,8,0]
	]


	# verify goal state is achievable before running A*
	if inversion_parity(initial_state) == inversion_parity(goal_state):
		best_first_search(f, initial_state, goal_state)
	else:
		print('impossible goal')

if __name__ == '__main__':
	main()


'''
	garbage bin:


#print('f: ', f(current_node), 'g: ', current_node._path_cost, 'h: ', manhattan_dist(current_node._state, goal_state))
		#current_node.pretty_print()


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

	for y, row in enumerate(state):
			for x, col in enumerate(row):
				if state[y][x] != goal_state[y][x]:
					return False
# def __init__(self, state, action, parent, cost):



'''