import copy

class Node(object):
	'''
		Represents a node of the n-puzzle game
		_state: [
					[1,2,3],
					[4,5,6],
					[7,8,0]
				], where 0 represents the blank tile
		_parent: parent node in the game tree
		_path_cost: total cost to generate this node
		_action: the action the parent took to generate this node
	'''

	actions = [		#(+/-y, +/-x)
		(0,1),		#right
		(0,-1),		#left
		(1,0),		#up
		(-1,0)		#down
	]
	width = 0
	height = 0

	def generate_successors(self):
		successors = []
		b_x, b_y = self._blank_tile_pos()
		for move_y, move_x in Node.actions:
			#validate in bounds move
			if (move_y, move_x) != self._action and self._in_bounds(b_x + move_x, b_y + move_y):
				successor_state = self._swap(b_x + move_x,
										b_y + move_y,
										b_x, 
										b_y,
										copy.deepcopy(self._state))
				#reverse move so that we do not reverse to parent node
				successor_node = Node(successor_state, (move_y, move_x), self, self._path_cost + 1)
				successors.append(successor_node)
		return successors

				
	def _blank_tile_pos(self):
		for y, row in enumerate(self._state):
			for x, col in enumerate(row):
				if col == 0:
					return x, y
		return None

	def _swap(self, x1, y1, x2, y2, state):
		temp = state[y1][x1]
		state[y1][x1] = state[y2][x2]
		state[y2][x2] = temp
		return state

	def _in_bounds(self, x1, y1):
		return (0 <= x1 < len(self._state[0])) and (0 <= y1 < len(self._state))

	def pretty_print(self):
		for row in self._state:
			print(row)

	def __init__(self, state, action, parent, cost):
		self._state = state
		self._parent = parent
		self._path_cost = cost
		if action:
		  self._action = -1 * action[0], -1 * action[1] #reverse the move so we do not generate parent
		else:
		  self._action = action


