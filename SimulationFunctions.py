import numpy as np
import pandas as pd
from math import e , pow
from scipy.stats import expon, randint,uniform
import scipy.integrate as integrate
from scipy.integrate import quad

from SimulationParameters import *
#return uxu matrix of the 
def calculate_ue_contact_rate_matrix(user_equipments,ue_contact_rate=UE_CONTACT_RATE):
	arr = []
	for x in range(len(user_equipments)):
		t = []
		for y in range(len(user_equipments)):
			#v = 0 if user_equipments[x].cluster != user_equipments[y].cluster else expon.rvs(scale=ue_contact_rate) 
			v = 0 if user_equipments[x].cluster != user_equipments[y].cluster else uniform.rvs(UE_CONTACT_RATE/2,UE_CONTACT_RATE*2)
			t.append(v)
		arr.append(t)
	return np.array(arr)


#return 2d cluster of users
def get_ue_clusters(user_equipments,num_d2d_clusters=NUM_D2D_CLUSTERS):
	clusters = [[] for x in range(num_d2d_clusters)]
	for u in user_equipments:
		clusters[u.cluster].append(u) 
	return clusters

def integrand(t,user_equipments, contact_rate_matrix):
	s= 0
	for x in range(len(user_equipments)):
		for y in range(len(user_equipments)):
			lij = contact_rate_matrix[x][y]
			#s += lij / (e ** ((user_equipments[x].request_rate + sum(contact_rate_matrix[x])) * t))
			if lij:
				s += pow(e, -((1/user_equipments[x].request_rate + 1/sum(contact_rate_matrix[x])) * t)) /lij
	return s


#this implements equation (10) probability of cache hit at d2d level
def calculate_p_d2d(user_equipments,contact_rate_matrix, time=CACHE_RETENTION_TIME ):
	#assert(p_d2d>=0 and p_d2d <=1)
	
	return quad(integrand,1,time, args=(user_equipments,contact_rate_matrix))[0]



def calculate_cost_ran(clusters,contents,pd2d, normalizing_parameter=RAN_COST_NORMALIZING_PARAMETER):
	s = 0
	for c in clusters:
		t = 0 
		for o in contents:
			#time cost wrt to 
			t += o.size * (1- pd2d)
		s += len(c) * t
	return normalizing_parameter * s



#returns the minimum and maximum of priority based on the 
# priority scheme chosen
'''helper function unrelated to EdgeServer'''
def min_max_priority(contents, priority_to_choose):
	all_priorities = []
	#get priorities based on scheme chosen
	for c in contents:
		all_priorities.append(c.priorities[priority_to_choose])
	a = min(all_priorities)
	b = max(all_priorities)
	return(a,b)

