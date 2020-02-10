import tkinter as tk
from UI.NumericStringParser import NumericStringParser


class PopupWindow:
    def __init__(self, parent):
        top = self.top = tk.Toplevel(parent)
        self.nsp = NumericStringParser()
        self.entry_boxes = []
        self.input_array = []
        for i, char in enumerate(['a', 'b', 'c', 'd']):
            label = tk.Label(top, text='constant {0}:'.format(char))
            self.entry_boxes.append(tk.Entry(top))
            label.grid(row=(i // 2) * 2, column=i % 2, sticky=tk.W)
            self.entry_boxes[i].grid(row=(i // 2) * 2 + 1, column=i % 2, sticky=tk.W)
        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.grid(row=4, column=0)

    def send(self):
        self.input_array = [self.nsp.eval(x.get()) for x in self.entry_boxes]
        self.top.destroy()
