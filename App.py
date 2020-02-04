import tkinter

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

root = tkinter.Tk()
root.wm_title("Embedding in Tk")

fig = Figure()
ax1 = fig.add_subplot(111)


def dxdt(z, t=0):
    x1 = z[0]
    x2 = z[1]
    dx1dt = -3 * x1 + math.sqrt(2) * x2
    dx2dt = math.sqrt(2) * x1 - 2 * x2
    return [dx1dt, dx2dt]


t = np.linspace(0, 12, 100)
for i in np.linspace(0, 5, 5):
    for j in np.linspace(0, 5, 5):
        for k in [-1, 1]:
            for l in [-1, 1]:
                y0 = [k * i, l * j]
                y = odeint(dxdt, y0, t)
                x1 = y[:, 0]
                x2 = y[:, 1]
                ax1.plot(x1, x2)
y_max = ax1.get_ylim()[1]
x_max = ax1.get_xlim()[1]
points_num = 20
x1 = np.linspace(-1 * x_max, x_max, points_num)
x2 = np.linspace(-1 * y_max, y_max, points_num)
X1, X2 = np.meshgrid(x1, x2)
DX1, DX2 = dxdt([X1, X2])
M = (np.hypot(DX1, DX2))
M[M == 0] = 1.
DX1 /= M
DX2 /= M
ax1.set_title('Trajectories and direction fields')
ax1.quiver(X1, X2, DX1, DX2, M, pivot='mid', cmap=plt.cm.plasma)
ax1.set_xlabel('x1')
ax1.set_ylabel('x2')
ax1.grid()
ax1.set_xlim(-1 * x_max, x_max)
ax1.set_ylim(-1 * y_max, y_max)

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def _quit():
    root.quit()
    root.destroy()


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()