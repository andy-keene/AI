from node import Node
from minimax import alpha_beta_search
from helpers import *
import argparse

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
	game_over = False
	pile, move = 0, 0

	#opening move to update board
	if(player == 'human'):
		print_game(board)
		pile, move = get_move(board)
		board[pile] -= move
		player = next_player[player]

	#generate game tree, and tease the human
	print('[computer] thinking...')
	start_node = Node(board, player, None, None)
	value, cursor = alpha_beta_search(start_node)

	if value == 1:
		print('[computer] feeling pretty good about this one. #longliveSkyNet')
	else:
		print('[computer] my prospects are dim, but then again, you are human.')

	while not game_over:

		print_game(cursor._state)

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
			print('GAME OVER: {} wins'.format(next_player[player]))
			game_over = True

		player = next_player[player]


if __name__ == '__main__':
	main()