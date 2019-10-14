import numpy as np
import math
import matplotlib.pyplot as plt
import random

# Test
# X = np.array([[1, 0], [7, 4], [9, 6], [2, 1], [4, 8], [0, 3], [13, 5], [6, 8], [7, 3], [3, 6], [2, 1], [8, 3], [10, 2], [3, 5], [5, 1], [1, 9], [10, 3], [4, 1], [6, 6], [2, 2]])
X = np.array([[0], [1], [2], [7], [8], [9], [12], [14], [15]])

def K_Means(X, K):

    # Pre plot
    plotClusters(X, "before")

    # Initialize random cluster centers
    centerIndex = random.sample(range(len(X)), K)
    # Use the index to grab the center
    centers = []
    for i in range(len(centerIndex)):
        temp = centerIndex[i]
        centers.append(X[temp])

    # Now I have my centers, need to iterate the points and calculate the distance and place them in the appropriate cluster
    # Item 1 == center 1, Item 2 == center 2...
    clusters = init_clusters(X, centers)

    # for items in clusters:
    #     print(items)

    FindClusters(clusters, K)

def FindClusters():


def InitClusters(X, centers):
    # print(centers)

    cluster = [[] for i in range(len(centers))]

    for i in range(len(X)):
        dist = 1545651        
        for j in range(len(centers)):
            temp = math.sqrt((X[i] - centers[j])**2)

            if (temp <= dist):
                dist = temp
                val = X[i]
                found = j

        cluster[found].append(val)

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