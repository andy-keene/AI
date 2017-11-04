import random
from random import shuffle

flatten = lambda x,y: x+y

def is_equal(state, goal_state):
	'''
	Returns whether state == goal_state
	'''
	if len(state) != len(goal_state) or len(state[0]) != len(goal_state[0]):
		return False
	else:
		return reduce(flatten, state) == reduce(flatten, goal_state)


def position(state, element):
	'''
	Returns [i][j] coordinates of element as row, col
	'''
	row = [n for n in state if element in n][0]
	return row.index(element), state.index(row)

def generate_state(rows, cols):
	'''
	Returns a state of randomly distributed tiles for a 
	rows x cols game board, such as:
	[
	    #c1, c2, c3
		[3, 1, 4], #r1
		[2, 5, 6], #r2
		[0. 7, 8]  #r3
	]
	'''
	tiles = range(0, cols * rows)
	shuffle(tiles)
	print(tiles)
	return [tiles[i*cols:(i+1)*cols] for i in range(0, rows)]

def inversion_parity(state):
	'''
	Returns parity of the number of inversions for the given state
	*See proof regarding n-puzzle distinct subsets for states

	ex: [ 
			[4,3],
			[1,0],
		]
	has 3 inversions => odd (1) parity
	Note: this could be done using only list comprehensions, but is more readable
	this way
	'''
	tiles = reduce(flatten, state)
	inversion_count = 0
	for i, tile in enumerate(tiles):
		if tile != 0:
			inversion_count += sum([1 for previous_tile in tiles[:i] if previous_tile > tile])
	return inversion_count % 2

def print_path(node):
	'''
	Print path from initial state => goal state
	'''
	if not node:
		return	#base case
	else:
		print_path(node._parent)
		print('\npath cost: {}'.format(node._path_cost))
		node.pretty_print()
