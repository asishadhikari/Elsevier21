from PYGAD import pygad	
from SimulationParameters import *


#prepare parameters for pygad
fitness_function = fitness_function
num_generations = 50
num_parents_mating = 4

sol_per_pop = 8
num_genes = len(function_inputs)

init_range_low = -2
init_range_high = 5

parent_selection_type = "sss"
keep_parents = 1

crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = 10




def fitness_function(solution, solution_ix):
	pass



#create GA instance






