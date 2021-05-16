from EdgeServer import *
from PlottingFunctions import *
from SimulationParameters import *
from SimulationFunctions import *
import math
from scipy.integrate import quad

#EdgeServer variable for simulation
e = EdgeServer()
user_equipments = e.user_equipments
contents = e.contents
clusters = e.clusters

contact_rate_matrix = calculate_ue_contact_rate_matrix(user_equipments=user_equipments,ue_contact_rate=UE_CONTACT_RATE)
#probability that content is found within the network ?????

p_d2d = integrand(1,user_equipments, contact_rate_matrix)
assert(p_d2d>=0 and p_d2d <=1)


'''Todo
	1. [X] Plot priority vs content graph
	2. [ ] Plot num_ue (changing) ,cost,alpha


'''

	# 1. [.] Plot priority vs content graph
#plot_priority_vs_alpha(alpha=ALPHA,contents=contents)


	# 2. [ ] plot num_ue, cost, and alpha 

#cost of using RAN for content access
c_ran = calculate_cost_ran(clusters,contents,p_d2d)
csv_ran_cost_vs_alpha(ALPHA, user_equipments,c_ran)








