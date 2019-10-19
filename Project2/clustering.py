import numpy as np
import math
import matplotlib.pyplot as plt
import random

def K_Means(X, K):

    # Randomly initialize center
    randCenterIndexes = random.sample(range(len(X)), K)
    randCenters = []
    for k in randCenterIndexes:
        randCenters.append(X[k])

    output = FindClusters(X, randCenters)

    return output

def FindClusters(X, centers):
    oldCenters = []
    error = 100


    while error != 0:
        clusters = [[] for i in range(len(centers))]
        for i in range(len(X)):
            temp = 5444654
            for centerIndex in range(len(centers)):
                dist = calcDistance(X[i], centers[centerIndex])

                if (dist <= temp):
                    temp = dist
                    value = X[i]
                    found = centerIndex

            # Store value in corresponding cluster (i.e found)
            clusters[found].append(value)

        # Test if centers are the same, otherwise calculate new centers
        # print("C:", centers)
        # print("O:", oldCenters)
        try:
            if (np.allclose([centers], [oldCenters])):
                # print("Clusters:", clusters)
                # print("Centers:", centers)
                error = 0
        except:
            pass
        oldCenters = centers.copy()

        # Jank but to dynamically make the dimensions, e.g: x -- x,y -- x,y,z etc.
        # And to store the new centers again
        dimensions = [[] for i in range(clusters[0][0].shape[0])]
        centers = [[] for i in range(len(centers))]

        # Iterate over the cluster and store the values in their respective array
        # depending on the dimensions noted above
        for i in range(len(centers)):
            for j in clusters[i]:
                for val in range(len(j)):
                    dimensions[val].append(j[val])

            # Iterate over the dimension list and calculate the mean for that cluster
            # To get the new cluster center
            for numDim in range(len(dimensions)):
                value = np.mean(dimensions[numDim])
                centers[i].append(value)

    return centers


def calcDistance(point, centerPoint):
    distance = 0
    for i in range(point.shape[0]):
        value = (centerPoint[i] - point[i])**2
        distance += value

    distance = math.sqrt(distance)

    return distance



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