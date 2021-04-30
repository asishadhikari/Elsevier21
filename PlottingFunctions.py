import pandas as pd
import numpy as np
import plotly.express as px



def plot_zipf_priority_vs_alpha(alpha,contents):
	priority_vector = []
	for c in contents:
		priority_vector.append([c.zipf_priority,alpha])

	#priority_vector =  np.append(priority_vector, axis=0)
	df = pd.DataFrame(np.array(priority_vector),columns=['zipf_priority', 'alpha'])
	file_name = 'zipf_priority.csv'
	with open(file_name, 'a') as f:
		df.to_csv(f,header=False)  


def plot_ran_cost_vs_alpha(ALPHA, user_equipments,c_ran):
	costs = []
	costs.append([len(user_equipments),c_ran, ALPHA])
	df = pd.DataFrame(np.array(costs),columns=['num_ue','cost', 'alpha'])
	file_name = 'num_ue_vs_cost.csv'
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







