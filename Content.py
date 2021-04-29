
#Models Content Objects
class Content:
	def __init__(self,ix,num_content,alpha):
		s = 0
		for x in range(1,num_content+1):
			s += (x ** (1/alpha)) 

		self.priority = ix/s 
