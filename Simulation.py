from SimulationEntitiesSetup import *
from SimulationFunctions import *
from PlottingFunctions import *
from SimulationParameters import *


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
		if u.check_avilable(c.size, c.lower)
			available_ue.append(u)
	return available_ue



# Attaches allocable_num_ue to each UE object so that it can be used later 
def calculate_num_ue():
	all_priorities = []
	#get priorities based on scheme chosen
	for c in contents:
		all_priorities.append(c.priorities[priority_to_choose])
	
	b = max(all_priorities)
	a = min(all_priorities)

	#scale priority in a uniform manner based on chosen priority
	for c in contents:
		c.lower = (c.priorities[priority_to_choose] - a) //(b-a) *NUM_CONTENT 

		

def allocate_cache_from_ue():
	#adds allocable_num_ue attribute to each content
	calculate_num_ue()
	for c in contents:
		available_ue = get_available_ue(c)
		for u in available_ue:
			pass
