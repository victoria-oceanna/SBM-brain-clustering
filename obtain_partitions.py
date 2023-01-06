from scipy.io import loadmat
import numpy as np
import graph_tool as gt
from graph_tool import inference
from pytictoc import TicToc
from joblib import Parallel, delayed
from readFile import *
from SBMs import *
import config

#set global variables from config
choose_run = config.choose_run
iterations = config.iterations
directory = config.loc
runs = config.runs
subject_list = config.subject_list

def obtain_regular_partition(i, iterations):
    
    adj = loadmat(subject_list[i])
    PC = runs[i]
    adj = adj['network_adjacency'][0][PC][0][0]['adjacency'][0]['adjacency'][0]
    partition = regular_SBM(adj, iterations)
    
    return partition


def obtain_nested_partition(i, iterations):
    
    adj = loadmat(subject_list[i])
    PC = runs[i]
    adj = adj['network_adjacency'][0][PC][0][0]['adjacency'][0]['adjacency'][0]
    partition = nested_SBM(adj, iterations)
    
    return partition


