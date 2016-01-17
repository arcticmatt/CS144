import simplejson as json
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
from numpy import cumsum

print 'Running Graph Properties script'

with open('net_sci_coauthorships.txt', 'r') as f:
    js_graph = json.load(f) # Dictionary of key-value pairs
G = nx.from_dict_of_lists(js_graph)

#### Plot histogram #### 
# Get degrees of all nodes, create sorted list
degrees = nx.degree(G).values()
plt.hist(degrees, bins=10, log=True)
plt.title('Degree Histogram')
plt.ylabel('Number of Nodes')
plt.xlabel('Degree')
# plt.show()
plt.savefig('degree_histogram.png')
plt.clf()

#### Plot cumulative distribution function #### 
cumsums = cumsum(degrees)
plt.plot(cumsums)
plt.title('Cumulative Node Degrees')
plt.ylabel('Cumulative Node Degree')
plt.xlabel('Number of Nodes')
# plt.show()
plt.savefig('degree_cumsum.png')

#### Compute average clustering coefficient ####
avg_clustering = nx.average_clustering(G)
print 'Average Clustering Coefficient = ', avg_clustering

#### Compute overall clustering coefficient #### 
overall_clustering = nx.transitivity(G)
print 'Overall Clustering Coefficient = ', overall_clustering

#### Compute the maximal diameter ####
maximal_diameter = nx.diameter(G)
print 'Maximal Diameter = ', maximal_diameter

#### Compute the average diameter #### 
# The diameter of G is the greatest distance between 2 vertices
# So for each vertex, we take the greatest distance to all other nodes
# And we average all those distances
distances = nx.eccentricity(G).values()
avg_diameter = sum(distances) / len(distances)
print 'Average diameter = ', avg_diameter
