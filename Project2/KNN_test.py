import nearest_neighbors as NN
import numpy as np

print_stuff = True

if print_stuff:
    print("\n\n\nKNN tests:")
NN_X_train = np.array(
    [[1, 5], [2, 6], [2, 7], [3, 7], [3, 8], [4, 8], [5, 1], [5, 9], [6, 2], [7, 2], [7, 3], [8, 3], [8, 4],
     [9, 5]])
NN_Y_train = np.array([[-1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [1]])

NN_test_X = np.array([[1, 1], [2, 1], [0, 10], [10, 10], [5, 5], [3, 10], [9, 4], [6, 2], [2, 2], [8, 7]])
NN_test_Y = np.array([[1], [-1], [1], [-1], [1], [-1], [1], [-1], [1], [-1]])
self_test = NN.KNN_test(NN_X_train, NN_Y_train, NN_X_train, NN_Y_train, 1)
choose_k_self = NN.choose_K(NN_X_train, NN_Y_train, NN_X_train, NN_Y_train)
if print_stuff:
    print("KNN test on self =", self_test)
    print("KNN choose k on self =", choose_k_self)

choose_test = NN.choose_K(NN_X_train, NN_Y_train, NN_test_X, NN_test_Y)
if print_stuff:
    print("choose_k on test ", choose_test)

i = 0
while i < len(NN_test_X):
    test_test = NN.KNN_test(NN_X_train, NN_Y_train, NN_test_X, NN_test_Y, i + 1)
    if print_stuff:
        print("KNN k=", i + 1, "test on test accuracy =", test_test)
    i += 1

for k in [1, 2, 5]:
    if print_stuff:
        print("TESTING K =", k)
    for i in range(len(NN_test_X)):
        NN_res = NN.KNN_test(NN_X_train, NN_Y_train, np.array([NN_test_X[i]]), np.array([NN_test_Y[i]]), k)
        if print_stuff:
            print("Writeup KNN", k, "Test on", NN_test_X[i], NN_test_Y[i],
                  "Correct" if NN_res == 1.0 else "not correct")
