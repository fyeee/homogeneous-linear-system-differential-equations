import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from ODEPlotter import ODEPlotter
import random


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.control_frame = tk.Frame(self.root)
        self.plot_frame = tk.Frame(self.root)
        self.root.wm_title("Ordinary Differential Equations")
        self.control_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.fig = Figure()
        self.plotter = ODEPlotter(self.fig)
        self.sliders = []
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.callbacks.connect('button_press_event', self.on_click_figure)
        self.set_up_control_frame()

    def set_up_control_frame(self):
        for i, char in enumerate(['a', 'b', 'c', 'd']):
            self.sliders.append(tk.Scale(master=self.control_frame, from_=-10, to=10, tickinterval=4, length=200,
                                         orient=tk.HORIZONTAL, resolution=0.01, command=self.slider_update,
                                         label='Change Constant Coefficients ' + char))
            self.sliders[i].grid(row=i // 2, column=i % 2, sticky=tk.W)
            self.sliders[i].set(random.randrange(-10, 11))

    def slider_update(self, val):
        values = [slider.get() for slider in self.sliders]
        self.plotter.set_system(values)
        self.plotter.plot_direction_field()
        self.canvas.draw()
        self.plotter.clear_figure()

    def on_click_figure(self, event):
        if event.xdata and event.ydata:
            self.plotter.plot_trajectories((event.xdata - 0.5) * 10, (event.ydata - 0.5) * 10)
            self.plotter.plot_direction_field()
            self.canvas.draw()
            self.plotter.clear_figure()

    def quit(self):
        self.root.quit()
        self.root.destroy()


if __name__ == "__main__":
    app = App()
    tk.mainloop()
