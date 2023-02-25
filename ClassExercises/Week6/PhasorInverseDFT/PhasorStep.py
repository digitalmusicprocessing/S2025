import numpy as np
import matplotlib.pyplot as plt

def sample_phasor(k, N, n):
    t = 2*np.pi*k*np.arange(n+1)/N
    c = np.cos(t)
    s = np.sin(t)
    plt.scatter(c, s)
    tt = np.linspace(n-1, n, 200)
    c = np.cos(2*np.pi*k*tt/N)
    s = np.sin(2*np.pi*k*tt/N)
    plt.plot(c, s)
    plt.scatter([c[-1]], [s[-1]], 100, c='C1')
    plt.xlim([-1.5, 1.5])
    plt.ylim([-1.5, 1.5])
    plt.axis("off")

def make_both(k, N):
    plt.figure(figsize=(16, 8))
    for n in range(1, N):
        plt.clf()
        plt.subplot(121)
        sample_phasor(k, N, n)
        plt.title("N = {}, k = {}".format(N, k))
        plt.subplot(122)
        sample_phasor(N-k, N, n)
        plt.title("N = {}, k = {}".format(N, N-k))
        plt.savefig("{}.png".format(n), bbox_inches='tight')

def make_one(k, N):
    plt.figure(figsize=(8, 8))
    for n in range(1, N):
        plt.clf()
        sample_phasor(k, N, n)
        plt.title("k = {}, n = {}".format(k, n))
        plt.savefig("{}.png".format(n), bbox_inches='tight')

make_both(6, 50)
