import numpy as np
import matplotlib.pyplot as plt

def polyFit(X, xs, K, doPlot = False):
    """
    Given a Nx2 array X of 2D coordinates, fit a k^th order polynomial
    and evaluate it at the coordinates in xs.
    This function assumes that all of the points have a unique X position
    """
    x = X[:, 0]
    y = X[:, 1]
    N = X.shape[0]
    A = np.zeros((N, K))
    for i in range(K):
        A[:, i] = x**i
    b = np.linalg.lstsq(A, y)[0]

    M = xs.size
    Y = np.zeros((M, 2))
    Y[:, 0] = xs
    for i in range(K):
        Y[:, 1] += b[i]*(xs**i)
    if doPlot:
        plt.plot(Y[:, 0], Y[:, 1], 'b')
        plt.hold(True)
        plt.scatter(X[:, 0], X[:, 1], 20, 'r')
        plt.show()
    return Y
