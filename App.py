import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from ODEs.ODEPlotter import ODEPlotter
from ODEs.ODESolver import ODESolver
from UI.PopupWindow import PopupWindow
import random


class App:
    def __init__(self):
        # create different sections of the app
        self.root = tk.Tk()
        self.root.geometry("800x1100")
        self.control_frame = tk.Frame(self.root)
        self.plot_frame = tk.Frame(self.root)
        self.solution_frame = tk.Frame(self.root)
        self.root.wm_title("Ordinary Differential Equations")
        self.control_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.solution_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.plot_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        # plot frame initialize
        self.fig = Figure()
        self.plotter = ODEPlotter(self.fig)
        # control frame initialize
        self.sliders = []
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.plot_frame)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.callbacks.connect('button_press_event', self.on_click_figure)
        self.matrix_text = [tk.StringVar(), tk.StringVar()]
        self.set_up_control_frame()
        # solution frame initialize
        self.solver = ODESolver()
        self.solutions = [tk.StringVar(), tk.StringVar()]
        self.set_up_solution_frame()

    def set_up_control_frame(self):
        for i, char in enumerate(['a', 'b', 'c', 'd']):
            self.sliders.append(tk.Scale(master=self.control_frame, from_=-10, to=10, tickinterval=4, length=200,
                                         orient=tk.HORIZONTAL, resolution=0.01, command=self.slider_update,
                                         label='Change Constant Coefficients ' + char))
            self.sliders[i].grid(row=i // 2, column=i % 2, sticky=tk.W)
            self.sliders[i].set(random.randrange(-10, 11))
        self.set_up_text_field()
        button = tk.Button(master=self.control_frame, text="Type in Coefficients", font="Verdana 10 bold",
                           command=self.popup)
        button.grid(row=1, column=3)

    def popup(self):
        popup_window = PopupWindow(self.root)
        [popup_window.entry_boxes[i].insert(tk.END, str(slider.get())) for i, slider in enumerate(self.sliders)]
        self.root.wait_window(popup_window.top)
        if popup_window.input_array:
            [slider.set(popup_window.input_array[i]) for i, slider in enumerate(self.sliders)]

    def slider_update(self, val):
        values = [slider.get() for slider in self.sliders]
        self.solver.set_matrix(values)
        self.plotter.set_system(values)
        self.update_text_field()
        self.plotter.plot_direction_field()
        self.canvas.draw()
        self.plotter.clear_figure()
        self.update_solution()

    def on_click_figure(self, event):
        if event.xdata and event.ydata:
            self.plotter.plot_trajectories((event.xdata - 0.5) * 10, (event.ydata - 0.5) * 10)
            self.plotter.plot_direction_field()
            self.canvas.draw()
            self.plotter.clear_figure()

    def set_up_text_field(self):
        x1_text = tk.Label(self.control_frame, font="Verdana 13 bold",
                           textvariable=self.matrix_text[0])

        x1_text.grid(row=0, column=2)
        x2_text = tk.Label(self.control_frame, font="Verdana 13 bold",
                           textvariable=self.matrix_text[1])
        x2_text.grid(row=1, column=2)

    def update_text_field(self):
        values = [slider.get() for slider in self.sliders]
        if values[1] >= 0:
            sign1 = "+"
        else:
            sign1 = "-"
        if values[3] >= 0:
            sign2 = "+"
        else:
            sign2 = "-"
        self.matrix_text[0].set("x1' = {0}x1 {1} {2}x2".format(values[0], sign1, abs(values[1])))
        self.matrix_text[1].set("x2' = {0}x1 {1} {2}x2".format(values[2], sign2, abs(values[3])))

    def update_solution(self):
        solutions = self.solver.solve_ODE()
        if solutions is not None:
            for i in range(len(solutions)):
                self.solutions[i].set(solutions[i])

    def set_up_solution_frame(self):
        text = tk.Label(self.solution_frame, font="Verdana 15 bold", text="General Solution")
        text.pack()
        solution_x1 = tk.Label(self.solution_frame, font="Verdana 11 bold", textvariable=self.solutions[0])
        solution_x1.pack()
        solution_x1 = tk.Label(self.solution_frame, font="Verdana 11 bold", textvariable=self.solutions[1])
        solution_x1.pack()

    def quit(self):
        self.root.quit()
        self.root.destroy()


if __name__ == "__main__":
    app = App()
    tk.mainloop()
