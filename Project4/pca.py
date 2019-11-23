import numpy as np

def compute_Z(X,centering=True,scaling=False):
    return X - X.mean(axis=0) if centering else X/X.std(axis=0)
def compute_covariance_matrix(Z):
    return np.dot(Z.transpose(), Z)
def find_pcs(COV):
    L, PCS = np.linalg.eig(COV)
    return np.flip(L[np.argsort(L)], axis=0), (np.flip(PCS[np.argsort(L)], axis=0)).transpose()
def project_data(Z,PCS,L,k,var):
    if k > Z[0].size:
        return np.dot(Z, PCS)
    if var > 0:
        k = np.max(np.argwhere(var >= (L.cumsum()/L.sum()))) + 1
    return np.dot(Z, PCS[:, :k])
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