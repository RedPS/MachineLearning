#!/usr/bin/env python3

import pca
import numpy as np
import os
import matplotlib.pyplot as py

def load_data(input_dir):
    exists = os.path.exists(input_dir)
    if not exists:
        print("Can't find input dir")
        return
    dataimg = []
    finalresult = []
    input = input_dir
    for dir, child, datas in os.walk(input):
        for data in np.sort(datas):
            image = py.imread(input+ data, 'pgm')
            image = image.flatten()
            dataimg.append(image)
    finalresult = np.array(dataimg)
    finalresult = finalresult.astype(np.float)
    finalresult = finalresult.transpose()
    return finalresult


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
        py.imsave('Output/out%d.png'%j,compress[j].reshape(60,48),vmin=0,vmax=255,cmap='gray',format='png')
