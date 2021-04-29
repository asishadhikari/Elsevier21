from scipy.stats import expon, randint
from UserEquipment import UserEquipment
from Content import Content


'''SIMULATION PARAMETERS'''

#Object priority profile (0-5)
ALPHA = 5

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



#create cache content
content = [Content(ix=x+1, num_content=NUM_CONTENT,alpha=ALPHA) for x in range(NUM_CONTENT)]

#create clusters 
clusters = [[] for x in range(NUM_D2D_CLUSTERS)]


request_size = expon.rvs(scale=UE_REQUEST_RATE,size=NUM_UE)
#create UEs
user_equipments = [UserEquipment(request_size[i]) for i in range(NUM_UE)]



#Assign users randomly and uniformly to clusters
cluster_id_generator = randint.rvs(0,NUM_D2D_CLUSTERS,size=NUM_UE)

assert(len(cluster_id_generator) == len(user_equipments))

for i in range(len(cluster_id_generator)):
	clusters[cluster_id_generator[i]].append(user_equipments[i])




