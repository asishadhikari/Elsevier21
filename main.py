from SimulationEntitiesSetup import *
from SimulationFunctions import *
from PlottingFunctions import *
from SimulationParameters import *

#list of cachable contents each with zipf priority
contents = create_content(num_content=NUM_CONTENT,alpha=ALPHA,average_content_size=AVERAGE_CONTENT_SIZE)

#list of user equipments active in a network
user_equipments = create_user_equipment(num_ue=NUM_UE,ue_request_rate = UE_REQUEST_RATE,
	num_d2d_clusters=NUM_D2D_CLUSTERS)


'''Call some simulation functions'''
# write_csv_alpha_vs_zipf_priority(contents)
# plot_with_plotly()
#Already have enough data
#plot_zipf_priority_vs_alpha(alpha=ALPHA,contents=contents)


contact_rate_matrix = calculate_ue_contact_rate_matrix(user_equipments=user_equipments,ue_contact_rate=UE_CONTACT_RATE)

clusters = create_clusters(user_equipments, NUM_D2D_CLUSTERS)


#probability that content is found within the network
p_d2d = calculate_p_d2d(CACHE_RETENTION_TIME,user_equipments,contact_rate_matrix)




#cost of using RAN for content access
c_ran = calculate_cost_ran(clusters,contents,p_d2d)





plot_ran_cost_vs_alpha(ALPHA, user_equipments,c_ran)






