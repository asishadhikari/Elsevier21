import numpy as np
import pandas as pd
from math import e
from scipy.stats import expon, randint
import scipy.integrate as integrate
from scipy.integrate import quad

#return uxu matrix of the 
def calculate_ue_contact_rate_matrix(user_equipments,ue_contact_rate):
	arr = []
	for x in range(len(user_equipments)):
		y = [expon.rvs(scale=ue_contact_rate) for z in range(len(user_equipments))]
		arr.append(y)
	return np.array(arr)


#return 2d cluster of users
def create_clusters(user_equipments,num_d2d_clusters):
	clusters = [[] for x in range(num_d2d_clusters)]
	for u in user_equipments:
		clusters[u.cluster].append(u) 
	return clusters

def integrand(t,user_equipments, contact_rate_matrix):
	s= 0
	for x in range(len(user_equipments)):
		for y in range(len(user_equipments)):
			s += contact_rate_matrix[x][y] / (e ** (user_equipments[x].request_rate + sum(contact_rate_matrix[x])) )* t 
	return s


#this implements equation (10) probability of cache hit at d2d level
def calculate_p_d2d(time,user_equipments,contact_rate_matrix ):
	return quad(integrand,0,time, args=(user_equipments,contact_rate_matrix))[0]



def calculate_cost_ran(clusters,contents,pd2d, normalizing_parameter=1):
	s = 0
	for c in clusters:
		t = 0 
		for o in contents:
			t += o.size * (1- pd2d)
		s += len(c) * t
	return normalizing_parameter * s
