# 8: for k = 1 to K do
# 9: Xk ← { xn : zn = k } // points assigned to cluster k
# 10: µk ← mean(Xk
# ) // re-estimate center of cluster k
# 11: end for
# 12: until µs stop changing
# 13: return z // return cluster assignments

import numpy as np
import math
import matplotlib.pyplot as plt
import random
import time

# Test
# X = np.array([[1, 0], [7, 4], [9, 6], [2, 1], [4, 8], [0, 3], [13, 5], [6, 8], [7, 3], [3, 6], [2, 1], [8, 3], [10, 2], [3, 5], [5, 1], [1, 9], [10, 3], [4, 1], [6, 6], [2, 2]])
X = np.array([[0], [1], [2], [7], [8], [9], [12], [14], [15]])

def K_Means(X, K):

    PrePlotClusters(X, "before")
    
    # Randomly initialize center
    randCenterIndexes = random.sample(range(len(X)), K)
    randCenters = []
    for k in randCenterIndexes:
        randCenters.append(X[k])
    
    FindClusters(X, randCenters)

def FindClusters(X, centers):
    oldCenters = []

    while oldCenters != centers:
        print("going")
        clusters = [[] for i in range(len(centers))]
        for i in range(len(X)):
            temp = 5444654
            for centerIndex in range(len(centers)):
                dist = calcDistance(X[i], centers[centerIndex])

                if (dist <= temp):
                    temp = dist
                    value = X[i]
                    found = centerIndex
            
            clusters[found].append(value)

        # Update cluster center by the mean
        oldCenters = centers.copy()
        centers.clear()
        
        for i in range(len(oldCenters)):
            number = np.mean(clusters[i])
            centers.append(np.array([number]))

    for i in centers:
        for j in i:
            print("Center:", j)
        
    PlotClusters(clusters, "after")


def calcDistance(point, centerPoint):

    distance = 0
    for i in range(point.shape[0]):
        value = (centerPoint[i] - point[i])**2
        distance += value

    distance = math.sqrt(distance)

    return distance

def PrePlotClusters(X, file):
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

def PlotClusters(clusters, file):

    x = []
    colorString = 'red'

    for i in range(len(clusters)):
        for j in clusters[i]:
            for items in j:
                print(items)
                x.append(items)
            
        plt.scatter(x, np.zeros_like(x), c=colorString)
        x.clear()
        colorString = 'blue'
        print("----------")

    
    plt.savefig(file + ".jpg")


K_Means(X, 2)




# I was just thinking about K_Means_better and tried to write down what was in my mind, the below is not code it is just some initial thoughts 
"""
def K_Means_better(X, K):
  centers = []
  numberofcenters= []
  SameCenters= []
  alreadyseen = 0
  tmp = 0

    for  i in range(0, 9999999):
        centers.append(listofKmeans)
        if list(centers[i]) in list(samecenters):
            alreadyseen = 0
            while center[i] != samecenter
                alreadyseen = alreadyseen + 1
            numberofcenters[alreadyseen] = numberofcenters[alreadyseen] + 1
        else:
            samecenters.append(centers[i])
            numberofcenters.append(1)
    for i in range(0, len(numberofcenters))
        if numberofcenters[tmp] < numberofcenters[i]
            tmp = i
    MostSeen = tmp

    return np.array(SameCenters[MostSeen])
"""