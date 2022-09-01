from validaciones import colonias
import tkinter as tk
from tkinter import ttk

class Entrada_colonias:
    """Esta clase produce un tkinter entry apta para la
    escritura del número de colonias observables en una dilución"""
    def __init__(self, ventana, row, column, state=tk.DISABLED):
        self.ventana = ventana
        self.row = row
        self.column = column
        self.sv = tk.StringVar(value='')
        self.state = state
        self.entry = ttk.Entry(self.ventana, width=15, justify='center', textvariable=self.sv, validate='key', validatecommand=(ventana.register(colonias), "%P"), state=self.state)
        self.entry.grid(row=self.row, column=self.column)

    def readonly(self):
        self.entry.config(state='readonly')

    def write(self):
        self.entry.config(state='normal')

    def delval(self):
        self.entry.delete(0, tk.END)

    def get(self):
        return self.entry.get()

    def __str__(self):
        return self.sv