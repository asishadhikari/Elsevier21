from scipy.stats import expon, randint
from UserEquipment import UserEquipment
from SimulationFunctions import *
from SimulationEntitiesSetup import *

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

'''DONE SIMULATION PARAMETERS'''


#list of cachable contents each with zipf priority
contents = create_content(num_content=NUM_CONTENT,alpha=ALPHA)

#list of user equipments active in a network
user_equipments = create_user_equipment(num_ue=NUM_UE,ue_request_rate = UE_REQUEST_RATE, num_d2d_clusters=NUM_D2D_CLUSTERS)










