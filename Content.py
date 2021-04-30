from scipy.stats import expon


#Models Content Objects
class Content:
	def __init__(self,ix,num_content,alpha,average_content_size):
		s = 0
		for x in range(1,num_content+1):
			s = s +  ((1/x)**alpha)

		self.priority = (1/(ix **alpha)) / s
		self.ix = ix
		self.size= expon.rvs(average_content_size)


