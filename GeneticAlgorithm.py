import numpy as np
from PYGAD import pygad	
from SimulationParameters import *




#Global variables to be used by fitness function
# contents = []
# user_equipments = []
# clusters = []




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

					#  # ue asked to cache but does not want to cache return 0
					# if not user_equipments[ue_ix].check_available(contents[content_ix]):
					# 	return 0

					ue_cluster = user_equipments[ue_ix].cluster
					#indicate in the appropriate cluster index that the service has been cached
					cluster_caching_decisions[ue_cluster][content_ix] = 1

		#fitness is 0 if a content is not cached in all clusters
		cluster_caching_decisions = cluster_caching_decisions.flatten()
		for d in cluster_caching_decisions:
			if not d:
				return 0

		return priority_score



	#create ga_instance
	ga_instance = pygad.GA(
		num_generations=100,
		gene_type=int,
		gene_space=[0,1],
		num_parents_mating=10,
		fitness_func=fitness_function,
		sol_per_pop=20,
		num_genes=len(user_equipments)* len(contents),
		init_range_low=0,
		init_range_high=1,
		mutation_probability = 0.5,
		mutation_by_replacement=True,
		mutation_type="random", 
		parent_selection_type="tournament",
		keep_parents=-1,
		crossover_type="single_point",
		
		)

	ga_instance.run()
	ga_instance.plot_result()

	return ga_instance
		



	'''unused GA params:
		crossover_probability
		gene_type
		gene_space = [0,1]
		save_best_solutions
		mutation_percent_genes
		mutation_num_genes
		random_mutation_max_val


	'''
