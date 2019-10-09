import numpy as np


def perceptron_train(X,Y):
    # initialize W and B (to 0)
    # strat calculating a
        # if a <=0 UPDATE
        # else don't  
        # set a flag for epoch so you know when to stop 
        # so if W hasn't changed for that epoch we have converged and we're done
def perceptron_test(X_test, Y_test, w, b):
    # compare prediction with the label 
    """
    for i in X
        calculate a 
        if a*Y > 0
        correct++
    return the average correct
    """