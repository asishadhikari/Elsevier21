from scipy.stats import expon, randint
from UserEquipment import UserEquipment
from Content import Content


#return a list of cachable content objects
def create_content(num_content,alpha):
	content = [Content(ix=x+1, num_content=num_content,alpha=alpha) for x in range(num_content)]
	return content

#return list of user equipements active connected to a edge server
def create_user_equipment(num_ue,ue_request_rate,num_d2d_clusters):
	request_size = expon.rvs(scale=ue_request_rate,size=num_ue)

	#create UEs
	user_equipments = \
	[UserEquipment(ue_request_rate=ue_request_rate,num_d2d_clusters=num_d2d_clusters) for i in range(num_ue)]

	return user_equipments



