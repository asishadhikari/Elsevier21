from SimulationFunctions import *
from SimulationEntitiesSetup import *

'''SIMULATION PARAMETERS'''

#Object priority profile (5)  #1.1 gives nice graph
ALPHA = 1.1

#number of UEs in the network (100-300)
NUM_UE = 100

#number of contents (20)
NUM_CONTENT =  20

#number of D2D clusters (4)
NUM_D2D_CLUSTERS = 4

# lambda_x the user content access request rate (0.05)
UE_REQUEST_RATE = 0.05

#mean contact rate between two users (0.05 - 0.25)
UE_CONTACT_RATE = 0.25

AVERAGE_CONTENT_SIZE = 0.2


#500 ms
CACHE_RETENTION_TIME = 500

'''DONE SIMULATION PARAMETERS'''


#list of cachable contents each with zipf priority
contents = create_content(num_content=NUM_CONTENT,alpha=ALPHA,average_content_size=AVERAGE_CONTENT_SIZE)

#list of user equipments active in a network
user_equipments = create_user_equipment(num_ue=NUM_UE,ue_request_rate = UE_REQUEST_RATE,
	num_d2d_clusters=NUM_D2D_CLUSTERS)


'''Call some simulation functions'''
#write_csv_alpha_vs_priority(contents)
#plot_with_plotly()


contact_rate_matrix = calculate_ue_contact_rate_matrix(user_equipments=user_equipments,
	ue_contact_rate=UE_CONTACT_RATE)

clusters = create_clusters(user_equipments, NUM_D2D_CLUSTERS)


p_d2d = calculate_p_d2d(CACHE_RETENTION_TIME,user_equipments,contact_rate_matrix)











