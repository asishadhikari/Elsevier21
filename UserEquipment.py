from scipy.stats import expon, randint
from SimulationParameters import *
from scipy.stats import expon
from Content import Content

#models the User equipment
class UserEquipment:
	def __init__(self,ue_request_rate=UE_REQUEST_RATE,num_d2d_clusters=NUM_D2D_CLUSTERS):
		#uniform distribute clusters 
		self.cluster = randint.rvs(0,num_d2d_clusters)
		#exponential distribute request rate
		self.request_rate = expon.rvs(scale=ue_request_rate)
		self.storage_space = randint.rvs(
			AVERAGE_UE_CACHE_SPACE*(1- CACHE_DIFFERENCE_RANGE),AVERAGE_UE_CACHE_SPACE+(1 + CACHE_DIFFERENCE_RANGE))
		#Signalling 
		self.rand_num = randint.rvs(0,NUM_CONTENT)


	#must always be passed content type
	def allocate_cache(self,c: Content):
		if check_available(c):
			self.storage_space -= c.size

	#check if size and threshold criteria met. 
	#must be passed content type
	def check_available(self,c : Content):
		return self.storage_space >= c.size and self.rand_num <= c.lower

	def reset_cache(self):
		self.storage_space = randint.rvs(
			AVERAGE_UE_CACHE_SPACE*(1- CACHE_DIFFERENCE_RANGE),AVERAGE_UE_CACHE_SPACE+(1 + CACHE_DIFFERENCE_RANGE))


	def generate_request(self):
		s = 0
		for x in range(1,NUM_CONTENT+1):
			s = s +  ((1/x)**ALPHA)
		return round( (1/(ix **alpha)) / s )

	def calculate_zipf_priority(self,ix, num_content,alpha):
		s = 0
		for x in range(1,num_content+1):
			s = s +  ((1/x)**alpha)
		return (1/(ix **alpha)) / s


