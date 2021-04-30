from scipy.stats import expon, randint

#models the User equipment
class UserEquipment:
	def __init__(self,ue_request_rate,num_d2d_clusters):
		#uniform distribute clusters
		self.cluster = randint.rvs(0,num_d2d_clusters)
		#exponential distribute request rate
		self.request_rate = expon.rvs(scale=ue_request_rate)

