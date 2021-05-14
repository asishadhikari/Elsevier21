import numpy as np
from PYGAD import pygad	
from SimulationParameters import *




#Global variables to be used by fitness function
contents = []
user_equipments = []
clusters = []


''' Check the Preparing the ``fitness_func`` Parameter section 
for information about creating such a function.'''
def fitness_function(solution, solution_ix):
	#if not all cached in a cluster, fitness 0
	# if size limit exceeded 0
	#else fitness sum of priority

	#fitness criteria dependent on cluster, and ue cache space
	fail = False

	#convert the 1D solution vector to 2D so that we can easily use
	ue_caching_decisions = np.reshape(solution, (len(user_equipments),len(contents), 'c' ))

	#Make sure that the solutions vector has been transformed properly
	assert len(ue_caching_decisions) == NUM_UE
	assert len(ue_caching_decisions[0])== NUM_CONTENT

	








	return 0 if fail else fitness 


def genetic_algo_decisions(edgeserver):
	return initial_ga_setup(edgeserver)


#pass in edgeserver instance
def initial_ga_setup(edgeserver):
	contents = edgeserver.contents
	user_equipments = edgeserver.user_equipments
	clusters = edgeserver.clusters
	edgeserver = edgeserver

	#GA parameters

	num_generations=100
	num_parents_mating=10
	fitness_func=fitness_function
	sol_per_pop=20
	num_genes=len(user_equipments)* len(contents)
	gene_type = int
	init_range_low=0
	init_range_high=1
	mutation_probability = 0.3
	mutation_by_replacement=True
	random_mutation_min_val = 0
	mutation_type="random"
	parent_selection="sss"
	keep_parents=-1
	crossover_type="single_point"
	random_mutation_min_val=0.0
	random_mutation_max_val=1.0
	save_best_solutions=True
	gene_space = [0,1]




	'''unused GA params:
		crossover_probability
		mutation_percent_genes
		mutation_num_genes
		random_mutation_max_val





#create GA instance 






