import tkinter as tk
from tkinter import ttk

from modules.dh.table import DhTable



class DhTableTab(tk.Frame):
    def __init__(self, master: ttk.Notebook):
        super().__init__(master)

        self._frame_options = tk.Frame(self)
        self._frame_options.pack(padx = 5, pady = 5)

        self._frame_buttons = tk.Frame(self)
        self._frame_buttons.pack(padx = 5, pady = 5)

        self._frame_table = tk.Frame(self, bg = '#000000')
        # Do not pack the table-frame here as it should not be shown from the beginning.

        btn_generate_dh = ttk.Button(self._frame_buttons, text = 'Generate!', command = self.callback_generate_table)
        btn_generate_dh.pack()


    def callback_generate_table(self):
        # Hide the frame.
        self._frame_table.pack_forget()
        for slave in self._frame_table.grid_slaves():
            slave.grid_remove()
            slave.destroy()

        table = DhTable(5)
        table.generate_random_joints()

        self._frame_table.grid_columnconfigure(0, pad = 1)
        self._frame_table.grid_columnconfigure(1, pad = 1)
        self._frame_table.grid_columnconfigure(2, pad = 1)
        self._frame_table.grid_columnconfigure(3, pad = 1)

        width_0 = 5
        width_1 = 15
        width_2 = 10
        width_3 = 15
        width_4 = 10

        tk.Label(self._frame_table, text = 'i', width = width_0).grid(column = 0, row = 0, pady = (0, 1))
        tk.Label(self._frame_table, text = 'θ_i', width = width_1).grid(column = 1, row = 0, pady = (0, 1))
        tk.Label(self._frame_table, text = 'd_i', width = width_2).grid(column = 2, row = 0, pady = (0, 1))
        tk.Label(self._frame_table, text = 'α_i', width = width_3).grid(column = 3, row = 0, pady = (0, 1))
        tk.Label(self._frame_table, text = 'a_i', width = width_4).grid(column = 4, row = 0, pady = (0, 1))

        for it_i, it_joint in enumerate(table.get_joints()):
            tk.Label(self._frame_table, text = str(it_joint.get_index()), width = width_0).grid(column = 0, row = it_i + 1)
            tk.Label(self._frame_table, text = str(it_joint.get_theta_str()), width = width_1).grid(column = 1, row = it_i + 1)
            tk.Label(self._frame_table, text = str(it_joint.get_d_str()), width = width_2).grid(column = 2, row = it_i + 1)
            tk.Label(self._frame_table, text = str(it_joint.get_alpha_str()), width = width_3).grid(column = 3, row = it_i + 1)
            tk.Label(self._frame_table, text = str(it_joint.get_a_str()), width = width_4).grid(column = 4, row = it_i + 1)

        # Show the frame again.
        self._frame_table.pack(padx = 5, pady = 5)
