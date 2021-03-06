import numpy as np
from scipy.integrate import odeint
from UI.Constants import *


class ODEPlotter:
    def __init__(self, figure):
        self.figure = figure
        self.ax = self.figure.add_subplot(111)
        # self.ax1 = self.figure.add_subplot(122)
        self.set_limit()
        self.setup_plot()
        self.system = None

    def set_system(self, coefficients):
        self.system = np.array([[coefficients[0], coefficients[1]],
                                [coefficients[2], coefficients[3]]])

    def dxdt(self, z, t=0):
        """
        dXdt = constant coefficients system * X
        """
        return np.tensordot(self.system, z, 1)

    def plot_trajectories(self, x_corr, y_corr):
        t = np.linspace(0, 12, 10000)
        y0 = [x_corr, y_corr]
        y = odeint(self.dxdt, y0, t)
        x1 = y[:, 0]
        x2 = y[:, 1]
        line = self.ax.plot(x1, x2)[0]
        self.add_arrow(line)
        self.set_limit()

    def plot_direction_field(self):
        x1 = np.linspace(-1 * X_MAX, X_MAX, DIRECTION_FIELD_NUM)
        x2 = np.linspace(-1 * Y_MAX, Y_MAX, DIRECTION_FIELD_NUM)
        X1, X2 = np.meshgrid(x1, x2)
        DX1, DX2 = self.dxdt([X1, X2])
        norms = (np.hypot(DX1, DX2))
        norms[norms == 0] = 1.
        DX1 /= norms
        DX2 /= norms
        self.ax.quiver(X1, X2, DX1, DX2, norms, pivot='mid')
        self.set_limit()

    def add_arrow(self, line, position=None, size=25, color=None):
        if color is None:
            color = line.get_color()
        unfiltered = np.vstack((line.get_xdata(), line.get_ydata())).T
        filtered = unfiltered[(unfiltered[:, 0] >= -1 * X_MAX) & (unfiltered[:, 0] <= X_MAX) &
                              (unfiltered[:, 1] >= -1 * Y_MAX) & (unfiltered[:, 1] <= Y_MAX)]
        x_data = filtered[:, 0]
        y_data = filtered[:, 1]
        if position is None:
            position = (min(x_data.max(), X_MAX) + max(x_data.min(), -1 * X_MAX)) / 2
        # find closest index
        start_ind = np.argmin(np.absolute(x_data - position))
        end_ind = start_ind + 1
        line.axes.annotate('', xytext=(x_data[start_ind], y_data[start_ind]), xy=(x_data[end_ind], y_data[end_ind]),
                           arrowprops=dict(arrowstyle="->", color=color, lw=1.5), size=size)

    def setup_plot(self):
        self.ax.set_title('Trajectories and direction fields')
        self.ax.set_xlabel('x1')
        self.ax.set_ylabel('x2')

    def clear_figure(self):
        self.ax.clear()
        self.setup_plot()

    def set_limit(self):
        self.ax.set_xlim(-1 * X_MAX, X_MAX)
        self.ax.set_ylim(-1 * Y_MAX, Y_MAX)
