from readFile import *
from scipy.io import loadmat

#set global variables here

#set directory containing brain data
loc = "/home/daoutidi/shared/brain_transfer/"

print("Data directory:" + loc)

# import matrix of runs to use for each subject
choose_run = loadmat("/home/daoutidi/shared/runs_to_use.mat")

# create array of all subject file names for iterating on
file_names = readFile("/home/daoutidi/shared/brain_transfer/list_connectomes.txt")

# set global threshold to moderate outliers
threshold = 0.59

print("Current threshold: " + str(threshold))

# set global number of SBM iterations
iterations = 2

print("Number of iterations set to " +str(iterations))
