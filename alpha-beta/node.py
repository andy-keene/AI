import copy

class Node(object):
	'''
	Represents a node in the nim game tree
	Node.utility_map: a look up for the utility value for the terminal node of 
	each player

	_value: minimax value of this node
	_children: 
	_player: player representing the move *from* this state
	_state: the game board, such as:
		{
			<pile #> : count,
			...
		}
	_action: (pile, move) taken to get here 
	_parent: the generator of this game state

	'''
	utility_map = {
		'human': 0,
		'computer': 1
	}
	next_player = {
	#	'current': 'next to move'
		'human' : 'computer',
		'computer': 'human'
	}

	def generate_successors(self):
		self._children = []
		for pile, items in self._state.items():
			if items > 0:
				for move in range(1, items+1):
					copied_state = copy.deepcopy(self._state)
					copied_state[pile] -= move
					successor = Node(copied_state, Node.next_player[self._player], (pile, move), self)
					self._children.append(successor)
		return self._children

	def is_terminal(self):
		return sum(self._state.values()) == 0

	def utility_value(self):
		return Node.utility_map[self._player]

	def __init__(self, state, player=None, action=None, parent=None):
		self._value = None
		self._children = []
		self._player = player
		self._state = state
		self._action = action
		self._parent = parent