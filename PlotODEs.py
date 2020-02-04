from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


def dxdt(z, t=0):
    x1 = z[0]
    x2 = z[1]
    dx1dt = -3 * x1 + math.sqrt(2) * x2
    dx2dt = math.sqrt(2) * x1 - 2 * x2
    return [dx1dt, dx2dt]


def plot_trajectories(figure):
    t = np.linspace(0, 12, 100)
    for i in np.linspace(0, 5, 5):
        for j in np.linspace(0, 5, 5):
            for k in [-1, 1]:
                for l in [-1, 1]:
                    y0 = [k * i, l * j]
                    y = odeint(dxdt, y0, t)
                    x1 = y[:, 0]
                    x2 = y[:, 1]
                    figure.plot(x1, x2)


def plot_direction_field(figure):
    y_max = figure.get_ylim()[1]
    x_max = figure.get_xlim()[1]
    points_num = 20
    x1 = np.linspace(-1 * x_max, x_max, points_num)
    x2 = np.linspace(-1 * y_max, y_max, points_num)
    X1, X2 = np.meshgrid(x1, x2)
    DX1, DX2 = dxdt([X1, X2])
    M = (np.hypot(DX1, DX2))
    M[M == 0] = 1.
    DX1 /= M
    DX2 /= M
    figure.quiver(X1, X2, DX1, DX2, M, pivot='mid', cmap=plt.cm.plasma)
    figure.set_xlim(-1 * x_max, x_max)
    figure.set_ylim(-1 * y_max, y_max)


def setup_plot(figure):
    figure.set_title('Trajectories and direction fields')
    figure.grid()
    figure.set_xlabel('x1')
    figure.set_ylabel('x2')


if __name__ == "__main__":
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    setup_plot(ax1)
    plot_trajectories(ax1)
    plot_direction_field(ax1)
    plt.show()
