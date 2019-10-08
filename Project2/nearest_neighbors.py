import numpy as np
import math # just using the pow for calculating the norm

X = np.array ([[1, 1], [2, 1], [0, 10], [10, 10], [5, 5], [3, 10], [9, 4], [6, 2], [2, 2], [8, 7]])
Y = np.array( [[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1]])

XT = np.array([[1, 5], [2, 6], [2, 7], [3, 7], [3, 8], [4, 8], [5, 1], [5, 9], [6, 2], [7, 2], [7, 3], [8, 3], [8, 4], [9, 5]])
YT = np.array([[-1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [1]])

def KNN_test(X_train, Y_train, X_test, Y_test,K):
    NumberOfCorrect = 0
    radius = []
    for i, j in enumerate(X_test):
        for n, m in enumerate(X_train):
            radius.append(((math.pow((m[0] - j[0]), 2) + math.pow((m[1] - j[1]), 2)), Y_train[n][0]))
        List_sorted = sorted(radius, key=lambda member: member[0], reverse=False)[:K] # https://stackoverflow.com/questions/13669252/what-is-key-lambda/13669294
        if sum([member[1] for member in List_sorted]) == Y_test[i][0]:
            NumberOfCorrect = NumberOfCorrect+1
    return NumberOfCorrect / len(X_test)

# not going to lie I just forgot about the choose_K I'll finish that later
# def choose_K(X_train,Y_train,X_val,Y_val):

def main():
    print(KNN_test(X,Y,XT, YT, 1))

if __name__ == "__main__":
    main()