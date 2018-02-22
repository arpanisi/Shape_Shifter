import numpy as np
import matplotlib.pyplot as plt
ax = plt.subplot(111, projection='polar')
N_points = 201
for N_times in range(2, 101):
    r = np.ones(N_points)
    theta = np.linspace(-np.pi, np.pi, N_points)
    for i in range(N_points):
        theta_i = [theta[i], N_times*theta[i]]
        r_i = [1, 1]
        ax.plot(theta_i, r_i, 'b', linewidth=0.5)
    ax.set_rticks([])
    ax.set_thetagrids([])
    ax.set_rmax(1)
    title = 'N_times = ' + str(N_times)
    plt.title(title)
    plt.pause(0.001)
    ax.cla()
