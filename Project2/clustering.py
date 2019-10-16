import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time

# Test
# X = np.array([[1, 0], [7, 4], [9, 6], [2, 1], [4, 8], [0, 3], [13, 5], [6, 8], [7, 3], [3, 6], [2, 1], [8, 3], [10, 2], [3, 5], [5, 1], [1, 9], [10, 3], [4, 1], [6, 6], [2, 2]])
X = np.array([[0], [1], [2], [7], [8], [9], [12], [14], [15]])

def K_Means(X, K):

    # Pre plot
    PlotClusters(X, "before")

    clusters = InitClusters(X, K)
    
    UpdateClusters(clusters)

def UpdateClusters(clusters):

    # cluster = np.asarray(clusters)

    for clust in clusters[0]:
        for items in clust:
            print(items)
            
    # Choose the new center
    print("Size 1:", len(clusters[0]))
    print("Size 2:", len(clusters[1]))

    

    # Base case when clusters stop updating
    # if (clusters == updatedClusters):
    #     return clusters
    # else:
    #     UpdateClusters(updatedClusters)

def EuclideanDistance(center, point):
    distance = 0
    for i in range(point.shape[0]):
        val = (center[i] - point[i])**2
        distance += val
    
    distance = math.sqrt(distance)
    
    return distance


def InitClusters(X, K):
    # Initialize random cluster centers
    centerIndex = random.sample(range(len(X)), K)
    # Use the index to grab the center
    centers = []
    for items in centerIndex:
        centers.append(X[items])

    cluster = [[] for i in range(len(centers))]
    # cluster = np.asarray(cluster)
    
    for points in X:
        dist = 1546548
        for index, centerCoord in enumerate(centers):
            temp = EuclideanDistance(points, centerCoord)

            if (temp <= dist):
                dist = temp
                value = points
                found = index

        cluster[found].append(value)

    return cluster

def PlotClusters(X, file):
    # Plot the points and see for a before
    x = []
    y = []

    # make this work for a x,y plot
    for index in range(len(X)):
        try:
            x.append(X[index][0])
            y.append(X[index][1])
        except:
            pass
    
    try:
        plt.scatter(x, y)
    except:
        plt.scatter(x, np.zeros_like(x))
    
    plt.savefig(file + ".jpg")     


K_Means(X, 2)