import numpy as np 
import math 

# BEGIN inputing first set of data 
X_Training1 = np.array( [ [0,1],
                          [0,0],
                          [1,0],
                          [0,0],
                          [1,1] ] )

Y_Training1 = np.array( [ [1],
                          [0],
                          [0],
                          [0],
                          [1] ] )

X_Validation1 = np.array( [ [0,0],
                            [0,1],
                            [1,0],
                            [1,1] ] )

Y_Validation1 = np.array( [ [0],
                            [1],
                            [0],
                            [1] ] )

X_Testing1 = np.array( [ [0,0],
                         [0,1],
                         [1,0],
                         [1,1] ] )

Y_Testing1 = np.array( [ [1],
                         [1],
                         [0],
                         [1] ] )
# END inputing first set of data 

# BEGIN inputing 2nd set of data 
X_Training2 = np.array( [ [0, 1, 0, 0],
                          [0, 0, 0, 1],
                          [1, 0, 0, 0], 
                          [0, 0, 1, 1], 
                          [1, 1, 0, 1],
                          [1, 1, 0, 0], 
                          [1, 0, 0, 1], 
                          [0, 1, 0, 1], 
                          [0, 1, 0, 0] ] )

Y_Training2 = np.array( [ [0], 
                          [1], 
                          [0], 
                          [0], 
                          [1], 
                          [0], 
                          [1], 
                          [1], 
                          [1] ] )


X_Validation2 = np.array( [ [1, 0, 0, 0], 
                            [0, 0, 1, 1], 
                            [1, 1, 0, 1],
                            [1, 1, 0, 0], 
                            [1, 0, 0, 1], 
                            [0, 1, 0, 0] ] )

Y_Validation2 = np.array( [ [0], 
                            [0], 
                            [1], 
                            [0], 
                            [1], 
                            [1] ] )


X_Testing2 = np.array( [ [0, 1, 0, 0], 
                         [0, 0, 0, 1], 
                         [1, 0, 0, 0], 
                         [0, 0, 1, 1], 
                         [1, 1, 0, 1],
                         [1, 1, 0, 0], 
                         [1, 0, 0, 1], 
                         [0, 1, 0, 1], 
                         [0, 1, 0, 0] ] )

Y_Testing2 = np.array( [ [1], 
                         [1], 
                         [0], 
                         [0], 
                         [1], 
                         [0], 
                         [1], 
                         [1], 
                         [1] ] )
# END inputing 2nd set of data 



# BEGIN Data for generating the decision tree (last part of the project)
X_real = np.array( [ [4.8, 3.4, 1.9, 0.2], 
                     [5.0, 3.0, 1.6, 1.2], 
                     [5.0, 3.4, 1.6, 0.2],
                     [5.2, 3.5, 1.5, 0.2], 
                     [5.2, 3.4, 1.4, 0.2], 
                     [4.7, 3.2, 1.6, 0.2],
                     [4.8, 3.1, 1.6, 0.2], 
                     [5.4, 3.4, 1.5, 0.4], 
                     [7.0, 3.2, 4.7, 1.4],
                     [6.4, 3.2, 4.7, 1.5], 
                     [6.9, 3.1, 4.9, 1.5], 
                     [5.5, 2.3, 4.0, 1.3],
                     [6.5, 2.8, 4.6, 1.5], 
                     [5.7, 2.8, 4.5, 1.3], 
                     [6.3, 3.3, 4.7, 1.6],
                     [4.9, 2.4, 3.3, 1.0] ] )

Y_real = np.array( [ [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1], 
                     [1],
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0], 
                     [0] ] )
# END Data for generating the decision tree (last part of the project)

def DT_train_binary(X,Y,max_depth):

def DT_test_binary(X,Y,DT):

def DT_train_binary_best(X_train, Y_train, X_val, Y_val):

def DT_train_real(X,Y,max_depth):

def DT_test_real(X,Y,DT):

def DT_train_real_best(X_train,Y_train,X_val,Y_val):

def main():

if __name__ == "__main__":
    main()

