from node import Node
from minimax import alpha_beta_search
import copy

node = Node(state, 'player', None, None)
v, node = alpha_beta_search(node)
print('max value: ' + str(v))

for successor in node.generate_successors():
	print('successor ', successor._state, 'move', successor._player)
	for t in successor.generate_successors():
		print('       and its successors: ', t._state, 'move', t._player)
	if successor.is_terminal():
		print('terminl value', successor.utility_value())
		#v, temp = alpha_beta_search(successor)
		#print('v, temp', v, temp)


'''
	garbage bin:


if not optimal_move or not node._value:
		print('ERR: no optimal move in children is found, picking first one!')
		optimal_move = node._children[0]

	#print( 'node value... ', node._value)
	# cursor = current state of the game, a node


'''