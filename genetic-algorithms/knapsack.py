#version 0.0: uses list operations for more clarity
import random
from pregenerated_bags import knapsack1 as knapsack


def fitness(items, knapsack, max_weight=100):
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

def natural_selection(population, population_size=10, generations=200, fitness_function=None):
	'''
	Runs the the genetic algorithm as follows:

	- Randomly select a pair of parents to breed.
	- Pick a random spot for crossover, and breed two new children (with fitness computed). 
	- Randomly decide whether to mutate based on MutationPct, and if so, mutate one gene. 
	- Kill off the two weakest members of the population, to keep the size constant.

	Returns the most promising member of the population according to the fitness function
	'''
	population = generate_population(len(knapsack.keys()), population_size)
	population_bounds = population_size - 1 
	items_bounds = len(knapsack.keys()) - 1

	
	for generation in range(generations):
		mother = population[random.randint(0, population_bounds)]
		father = population[random.randint(0, population_bounds)]

		pivot_point = random.randint(1, items_bounds-1)
		first_child = mother[:pivot_point] + father[pivot_point:]
		second_child = father[:pivot_point] + mother[pivot_point:]

		#mutate 2/3 times
		if random.randint(0, 3) <= 2: 
			gene_mutation = random.randint(0, items_bounds)
			first_child[gene_mutation] = 1 - first_child[gene_mutation]

		if random.randint(0, 3) <= 2: 
			gene_mutation = random.randint(0, items_bounds)
			second_child[gene_mutation] = 1 - second_child[gene_mutation]

		#add to population
		population += [first_child, second_child]
		
		#kill the weak
		population = sorted(population, key=fitness_function, reverse=True)
		population = population[:population_bounds+1]
	print(population[0], 'fitness_function = ', fitness_function(population[0]))

def main():
	population_size = 100
	generations = 50000
	max_weight = 100

	
	gene_pool = generate_population()
	natural_selection(knapsack, 
		population_size=25,
		generations=500000,
		fitness_function=lambda n: fitness(n, knapsack, max_weight=100))


if __name__ == '__main__':
	main()




''''




		#print('child1: {}\nChild2: {}'.format(first_child, second_child))

'''
