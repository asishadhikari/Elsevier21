from PYGAD import pygad	
from SimulationParameters import *


#prepare parameters for GA instance





contents = []
user_equipments = []
clusters = []




''' Check the Preparing the ``fitness_func`` Parameter section 
for information about creating such a function.'''
def fitness_function(all_ue_caching_decisions, solution_ix):
	#if not all cached in a cluster, fitness 0
	# if size limit exceeded 0
	#else fitness sum of priority

	fail = True

	for ue in all_ue_caching_decisions:
		for content in ue:

	return 0 if fail else fitness 


def genetic_algo_decisions(edgeserver):
	return initial_ga_setup(edgeserver)


#pass in edgeserver instance
def initial_ga_setup(edgeserver):
	contents = edgeserver.contents
	user_equipments = edgeserver.user_equipments
	clusters = edgeserver.clusters




#create GA instance 






