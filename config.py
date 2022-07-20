from readFile import *
from scipy.io import loadmat

#set global variables here

# import matrix of runs to use for each subject
choose_run = loadmat("/home/daoutidi/shared/runs_to_use.mat")

# create array of all subject file names for iterating on
file_names = readFile("/home/daoutidi/shared/brain_transfer/list_connectomes.txt")

# set global threshold to moderate outliers
threshold = 0.59

# set global number of SBM iterations
iterations = 10
