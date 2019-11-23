import numpy as np

def compute_Z(X,centering=True,scaling=False):
    return X - X.mean(axis=0) if centering else X/X.std(axis=0)
def compute_covariance_matrix(Z):
    return np.dot(Z.transpose(), Z)
def find_pcs(COV):
    L, PCS = np.linalg.eig(COV)
    sort = np.argsort(PCS)
    return np.flip(L[sort], axis=0), (np.flip(PCS[sort], axis=0)).transpose()
def project_data(Z,PCS,L,k,var):
    totaleigens = 0
    cumalative = 0
    if k==0:
        for index in range(len(L)):
            totaleigens = totaleigens + L[index]
        while cumalative < var:
            cumalative = 0
            k=K+1
            for j in range(0, k):
                cumalative= cumalative + L[j]
            cumalative = cumalative/totaleigens
        return np.dot(Z PCS[:, :k])
            
    else:
        return np.dot(Z PCS[:, :k])




