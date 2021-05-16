import numpy as np
from PYGAD import pygad	
from SimulationParameters import *


def genetic_algo_decisions(edgeserver):
	return initial_ga_setup(edgeserver)


#pass in edgeserver instance
def initial_ga_setup(edgeserver):
	contents = edgeserver.contents
	user_equipments = edgeserver.user_equipments
	clusters = edgeserver.clusters
	edgeserver = edgeserver

	''' Check the Preparing the ``fitness_func`` Parameter section 
	for information about creating such a function.'''
	def fitness_function(solution, solution_ix):
		'''ToDo:
		[X]   if not all cached in a cluster, fitness 0
		[X] if a user not ready to cache a content and asked, fitness 0 
		[X]   if size limit exceeded 0
		[X]  else fitness sum of priority
		
		'''

		#fitness criteria dependent on cluster, and ue cache space
		fail = False

		#convert the 1D solution vector to 2D so that we can easily use
		ue_caching_decisions = np.reshape(solution, (NUM_UE,NUM_CONTENT), 'c')


		#Make sure that the solutions vector has been transformed properly
		assert len(ue_caching_decisions) == NUM_UE
		assert len(ue_caching_decisions[0])== NUM_CONTENT


		#2d array to represent contents being cached across different clusters. Value 0 or 1 (cached)
		cluster_caching_decisions = [[0 for x in range(NUM_CONTENT)] for c in range(NUM_D2D_CLUSTERS)]
		cluster_caching_decisions = np.asarray(cluster_caching_decisions)

		#used to track net priority based gain
		priority_score = 0

		#check if ue not ready to cache a content
		for ue_ix in range(NUM_UE):
			ue_cache_used = 0
			for content_ix in range(NUM_CONTENT):
				#content_ix is cached at ue_ix 
				if ue_caching_decisions[ue_ix][content_ix]:
					#update the cache storage used at ue for the decision
					ue_cache_used += contents[content_ix].size
					
					#update priority score
					priority_score += contents[content_ix].priorities[PRIORITY_TO_CHOOSE]

					#if more cache space asked for user than available return 0
					if ue_cache_used > user_equipments[ue_ix].storage_space:
						return 0


					#????
					# #  # ue asked to cache but does not want to cache return 0
					if not user_equipments[ue_ix].check_available(contents[content_ix]):
						return 0	

					ue_cluster = user_equipments[ue_ix].cluster
					#indicate in the appropriate cluster index that the service has been cached
					cluster_caching_decisions[ue_cluster][content_ix] = 1

		#fitness is 0 if a content is not cached in all clusters
		cluster_caching_decisions = cluster_caching_decisions.flatten()
		for d in cluster_caching_decisions:
			if not d:
				return 0

		return 1/priority_score




	'''unused GA params:
		initial_population
		gene_type
		gene_space = [0,1]
		save_best_solutions
		mutation_percent_genes
		mutation_num_genes
		random_mutation_min_val
		random_mutation_max_val
		init_range_low=0,
		init_range_high=1,
		K_tournament,

		delay_after_gen=0.0:
		suppress_warnings=False



		

	parent_selection_type="sss": The parent selection type. Supported types are 
		sss (for steady-state selection), 
		rws (for roulette wheel selection), 
		sus (for stochastic universal selection), 
		rank (for rank selection), 
		random (for random selection), 
		and tournament (for tournament selection).

	crossover_type="single_point"
		supported:
			two_points,  uniform,  scattered,   None (no crossover)

	???not clear if some of the second params in callback are list or single
	callback functions:
		on_start = f(ga_instance)  called only once at start before evolution
		on_fitness = f(ga_instance, list_fitness_values) 
				-> called after canculating fitness values of all soln
		on_parents= f(ga_instance, list_selected_parents)
				-> called after selecting parents that mate
		on_crossover = f(ga_instance, list_offspring_from_crossover)
				-> called after crossover is applied to a generation
		on_mutation = f(ga_instance, offspring_generated_after_mutation)
				-> called each time mutation operation is applied
		on_generation = f(ga_instance)
				-> called after each generation. 
				-> if returns stop, GA.run() stops at cur generation

		@deprecated : callback_generation
		callback_generation=f(ga_instance)
				-> called after each generation
				-> if returns stop, GA.run() stops at current generation
	'''


	#create ga_instance
	ga_instance = pygad.GA(
		num_generations=100,
		sol_per_pop=20,
		num_parents_mating=10,
		keep_parents=0,
		parent_selection_type="sss",
		crossover_probability = 0.9,
		crossover_type="single_point",
		gene_type=int,
		gene_space=[0,1],
		fitness_func=fitness_function,
		num_genes=len(user_equipments)* len(contents),
		mutation_probability = 0.5,
		mutation_by_replacement=True,
		mutation_type="random", 
		allow_duplicate_genes=False
		)

	ga_instance.run()
	ga_instance.plot_result()

	return ga_instance
		




#Good result params:
