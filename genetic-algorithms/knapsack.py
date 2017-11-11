#version 0.0: uses list operations for more clarity
import random
from pregenerated_bags import knapsack2 as knapsack


def fitness(items, knapsack, max_weight):
	'''
	Returns the value of the prospective item list if sum(items weight) <= max_weight
	else returns 0
	*Note: probably should change this function to enumerate over the knapsack
	'''
	value = weight = 0
	for i, included in enumerate(items):
		if included:
			weight += knapsack[i]['weight']
			value += knapsack[i]['value']
	return value if weight <= max_weight else 0

def generate_population(item_count, population_size):
	'''
	Returns a list of randomized item inclusions
	The index of the list corresponds to the item, where its value
	0 or 1 indicates whether it is included or not
	[
		[0,1,0, ... , 0],
		...
	] 
	'''
	return [
		[random.randint(0,1) for inclusion in range(0, item_count)]
		for item in range(0, population_size)
	]

def natural_selection(population, generations=200, fitness_function=lambda n: 0):
	'''
	Runs the the genetic algorithm as follows:

	- Randomly select a pair of parents to breed.
	- Pick a random spot for crossover, and breed two new children (with fitness computed). 
	- Randomly decide whether to mutate based on MutationPct, and if so, mutate one gene. 
	- Kill off the two weakest members of the population, to keep the size constant.

	Returns the most promising member of the population according to the fitness function
	'''
	population_bounds = len(population) - 1 
	gene_length = len(population[0]) - 1

	
	for generation in range(generations):
		mother = population[random.randint(0, population_bounds)]
		father = population[random.randint(0, population_bounds)]

		pivot_point = random.randint(1, gene_length-1)
		first_child = mother[:pivot_point] + father[pivot_point:]
		second_child = father[:pivot_point] + mother[pivot_point:]

		#mutate 2/3 times
		if random.randint(0, 3) <= 2: 
			gene_to_mutate = random.randint(0, gene_length)
			first_child[gene_to_mutate] = 1 - first_child[gene_to_mutate]

		if random.randint(0, 3) <= 2: 
			gene_to_mutate = random.randint(0, gene_length)
			second_child[gene_to_mutate] = 1 - second_child[gene_to_mutate]

		#add to population, and kill the weak
		#NOTE: this is NOT performant! O(n + nlog(n))
		population += [first_child, second_child]
		population = sorted(population, key=fitness_function, reverse=True)
		population = population[:population_bounds+1]

	return population[0]

def main():
	#tune parameters (import knapsack to namespace)
	population_size = 100
	generations = 200000
	max_weight = 20
	gene_pool = generate_population(len(knapsack.keys()), population_size)
	fitness_function = lambda n: fitness(n, knapsack, max_weight)

	fittest_canidate = natural_selection(gene_pool, generations, fitness_function)

	total_value = total_weight = 0
	for item, included in enumerate(fittest_canidate):
		if included:
			print('Item: {}, Weight: {}, Value: {}'.format(item, 
				knapsack[item]['weight'],
				knapsack[item]['value'])
			)
			total_weight += knapsack[item]['weight']
			total_value += knapsack[item]['value']
	
	print('Total weight: {}, Total value: {}, Valid? {}'.format(total_weight,
		total_value,
		'Yes' if total_weight <= max_weight else 'No!'))

if __name__ == '__main__':
	main()


''''
	GARBAGE BIN:
		#print('child1: {}\nChild2: {}'.format(first_child, second_child))

'''
