#!/usr/bin/env python3

import pca
import numpy as np
import os
import matplotlib.pyplot as py

def load_data(input_dir):
    data = []
    exists = os.path.exists(input_dir)
    if not exists:
        print("Can't find input dir")
        return
    for pic in os.listdir(input_dir):
        if input_dir[-1:] != '/':
            imgOG = py.imread(input_dir+'/'+pic)
        else:
            imgOG = py.imread(input_dir+'/'+pic)
        imgFlat = imgOG.flatten()
        #unsure if want row major (above) or column major (below)
        #imgFlat = imgOG.flatten(order='F')
        data.append(imgFlat)
    return np.array(data)

def compress_images(DATA,k):
    exists = os.path.exists("Output")
    if not exists:
        os.mkdir('Output')
    #for each pic in the data arr
    Z = pca.compute_Z(DATA)
    COV = pca.compute_covariance_matrix(Z)
    L, PCS = pca.find_pcs(COV)
    Zstar = pca.project_data(Z,PCS,L,k,0)
    PCS = PCS[:, :k]
    PCS = PCS.T
    compress = np.dot(Zstar, PCS)
    compress = compress.T
    for j in range(0, len(compress)):
            # save the images you have to reshape them ( something like compress[j].reshape(60,48) before or as you are saving the images )
        # py.imsave('Output/out%i.png'%i,Zstar,vmin=0,vmax=255,cmap='gray',format='png')
