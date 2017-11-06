from node import Node
from minimax import alpha_beta_search
import copy
import argparse

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

def print_game(node):
	'''
	Prints game board as
	<pile> : <count>
	1 : 2
	2 : 1290
	3 : 1
	...
	return: None
	'''
	print('-- Piles --')
	for pile, count in node._state.items():
		print('{} : {}'.format(pile, count))
	print('')

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

def get_parser():
	'''
	Returns a cli argument parser for the game
	return: ArgumentParser
	'''
	parser = argparse.ArgumentParser(description='Play a game of nim')
	parser.add_argument('--piles',
		help='<pile1 count> <pile2 count> ... <pileN count>',
		metavar='<pile count>',
		type=int,
		nargs='+',
		required=True
		)
	parser.add_argument('--first-move',
		help='human or computer',
		metavar='<player>',
		choices=['human', 'computer'],
		required=True
		)
	return parser

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

def main():
	#setup the game
	parser = get_parser()
	args = vars(parser.parse_args())
	board = build_board(args['piles'])
	player = args['first_move']
	next_player = {
		'computer' : 'human',
		'human' : 'computer'
	}

	#TODO: Add setup for first move!
	game_over = False
	pile, move = 0, 0


	start = Node(board, player, None, None)
	value, cursor = alpha_beta_search(start)

	while not game_over:
		print ('[node value] ', cursor._value)

		print_game(cursor)
		if player == 'computer':
			cursor = computer_move(cursor)
			pile, move = cursor._action
			print('computer move: {} {}'.format(pile, move))
		elif player == 'human':
			pile, move = get_move(cursor._state)
			cursor = player_move(pile, move, cursor)

		if not cursor:
			print('[sys err] the cursor is null')
			exit(-1)

		if cursor.is_terminal():
			print('{} wins'.format(next_player[player]))
			game_over = True

		player = next_player[player]


if __name__ == '__main__':
	main()