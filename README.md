# SBM-brain-clustering

Dependencies: 
              
              numpy
              
              pyintergraph
              
              graph_tool
             
              networkx
              
              scipy.io
              
              joblib
              
              pytictoc (only used for timing; can be removed)

The code within this repository is intended to be used with pre-thresholded connectivity matrices. As written, the matrices are binarized and an unweighted, degree-corrected verison of both SBM and nSBM can be applied. Editing these codes for the weighted case is simple and instructions are provided within comments.

For basic use, changes only need to be made to the config file.

These codes were used to generate results for a pending publication: Brooks, S., Jones, V.O., Wang, H., Gao, J. Daoutidis, P. Stamoulis, C. “Community Detection in the Human Connectome: Method Types, Differences and their Impact on Inference.” Human Brain Mapping.
