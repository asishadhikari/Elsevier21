'''SIMULATION PARAMETERS'''
#number of caching rounds to run simulation
NUM_ROUNDS = 10

#Object priority profile (5)  #1.1 gives nice graph
ALPHA = 0.8


#0 => power_priority 1=>log_priority, 2=> blind_priority
PRIORITY_TO_CHOOSE = 2

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

#Average cache space avilable at a UE (for uniform distribution)
AVERAGE_UE_CACHE_SPACE = AVERAGE_CONTENT_SIZE *100
#used to map actual storage space as uniform distribution
CACHE_DIFFERENCE_RANGE = 0.2

UPPER_THRESHOLD = NUM_CONTENT



'''DONE SIMULATION PARAMETERS'''
