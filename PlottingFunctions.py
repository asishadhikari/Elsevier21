import pandas as pd
import numpy as np
import plotly.express as px


from SimulationParameters import *
from matplotlib import pyplot as plt


'''tutorial : https://howtothink.readthedocs.io/en/latest/PvL_H.html
	
'''
#plot the different priority graphs
def plot_priority_vs_alpha(alpha,contents):
	power_priority = []
	log_priority = []
	blind_priority = []
	content_ix = [x for x in range(NUM_CONTENT)]
	for c in contents:
		p = c.priorities
		power_priority.append(p[0])
		log_priority.append(p[1])
		blind_priority.append(p[2])

	# np.savetxt("./csv/priorities.csv",power_priority,delimiter=',')
	# np.savetxt("./csv/priorities.csv",log_priority,delimiter=',')
	# np.savetxt("./csv/priorities.csv",blind_priority,delimiter=',')
	

	np.savetxt("./csv/priorities.csv",(power_priority,log_priority,blind_priority),delimiter=',')
	



	plt.plot(power_priority, label='power priority',c='r')
	plt.plot(log_priority,label = 'log_priority',c= 'b')
	plt.plot(blind_priority,label= 'same priority')
	plt.xlabel("Content index")
	plt.ylabel("Priority")
	plt.legend()

	plt.show()


def csv_ran_cost_vs_alpha(ALPHA, user_equipments,c_ran):
	costs = []
	costs.append([len(user_equipments),c_ran, ALPHA])
	df = pd.DataFrame(np.array(costs),columns=['num_ue','cost', 'alpha'])
	file_name = '_temp_num_ue_vs_cost.csv'
	with open(file_name, 'a') as f:
		df.to_csv(f,header=False)  











def plot_zipf_priority_vs_alpha(alpha,contents):
	priority_vector = []
	for c in contents:
		priority_vector.append([c.zipf_priority,alpha])

	#priority_vector =  np.append(priority_vector, axis=0)
	df = pd.DataFrame(np.array(priority_vector),columns=['zipf_priority', 'alpha'])
	file_name = 'zipf_priority.csv'
	with open(file_name, 'a') as f:
		df.to_csv(f,header=False)  





def write_csv_alpha_vs_zipf_priority(contents):
	data = []
	for c in contents:
		data.append(c.zipf_priority)
	data = np.asarray(data)
	np.savetxt("priorityVariation.csv",data)


def plot_with_plotly():
	df = pd.read_csv('priorityVariation.csv')
	fig = px.line(df)
	fig.show()




