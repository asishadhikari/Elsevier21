from EdgeServer import *
from PlottingFunctions import *
from SimulationParameters import *
e = EdgeServer()

#plot priority vs content graph
plot_priority_vs_alpha(alpha=ALPHA,contents=e.contents)
