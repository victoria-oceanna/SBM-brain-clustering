from readFile import *
from os import listdir
from os.path import isfile, join
import math
from scipy.io import loadmat
import pandas as pd

#set global variables here

#SET DIRECTORY CONTAINING BRAIN DATA
loc = "/home/daoutidi/shared/new_adj/"

print("Data directory: " + loc)

#SELECT RUN BASED ON CONNECTIVITY -> "min_med_conn_run" for best run and "sec_med_conn_run" for second best run
choose_run = "min_med_conn_run"

print("Current run: " + choose_run)

#SET GLOBAL NUMBER OF SBM OR NSBM ITERATIONS
iterations = 10

print("Number of iterations set to " +str(iterations))

#GENERATE LIST OF SUBJECTS TO ITERATE OVER

#read csv file containing the indices of best runs corresponding to .mat files of brain data
PC = pd.read_csv('runs_mat.csv', delimiter=',')

#select column of indices based on choose_run
PC_run = PC[choose_run].to_numpy()

#get list of all subjects from dataframe row labels
subs = PC['Row'].to_list()

#create a list of all brain data files within loc directory, sort, and remove superfluous files
file_list = [f for f in listdir(loc) if isfile(join(loc, f))]
file_list = sorted(file_list)
file_list.remove('runs_mat_r2_adj_meet_conn_dens_02-Nov-2022.mat')
print("Number of files in file list: " + str(len(file_list)))

#get lists of viable subjects based on connectivity and the best run indices that correspond to them
mean_conn_first = []
list_of_subjects = []
PC_run_reduced = []
for i in range(len(subs)):
    if math.isnan(PC_run[i]) == False:
        PC = int(PC_run[i] - 1)
        PC_run_reduced.append(PC)
        #alter file names as needed
        list_of_subjects.append(loc + subs[i] + "_network_adjacency_xcorr-baselineYear1Arm1_Schaefer_1000.mat.mat")

runs = PC_run_reduced
subject_list = list_of_subjects

print("Number of subjects: " + str(len(subject_list)))
