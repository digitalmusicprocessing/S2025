import numpy as np
import matplotlib.pyplot as plt
import scipy.misc
import skimage
import skimage.io
from PolynomialFit import *

if __name__ == "__main__":
    plt.figure(figsize=(12, 4))
    N = 200
    doPlot = False
    
    i1 = 30
    j1 = 85
    
    """
    i2 = 162
    j2 = 175
    
    I = skimage.io.imread("CSMCurves.png")
    I1 = I[:, :, 2]
    I2 = I[:, :, 0]
    [X, Y] = np.meshgrid(np.arange(I.shape[1]), np.arange(I.shape[0]))
    
    y1 = X[I1 == 0]
    x1 = Y[I1 == 0]
    X1 = np.zeros((len(x1), 2))
    X1[:, 0] = x1
    X1[:, 1] = y1

    Y1 = polyFit(X1, np.linspace(np.min(x1), np.max(x1), N), 5, doPlot)
    
    x2 = Y[I2 == 0]
    y2 = X[I2 == 0]
    X2 = np.zeros((len(x2), 2))
    X2[:, 0] = x2
    X2[:, 1] = y2
    
    Y2 = polyFit(X2, np.linspace(np.min(x2), np.max(x2), N), 6, doPlot)
    
    Y1 = Y1[:, [1, 0]]
    Y2 = Y2[:, [1, 0]]
    Y1 = Y1 - np.mean(Y1, 0)[None, :]
    Y1[:, 1] *= 2
    Y1[:, 0] *= 3
    Y2 = Y2 - np.mean(Y2, 0)[None, :]
    Y2[:, 0] *= 2
    Y2[:, 1] *= 1.5
    Y2 += [[80, 0]]
    scale = np.max(np.abs(Y1))
    Y1 /= scale
    Y2 /= scale
    """
    t = np.linspace(0, 1, N)
    Y1 = np.zeros((N, 2))
    Y1[:, 0] = np.cos(2*np.pi*t)
    Y1[:, 1] = np.sin(4*np.pi*t)
    Y2 = np.zeros((N, 2))
    Y2[:, 0] = 1.3*np.cos(2*np.pi*(t**2))
    Y2[:, 1] = 1.3*np.sin(4*np.pi*(t**2))+0.1    
    
    
    Y1Sqr = np.sum(Y1**2, 1)
    Y2Sqr = np.sum(Y2**2, 1)
    CSM = Y1Sqr[:, None] + Y2Sqr[None, :] - 2*Y1.dot(Y2.T)
    CSM[CSM < 0] = 0
    CSM = np.sqrt(CSM)
    
    c1 = 'Reds'
    c2 = 'Blues'
    
    plt.subplot(121)
    plt.title('Curve Examples')
    plt.scatter(Y1[:, 0], Y1[:, 1], 30, np.arange(N), cmap=c1, edgecolor = 'none')
    plt.scatter(Y1[i1, 0], Y1[i1, 1], 100, 'r')
    plt.scatter(Y2[:, 0], Y2[:, 1], 30, np.arange(N), cmap=c2, edgecolor = 'none')
    plt.scatter(Y2[j1, 0], Y2[j1, 1], 100, 'r')
    plt.plot([Y1[i1, 0], Y2[j1, 0]], [Y1[i1, 1], Y2[j1, 1]])
    ax = plt.gca()
    ax.set_facecolor((0.7, 0.7, 0.7))
    plt.axis('equal')
    
    plt.subplot(122)
    plt.imshow(CSM, interpolation = 'none', cmap='magma_r')
    plt.colorbar()
    plt.scatter(-2*np.ones(N), np.arange(N), 20, np.arange(N), cmap=c1, edgecolor = 'none')
    plt.scatter(np.arange(N), -2*np.ones(N), 20, np.arange(N), cmap=c2, edgecolor = 'none')
    plt.scatter(j1, i1, 100, 'r', )
    plt.title("i = {}, j = {}".format(i1, j1))
    #plt.scatter(j2, i2, 100, 'c')
    
    plt.xlabel('Time Index on Right Curve')
    plt.ylabel('Time Index on Left Curve')
    #plt.title('Euclidean Cross-Similarity Matrix')
    
    plt.savefig("CSMExample.svg", bbox_inches='tight')
