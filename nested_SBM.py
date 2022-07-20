import to_adjacency
from graph_tool import centrality, draw, inference, clustering, generation, search, stats, topology
import graph_tool as gt
import networkx as nx
import numpy as np

# function for obtaining nSBM partition
def nested_SBM(adj, threshold, iterations):
    #convert connectivity matrix to graph
    g = to_adjacency(adj, threshold)
    
    #find an intial state
    state = inference.minimize_nested_blockmodel_dl(g, deg_corr=True)
    
    #call algorithm for desired number of iterations
    for i in range(0, iterations):
        #save state of recalled algorithm
        state_new = inference.minimize_nested_blockmodel_dl(g, deg_corr=True)
        #retain the state with the lower entropy value - ie. the better fit
        if state_new.entropy() < state.entropy():
            state = state_new
    
    #get the final block state as a partition
    partition0 = np.asarray(state.get_bs()[0])

    return g, state, partition0
