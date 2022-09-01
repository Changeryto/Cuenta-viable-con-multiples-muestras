from validaciones import diluciones
import tkinter as tk
from tkinter import ttk


class Total_diluciones:
    def __init__(self, ventana, row, column, *args):
        self.ventana = ventana
        self.row = row
        self.column = column

        self.sv1 = tk.StringVar(value='1E-0')

        self.entry1 = ttk.Entry(self.ventana, width=15, textvariable=self.sv1, validate='key', validatecommand=(ventana.register(diluciones), "%P"), justify='center')
        self.entry1.grid(row=self.row, column=self.column)

        self.sv2 = tk.StringVar(value="{:.0E}".format(float(self.sv1.get()) / 10))
        self.sv3 = tk.StringVar(value="{:.0E}".format(float(self.sv1.get()) / 100))
        self.sv4 = tk.StringVar(value="{:.0E}".format(float(self.sv1.get()) / 1000))
        self.sv5 = tk.StringVar(value="{:.0E}".format(float(self.sv1.get()) / 10000))

        self.entry2 = ttk.Entry(self.ventana, width=15, textvariable=self.sv2, state=tk.DISABLED, justify='center')
        self.entry2.grid(row=self.row, column=(self.column+1))

        self.entry3 = ttk.Entry(self.ventana, width=15, textvariable=self.sv3, state=tk.DISABLED, justify='center')
        self.entry3.grid(row=self.row, column=(self.column + 2))

        self.entry4 = ttk.Entry(self.ventana, width=15, textvariable=self.sv4, state=tk.DISABLED, justify='center')
        self.entry4.grid(row=self.row, column=(self.column + 3))

        self.entry5 = ttk.Entry(self.ventana, width=15, textvariable=self.sv5, state=tk.DISABLED, justify='center')
        self.entry5.grid(row=self.row, column=(self.column + 4))

        for ev in [self.entry1]:
            ev.bind('<FocusOut>', self.update_dil)
            ev.bind('<Return>', self.update_dil)

    def update_dil(self, *args):
        self.sv2.set(value="{:.0E}".format(float(self.sv1.get()) / 10))
        self.sv3.set(value="{:.0E}".format(float(self.sv1.get()) / 100))
        self.sv4.set(value="{:.0E}".format(float(self.sv1.get()) / 1000))
        self.sv5.set(value="{:.0E}".format(float(self.sv1.get()) / 10000))

    @property
    def max_dil(self):
        return float(self.sv1.get())

    @property
    def str_max_dil(self):
        return self.sv1.get()

