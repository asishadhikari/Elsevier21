from SimulationEntitiesSetup import *
from SimulationFunctions import *
from PlottingFunctions import *
from SimulationParameters import *


import random

#list of cachable contents each with zipf priority
contents = create_content(num_content=NUM_CONTENT,alpha=ALPHA,average_content_size=AVERAGE_CONTENT_SIZE)
#list of user equipments active in a network
user_equipments = create_user_equipment(NUM_UE,UE_REQUEST_RATE,NUM_D2D_CLUSTERS)

num_rounds = 10

''' 
0 is power_priority, 1 is log_priority, and 2 is blind_priority. 
this can be accessed from the Content object o as o.priorities[priority_to_choose]
'''
priority_to_choose = 0



'''
1. Contents each with separate (unchanging) priority are in a network
2. For each content, based on the number of users in network, edge server determines number of caching nodes checking availability
3. The edge server then allocates cache to n available UEs
3. Number of UEs dropping all cache in an interval and becoming free is poisson distributed. To model user mobility
4. At end of each round, a UE accesses a content randomly based on its request rate 
5. In case of cache hit, cost is only d2d cost. In case of cache miss, cost is d2d cost + ran cost

'''

def get_available_ue(c):
	available_ue = []
	for u in user_equipments:
		if u.check_avilable(c.size, c.lower):
			available_ue.append(u)
	return available_ue



#returns the minimum and maximum of priority based on the 
# priority scheme chosen 
def min_max_priority():
	all_priorities = []
	#get priorities based on scheme chosen
	for c in contents:
		all_priorities.append(c.priorities[priority_to_choose])
	a = min(all_priorities)
	b = max(all_priorities)
	return(a,b)


#Sets the lower threshold for all contents
def set_lower_threshold():
	a,b = min_max_priority()	
	#scale priority in a uniform manner based on chosen priority
	for c in contents:
		c.lower = (c.priorities[priority_to_choose] - a) //(b-a) *NUM_CONTENT 


#Sets the number of ue to cached for each content
def set_num_ue_caching():
	a,b = min_max_priority()
	for c in content:
		c.num_ue_caching = (c.priorities[priority_to_choose] - a) //(b-a) *NUM_UE 

def allocate_ue_cache(available_ue,c):
	random_ues = random.sample(available_ue,c.num_ue_caching)
	for u in random_ues:
		u.allocate_cache(c)




def allocate_cache_from_ue():
	#Set a lower threshold for each content to be cached
	set_lower_threshold()
	
	#based on priority, set the number of ue that must cache each content
	set_num_ue_caching()

	for c in contents:
		#available ue to cache c
		available_ue = get_available_ue(c)
		allocate_ue_cache(available_ue,c)