from graph_tool import inference
import graph_tool as gt
import networkx as nx
import numpy as np
from to_adjacency import *
import config

#set global variables from config
choose_run = config.choose_run
iterations = config.iterations
directory = config.loc
runs = config.runs
subject_list = config.subject_list

# function for obtaining SBM partition
def regular_SBM(adj, iterations):
    #convert connectivity matrix to graph
    g = to_adjacency(adj)
    
    #find an intial state
    state = inference.minimize_blockmodel_dl(g, deg_corr=True)

    #call algorithm for desired number of iterations
    for i in range(0, iterations):
        #save state of recalled algorithm
        state_new = inference.minimize_blockmodel_dl(g, deg_corr=True)
        #retain the state with the lower entropy value - ie. the better fit
        if state_new.entropy() < state.entropy():
            state = state_new

    #create empty list for partition - this step is necessary because the get_array function in graph-tool is broken
    block_belong = []
    #get the block membership of each node
    blocks = state.get_blocks()
    #for each node, idenitfy block membership and append at corresponding index
    for i in range(len(adj)):
        r = blocks[i]
        block_belong.append(r)

    #convert partition list to array
    block_belong = np.asarray(block_belong)
    partition = block_belong

    return partition

# function for obtaining nSBM partition
def nested_SBM(adj, iterations):
    #convert connectivity matrix to graph
    g = to_adjacency(adj)
    
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

    return partition0

# function for obtaining SBM partition
def w_regular_SBM(adj, iterations):
    #convert connectivity matrix to graph
    g = to_adjacency(adj)
    
    #find an intial state
    state = inference.minimize_blockmodel_dl(g, deg_corr=True, state_args=dict(recs=[g.ep.weight],
                                                            rec_types=["real-exponential"]))

    #call algorithm for desired number of iterations
    for i in range(0, iterations):
        #save state of recalled algorithm
        state_new = inference.minimize_blockmodel_dl(g, deg_corr=True, state_args=dict(recs=[g.ep.weight],
                                                            rec_types=["real-exponential"]))
        #retain the state with the lower entropy value - ie. the better fit
        if state_new.entropy() < state.entropy():
            state = state_new

    #create empty list for partition - this step is necessary because the get_array function in graph-tool is broken
    block_belong = []
    #get the block membership of each node
    blocks = state.get_blocks()
    #for each node, idenitfy block membership and append at corresponding index
    for i in range(len(adj)):
        r = blocks[i]
        block_belong.append(r)

    #convert partition list to array
    block_belong = np.asarray(block_belong)
    partition = block_belong

    return partition

# function for obtaining nSBM partition
def w_nested_SBM(adj, iterations):
    #convert connectivity matrix to graph
    g = to_adjacency(adj)
    
    #find an intial state
    state = inference.minimize_nested_blockmodel_dl(g, deg_corr=True, state_args=dict(recs=[g.ep.weight],
                                                            rec_types=["real-exponential"]))
    
    #call algorithm for desired number of iterations
    for i in range(0, iterations):
        #save state of recalled algorithm
        state_new = inference.minimize_nested_blockmodel_dl(g, deg_corr=True, state_args=dict(recs=[g.ep.weight],
                                                            rec_types=["real-exponential"]))
        #retain the state with the lower entropy value - ie. the better fit
        if state_new.entropy() < state.entropy():
            state = state_new
    
    #get the final block state as a partition
    partition0 = np.asarray(state.get_bs()[0])

    return partition0