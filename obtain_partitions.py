from scipy.io import loadmat
import numpy as np
import graph_tool as gt
from graph_tool import inference
from readFile import *
from to_adjacency import *
from SBMs import *
import config

#set global variables from config
choose_run = config.choose_run
threshold = config.threshold
file_names = config.file_names
iterations = config.iterations

def obtain_nested_partition(i):
    #choose run with lowest percent censored frames and adjust index
    PC = int(choose_run['best_runs'][i]) - 1
    
    # load the data for that run
    print(file_names[i])
    adj = loadmat("/home/daoutidi/shared/brain_transfer/" + file_names[i])
    
    # select the correct connectivity matrix for best run
    rmat = np.asarray(adj['RS_connectivity_raw'][0][PC]['xcorr'][0][0]['rmat'])
    run = np.asarray(rmat[0][0])

    # obtain nSBM partition
    partition = regular_SBM(run, threshold, iterations)
    return partition


def obtain_nested_partition(i):
    #choose run with lowest percent censored frames and adjust index
    PC = int(choose_run['best_runs'][i]) - 1
    
    # load the data for that run
    print(file_names[i])
    adj = loadmat("/home/daoutidi/shared/brain_transfer/" + file_names[i])
    
    # select the correct connectivity matrix for best run
    rmat = np.asarray(adj['RS_connectivity_raw'][0][PC]['xcorr'][0][0]['rmat'])
    run = np.asarray(rmat[0][0])

    # obtain nSBM partition
    partition = nested_SBM(run, threshold, iterations)
    return partition

