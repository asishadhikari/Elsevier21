from scipy.stats import expon
from SimulationParameters import *
import math

#used for power function must be in range [0,1]
k = 0.5

#Models Content Objects
class Content:
	def __init__(self,ix,num_content,alpha,average_content_size):

		self.zipf_priority = self.calculate_zipf_priority(ix,num_content,alpha) 
		power_priority = math.pow(self.zipf_priority,k)
		log_priority = math.log(self.zipf_priority) 
		blind_priority = NUM_UE//NUM_CONTENT
		self.priorities = [power_priority, log_priority,blind_priority]
		
		#index -> lower index is higher priority 
		self.ix = ix

		#content size
		self.size= expon.rvs(average_content_size)

		#changed later when priority base scheduling
		self.lower = NUM_CONTENT
		
		#this must be integer type
		self.num_ue_caching = 0


	def calculate_zipf_priority(self,ix, num_content,alpha):
		s = 0
		for x in range(1,num_content+1):
			s = s +  ((1/x)**alpha)
		return (1/(ix **alpha)) / s