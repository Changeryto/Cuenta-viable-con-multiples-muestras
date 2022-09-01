"""
A1 = tk.StringVar(value='')
entry_A1 = ttk.Entry(ventana, textvariable=A1, validate='key', validatecommand=(ventana.register(colonias), "%P"))
entry_A1.grid(row=5, column=1)

A2 = tk.StringVar(value='')
entry_A2 = ttk.Entry(ventana, textvariable=A2, validate='key', validatecommand=(ventana.register(colonias), "%P"))
entry_A2.grid(row=6, column=1)

A3 = tk.StringVar(value='')
entry_A3 = ttk.Entry(ventana, textvariable=A3, validate='key', validatecommand=(ventana.register(colonias), "%P"))
entry_A3.grid(row=7, column=1)

A4 = tk.StringVar(value='')
entry_A4 = ttk.Entry(ventana, textvariable=A4, validate='key', validatecommand=(ventana.register(colonias), "%P"))
entry_A4.grid(row=8, column=1)

A5 = tk.StringVar(value='')
entry_A5 = ttk.Entry(ventana, textvariable=A5, validate='key', validatecommand=(ventana.register(colonias), "%P"))
entry_A5.grid(row=9, column=1)
"""



"""
class Total_diluciones:
    def __init__(self, ventana, row, column):
        self.ventana = ventana
        self.row = row
        self.column = column

        self.sv1 = tk.StringVar(value='1E-0')
        self.entry1 = ttk.Entry(self.ventana, width=15, textvariable=self.sv1, validate='key', validatecommand=(ventana.register(diluciones), "%P"))
        self.entry1.grid(row=self.row, column=self.column)

        self.sv2 = tk.StringVar(value=str(float(self.sv1.get()) / 10))
        self.sv3 = tk.StringVar(value=str(float(self.sv1.get()) / 100))
        self.sv4 = tk.StringVar(value=str(float(self.sv1.get()) / 1000))
        self.sv5 = tk.StringVar(value=str(float(self.sv1.get()) / 10000))

        self.entry2 = ttk.Entry(self.ventana, width=15, textvariable=self.sv2)
        self.entry2.grid(row=self.row, column=(self.column+1))

        self.entry3 = ttk.Entry(self.ventana, width=15, textvariable=self.sv3)
        self.entry3.grid(row=self.row, column=(self.column + 2))

        self.entry4 = ttk.Entry(self.ventana, width=15, textvariable=self.sv4)
        self.entry4.grid(row=self.row, column=(self.column + 3))

        self.entry5 = ttk.Entry(self.ventana, width=15, textvariable=self.sv5)
        self.entry5.grid(row=self.row, column=(self.column + 4))

        #self.entry1.bind('<Return>', self.update_dil())

    def update_dil(self):
        self.sv2 = tk.StringVar(value=str(float(self.sv1.get()) / 10))
        self.sv3 = tk.StringVar(value=str(float(self.sv1.get()) / 100))
        self.sv4 = tk.StringVar(value=str(float(self.sv1.get()) / 1000))
        self.sv5 = tk.StringVar(value=str(float(self.sv1.get()) / 10000))
        """