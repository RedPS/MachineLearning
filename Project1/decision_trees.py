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

Y_Training2 = np.array( [   [0], 
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


X_Testing2 = np.array( [    [0, 1, 0, 0], 
							[0, 0, 0, 1], 
							[1, 0, 0, 0], 
							[0, 0, 1, 1], 
							[1, 1, 0, 1],
							[1, 1, 0, 0], 
							[1, 0, 0, 1], 
							[0, 1, 0, 1], 
							[0, 1, 0, 0] ] )

Y_Testing2 = np.array( [    [1], 
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
X_real = np.array( [    [4.8, 3.4, 1.9, 0.2], 
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

Y_real = np.array( [    [1], 
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

def mylog2(side):
	if not side:
		return 0
	return -side * math.log2(side)

def Set_Prob(Set, Label):
	return (np.count_nonzero(Set == Label)) / len(Set) if (len(Set)) else 0

def entropy(Set):
	return mylog2(Set_Prob(Set, 0)) + mylog2(Set_Prob(Set, 1))

def informationGain(Xset, label, i):
	return entropy(label) - (Set_Prob(Xset[:,i], 0) * entropy(label[Xset[:,i] == 0]) + Set_Prob(Xset[:,i], 1) * entropy(label[Xset[:,i] == 1]))

def SplitData(XSet, YSet):
	Position = 0
	BetterInfoGain = 0
	for i in range (np.size(XSet,1)):
		if informationGain(XSet, YSet, i) > BetterInfoGain:
			Position = i
			BetterInfoGain = informationGain(XSet, YSet, i)
	return Position 

def DT_train_binary(X,Y,max_depth):
	if (max_depth == 0):
		if ( X.size == 0):
			return 0 if Set_Prob(Y, 0) > Set_Prob(Y, 1) else 1
	else:
		Left = X[X[:,SplitData(X, Y)] == 0]
		LabelonLeft = Y[X[:,SplitData(X, Y)] == 0]
		Right = X[X[:,SplitData(X, Y)] == 1]
		LabelonRight = Y[X[:,SplitData(X, Y)] == 1]
		Left = np.delete(Left, SplitData(X, Y), 1)
		Right = np.delete(Right, SplitData(X, Y), 1)
		return [SplitData(X, Y),ChildTree(LabelonLeft, 0, Left, max_depth-1), ChildTree(LabelonRight, 0, Right, max_depth-1)]

def ChildTree(Set, label, Side, max_depth):
	if (entropy(Set) == label):
		Child = Set[0]
	else:
		Child = DT_train_binary(Side, Set, max_depth - 1)
	return Child


