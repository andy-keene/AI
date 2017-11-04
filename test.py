from npuzzle import Node


state1 = [
			[1,2,3],
			[4,5,6],
			[7,8,0]
		]
state2 = [
			[1,2,0],
			[4,5,6],
			[7,8,3]
		]
state3 = [
			[0,2,3],
			[4,5,6],
			[7,8,1]
		]
state4 = [
			[1,2,3],
			[4,0,6],
			[7,8,5]
		]
state5 = [
			[1,2,3],
			[4,5,6],
			[0,8,7]
		]


test_states = [state1, state2, state3, state4, state5]

for s in test_states:
	node = Node(s, None, None, 0)
	print('\nbase state:')
	node.pretty_print()
	print('successors')
	for successor in node.generate_successors():
		successor.pretty_print()


node = Node(state1, None, None, 0)
for i in range(0, 10):
	print('state')
	node.pretty_print()

	node = node.generate_successors()[0]