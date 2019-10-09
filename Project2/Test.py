from nearest_neighbors import *
#from perceptron import *
# Data for KNN
X = np.array ([[1, 1], [2, 1], [0, 10], [10, 10], [5, 5], [3, 10], [9, 4], [6, 2], [2, 2], [8, 7]])
Y = np.array( [[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1]])
XT = np.array([[1, 5], [2, 6], [2, 7], [3, 7], [3, 8], [4, 8], [5, 1], [5, 9], [6, 2], [7, 2], [7, 3], [8, 3], [8, 4], [9, 5]])
YT = np.array([[-1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [1]])

# Data for Perceptron 
Perceptron_X1 = np.array([[0, 1], [1, 0], [5, 4], [1, 1], [3, 3], [2, 4], [1, 6]])
Perceptron_Y1 = np.array([[1], [1], [0], [1], [0], [0], [0]])
Perceptron_X2 = np.array([[-2, 1], [1, 1], [1.5, -0.5], [-2, -1], [-1, -1.5], [2, -2]])
Perceptron_Y2 = np.array([[1], [1], [1], [-1], [-1], [-1]])


def main():
    print("KNN_Test:", KNN_test(X,Y,XT, YT, 1))
    print("Chosen_K:", choose_K(X,Y,XT,YT))
#    print("Perceptron_Train:",perceptron_train(X, Y)
#    print("Perceptron_Test",perceptron_test(X, Y, W[0], W[1]))
if __name__ == "__main__":
    main()