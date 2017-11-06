from node import Node

pos_inf = float('inf')
neg_inf = float('-inf')



def alpha_beta_search(node):
	v = max_value(node, neg_inf, pos_inf)
	node._value = v
	return v, node

def max_value(node, alpha, beta):
	#print('in max player: ', node._player, ' state ', node._state)
	if node.is_terminal():
		return node.utility_value()
	
	v = neg_inf

	for successor in node.generate_successors():
		v = max(v, min_value(successor, alpha, beta))
		node._value = v
		if v >= beta:
			return v
		alpha = max(alpha, v)
	return v

def min_value(node, alpha, beta):
	#print('in min player: ', node._player, ' state ', node._state)
	if node.is_terminal():
		return node.utility_value()
	
	v = pos_inf

	for successor in node.generate_successors():
		v = min(v, max_value(successor, alpha, beta))
		node._value = v
		if v <= alpha:
			return v
		beta = min(beta, v)
	return v
	