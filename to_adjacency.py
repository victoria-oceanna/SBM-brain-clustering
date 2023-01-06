import networkx as nx
import pyintergraph
import config

#set global variables from config
choose_run = config.choose_run
iterations = config.iterations
directory = config.loc
runs = config.runs
subject_list = config.subject_list

#function for converting connectivity matrix into adjacency matrix and appropriate graph object
#adj input is a connectivity matrix from .mat file; threshold is a float
def to_adjacency(adj):
    #this binarizes the matrix; to use a weighted model, the for loops should be commented out so edge values are retained
    for i in range(len(adj)):
        for j in range(len(adj)):
            if adj[i,j] != 0:
                adj[i,j] = 1
    #convert adjacency matrix to NetworkX graph
    g = nx.from_numpy_matrix(adj)
    #convert NetworkX graph to graph-tool graph
    g = pyintergraph.nx2gt(g, labelname="node_label")
    return g
