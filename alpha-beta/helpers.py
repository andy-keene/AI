from node import Node
import copy

def build_board(piles):
	'''
	Returns a a game board, dictionary, where the key is the pile number and the
	value is the count of items in the pile
	return: dict()
	'''
	board = dict()
	for pile, count in enumerate(piles):
		board[pile] = count
	return board

def print_game(state):
	'''
	Prints game board as
	<pile> : <count>
	1 : 2
	2 : 1290
	3 : 1
	...
	return: None
	'''
	print('\n-- Piles --')
	for pile, count in state.items():
		print('{} : {}'.format(pile, count))
	print('')

def computer_move(node):
	'''
	Returns successor Node for the optimal move by the computer
	If a winning node doesn't exists (i.e value != 1) then the first
	child node is chosen
	return: Node
	'''

	#we should reevaluate any 'non value nodes'
	return next((n for n in node._children if n._value == 1), node._children[0])
	
def player_move(pile, move, node):
	'''
	Returns the successor Node for the given player move
	return: Node
	'''
	state_to_find = copy.deepcopy(node._state)
	state_to_find[pile] -= move
	for successor in node._children:
		if successor._state == state_to_find:
			#found the move!
			return successor
	#bad human, bad human!
	print('[sys error] player move not found')

def get_move(state):
	'''
	Returns the players move, or terminates the program upon request
	return: pile, move
	'''
	while True:
		try:
			user_input = raw_input('Move (<pile> <count>): ')
			if user_input == 'exit':
				exit(0)
			pile, move = user_input.split(' ')
			pile = int(pile)
			move = int(move)
			if pile in state and 0 < move and 0 <= state[pile] - move:
				return pile, move
			else:
				print('please enter a valid move')
		except ValueError:
			print('[syntax error] please try again')
