from SimulationEntitiesSetup import *
from SimulationFunctions import *
from PlottingFunctions import *
from SimulationParameters import *
from GeneticAlgorithm import *

import random



class EdgeServer:
	'''
		1. Contents each with separate (unchanging) priority are in a network
		2. For each content, based on the number of users in network, edge server determines number of caching nodes checking availability
		3. The edge server then allocates cache to n available UEs
		3. Number of UEs dropping all cache in an interval and becoming free is poisson distributed. To model user mobility
		4. At end of each round, a UE accesses a content randomly based on its request rate 
		5. In case of cache hit, cost is only d2d cost. In case of cache miss, cost is d2d cost + ran cost

	'''

	def __init__(self):
		#list of cachable contents each with zipf priority
		self.contents = create_content(num_content=NUM_CONTENT,alpha=ALPHA,average_content_size=AVERAGE_CONTENT_SIZE)
		#list of user equipments served by edge server
		self.user_equipments = create_user_equipment(NUM_UE,UE_REQUEST_RATE,NUM_D2D_CLUSTERS)
		self.clusters = get_ue_clusters(self.user_equipments, NUM_D2D_CLUSTERS)



	#return list of UEs available to cache content c	
	def get_available_ue(self,c):
		available_ue = []
		for u in self.user_equipments:
			if u.check_available(c):
				available_ue.append(u)
		return available_ue


	#Allocate cache based on priority selected for all Contents
	def allocate_cache_from_ue(self, priority_to_choose=PRIORITY_TO_CHOOSE):
		contents = self.contents
		#lowest and highest priority from contents
		lower,upper = min_max_priority(contents,priority_to_choose)

		#ask UEs to set their priority threshold based on priorities observed
		for u in self.user_equipments:
			u.signal_rand_num_to_server(lower,upper)	

		
		

		#set lower threshold for caching and determine number of ues that will cache 
		#	each content
		for c in contents:
			c.num_ue_caching = (c.priorities[priority_to_choose] - lower) //(upper-lower) *NUM_UE 
			c.lower = (c.priorities[priority_to_choose] - lower) //(upper-lower) *NUM_CONTENT 
			#based on decisions made, get list of ALL available ues that will cache
			available_ue = self.get_available_ue(c)
			#select randomly the number of UEs chosen to cache from all avilable UEs
			random_ues = random.sample(available_ue,c.num_ue_caching)
			#allocate cache stroage from c.num_ue_caching UEs
			for u in random_ues:
				u.allocate_cache(c)





 