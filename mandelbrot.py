import numpy as np
import matplotlib.pyplot as plt

tol = 8
degree = 2

x0 = -0.21503361460851339
y0 = 0.67999116792639069

ax = plt.subplot(111)
ZM = np.arange(1, 200, 0.35)

nx = 384
ny = 216
n_iter = 80

for zm in ZM:
    zmf = np.exp(-zm/20.)

    x1 = x0 - 2 * zmf
    x2 = x0 + 2 * zmf
    y1 = y0 - 1.13 * zmf
    y2 = y0 + 1.13 * zmf


    x, y = np.meshgrid(np.linspace(x1, x2, nx), np.linspace(y1, y2, ny))
    c = x + 1j*y
    z = np.zeros(c.shape)
    I = np.zeros(c.shape)

    for k in range(n_iter):
        z = z ** degree + c
        ind = (np.abs(z) > tol) * (I == 0)
        I[ind] = 255 - k

    ax.imshow(I, extent=(x1, x2, y1, y2)) #, shape=(3840, 2160), interpolation='bilinear')
    plt.pause(0.001)
    ax.cla()
