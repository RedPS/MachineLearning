import numpy as np
"""
this will take the data matrix X and boolean variables centering and scaling and return the one that is active
basically what we are doing is subtracting the mean or the standard deviation (according to what the user chooses)
"""
def compute_Z(X,centering=True,scaling=False):
    # if centering is True subtract the mean from each feature in X
    # else (if scaling is true) subtract the standard deviation from each feature in X
    return X - X.mean(axis=0) if centering else X/X.std(axis=0)
"""
The above function will take the standardized data matrix Z and return the covariance matrix ZTZ=COV (a numpy array).
"""
def compute_covariance_matrix(Z):
    # we are just returning the covariance matrix Z.T dot Z, literally the easiest part of this project
    return np.dot(Z.transpose(), Z)
"""
The below function will take the covariance matrix COV and return the ordered (largest to smallest) principal components PCS 
PCS is a numpy array where each column is an eigenvector and corresponding eigenvalues L is also a numpy array
We are using np.linalg.eig for this.
"""
def find_pcs(COV):
    L, PCS = np.linalg.eig(COV)
    return np.flip(L[np.argsort(L)], axis=0), (np.flip(PCS[np.argsort(L)], axis=0)).transpose()
"""
The above function will take the standardized data matrix Z, the principal components PCS, and corresponding eigenvalues L, 
as well as a k integer value and a var ﬂoating point value. k is the number of principal components you wish to maintain 
when projecting the data into the new space. 0 ≤ k ≤ D. If k= 0, then we use the cumulative variance to determine the projection dimension. 
var is the desired cumulative variance explained by the projection. 0 ≤v≤ 1. 
If v= 0, then k is used instead. We are Assuming they are never both 0 or both > 0. This function will return Z_star, the projected data.
"""
def project_data(Z,PCS,L,k,var):
    if var > 0:
        k = np.max(np.argwhere(var >= (L.cumsum()/L.sum()))) + 1
        PCS = PCS[:, :k]
    return np.dot(Z, PCS)
"""
K = 0 was tricky, hopefully there was a function in numpy for calculating the cumalative since the assignment is not about 
implemeting a cumalative function I just used the numpy one but here is the pseduo code 
  totaleigens = 0
  cumalative = 0
    if k==0
        temp = k
        for index in range(len(L)):
            totaleigens = totaleigens + L[index]
        while cumalative < var:
            cumalative = 0
            temp=temp+1
            for j in range(0, k):
                cumalative= cumalative + L[j]
            cumalative = cumalative/totaleigens
        return np.dot(Z,PCS[:, :temp])
"""