import networkx as nx
import pyintergraph
import config

#set global variables from config
choose_run = config.choose_run
threshold = config.threshold
file_names = config.file_names
iterations = config.iterations
directory = config.loc 

#function for converting connectivity matrix into adjacency matrix and appropriate graph object
#adj input is a connectivity matrix from .mat file; threshold is a float
def to_adjacency(adj, threshold):
    for i in range(len(adj)):
        for j in range(len(adj)):
            #for each entry, if value is less than or equal to the threshold, it will be zeroed
            if adj[i,j] <= threshold:
                adj[i,j] = 0
            #if any entries are NaN, print error message
            elif adj[i,j] == "NaN":
                print("Unknown connection")
            #for all entries above threshold, replace value with 1
            else:
                adj[i,j] = 1
    #convert adjacency matrix to NetworkX graph
    g = nx.from_numpy_matrix(adj)
    #convert NetworkX graph to graph-tool graph
    g = pyintergraph.nx2gt(g, labelname="node_label")
    return g

