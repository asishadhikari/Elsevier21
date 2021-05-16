from EdgeServer import *
from PlottingFunctions import *
from SimulationParameters import *
from SimulationFunctions import *
import math
from scipy.integrate import quad

#EdgeServer variable for simulation
edgeserver = EdgeServer()
user_equipments = edgeserver.user_equipments
contents = edgeserver.contents
clusters = edgeserver.clusters

contact_rate_matrix = calculate_ue_contact_rate_matrix(user_equipments=user_equipments,ue_contact_rate=UE_CONTACT_RATE)

'''Todo
	1. [X] Plot priority vs content graph
	2. [X] Plot num_ue (changing) ,cost,alpha
	3. [ ] Plot GA convergence


'''

	# 1. [X] Plot priority vs content graph
#plot_priority_vs_alpha(alpha=ALPHA,contents=contents)


	# 2. [X] plot num_ue, cost, and alpha 
#cost of using RAN for content access
'''
p_d2d = calculate_p_d2d(contents)
assert(p_d2d>=0 and p_d2d <=1)
c_ran = calculate_cost_ran(clusters,contents,p_d2d)
csv_ran_cost_vs_alpha(ALPHA, user_equipments,c_ran)
'''

	#3. [ ] Plot GA convergence
ga_instance = edgeserver.allocate_cache_from_ue_and_return_ga()







