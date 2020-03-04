import tkinter as tk
from tkinter import ttk

from modules.ui.dh_table_tab import DhTableTab



class MainFrame(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('750x500')
        self.title('Robotics ExGen')

        self._init_tabs()

        self.mainloop()


    def _init_tabs(self):
        tab_control = ttk.Notebook(self)

        tab1 = DhTableTab(tab_control)
        tab_control.add(tab1, text = 'Generate DH-Table')

        tab_control.pack(expand = True, fill = 'both')
