import tkinter as tk
from tkinter import ttk, messagebox
from entrada_colonias import Entrada_colonias
from total_diluciones import Total_diluciones
from columna_colonias import Columna_colonias
from funciones import Calc_promed
from menu import Main_menu


def bloquer(*args):
    dils = [dilA, dilB, dilC, dilD, dilE]
    for i in dils:
        if i[0] > entry_no_dil.get():
            for j in i[1:6]:
                j.delval()
                j.readonly()
        elif i[0] <= entry_no_dil.get():
            for j in i[1:6]:
                j.write()


def calc():
    A = Columna_colonias([A1.get(), A2.get(), A3.get(), A4.get(), A5.get()],
                         [A1.get(), A2.get(), A3.get(), A4.get(), A5.get()], 'A')
    if A.depured != []:
        B = Columna_colonias([B1.get(), B2.get(), B3.get(), B4.get(), B5.get()],
                             [B1.get(), B2.get(), B3.get(), B4.get(), B5.get()], 'B')
        C = Columna_colonias([C1.get(), C2.get(), C3.get(), C4.get(), C5.get()],
                             [C1.get(), C2.get(), C3.get(), C4.get(), C5.get()], 'C')
        D = Columna_colonias([D1.get(), D2.get(), D3.get(), D4.get(), D5.get()],
                             [D1.get(), D2.get(), D3.get(), D4.get(), D5.get()], 'D')
        E = Columna_colonias([E1.get(), E2.get(), E3.get(), E4.get(), E5.get()],
                             [E1.get(), E2.get(), E3.get(), E4.get(), E5.get()], 'E')

        cols = [A, B, C, D, E]
        for i in cols:
            if i.rechazo() != False:
                messagebox.showwarning('Valor atípico', i.rechazo())

        # suma = sum(A.depured) + sum(B.depured) + sum(C.depured) + sum(D.depured) + sum(E.depured)
        ufc = Calc_promed([A.depured, B.depured, C.depured, D.depured, E.depured], float(entry_alic.get()),
                          tot_dil.max_dil)
        # ufc = calc_ufc(media, float(entry_alic.get()), tot_dil.max_dil)
        messagebox.showinfo('Cálculo',
                            f'Total de colonias: {ufc.tot_col} \nPromedio de UFCs: ({ufc.numerador}) / {ufc.denominador} = {("%.4f" % ufc.promed())} UFC\nFórmula: {("%.4f" % ufc.promed())} UFC * (1/{entry_alic.get()} mL) * (1/{tot_dil.str_max_dil}) \n\nConcentración: {ufc.calc_ufc()} UFC/mL')
    else:
        messagebox.showerror('Primera columna vacía',
                             'No puede dejar la primer columna vacía, modifique la dilución máxima si requiere otra.')


ventana = tk.Tk()
ventana.geometry('600x300')
ventana.title('Cuenta viable con múltiples muestras')
ventana.iconbitmap('agar.ico')

# Menu
menu_principal = Main_menu(ventana)
menu_principal.mostrar()

# Configuración superior
config = ttk.Frame(ventana, width=150)

label_no_dil = ttk.Label(config, text='Cantidad de diluciones:')
label_no_dil.grid(row=0, column=1, sticky='E')

# label_no_rep = ttk.Label(config, text='Cantidad de repeticiones:')
# label_no_rep.grid(row=1, column=1, sticky='E')

label_alic = ttk.Label(config, text='Alícuota de transferencia:\n(mL o g)')
label_alic.grid(row=2, column=1, sticky='E')

label_sp = ttk.Label(config, text='')
label_sp.grid(row=3, column=0)

entry_no_dil = tk.Scale(config, from_=1, to=5, orient=tk.HORIZONTAL)
entry_no_dil.grid(row=0, column=2)

# entry_no_rep = tk.Scale(config, from_=1, to=5, orient=tk.HORIZONTAL)
# entry_no_rep.grid(row=1, column=2)

sv_alic = tk.StringVar(value='0.1')
entry_alic = ttk.Entry(config, textvariable=sv_alic, justify=tk.CENTER)
entry_alic.grid(row=2, column=2, pady=10, sticky=tk.N)

button_calc = ttk.Button(config, text='Calcular', command=calc)
button_calc.grid(row=2, column=3, padx=20)

config.grid(row=0, column=1, sticky='W', padx=55)
# Fin configuración superior

# Inicio parrilla de colonias

parrilla = ttk.Frame(ventana, width=400)

label1 = ttk.Label(parrilla, text='1')
label1.grid(row=5, column=0)
label2 = ttk.Label(parrilla, text=2)
label2.grid(row=6, column=0)
label3 = ttk.Label(parrilla, text='3')
label3.grid(row=7, column=0)
label4 = ttk.Label(parrilla, text='4')
label4.grid(row=8, column=0)
label5 = ttk.Label(parrilla, text='5')
label5.grid(row=9, column=0)

labelA = ttk.Label(parrilla, text='A')
labelA.grid(row=10, column=1)
labelB = ttk.Label(parrilla, text='B')
labelB.grid(row=10, column=2)
labelC = ttk.Label(parrilla, text='C')
labelC.grid(row=10, column=3)
labelD = ttk.Label(parrilla, text='D')
labelD.grid(row=10, column=4)
labelE = ttk.Label(parrilla, text='E')
labelE.grid(row=10, column=5)

label_dil = ttk.Label(parrilla, text='Dilución:\n')
label_dil.grid(row=4, column=0)

tot_dil = Total_diluciones(parrilla, 4, 1)
# tot_dil.entry1.bind("<Return>", tot_dil.printer())


A1 = Entrada_colonias(parrilla, 5, 1)
A1.write()
A2 = Entrada_colonias(parrilla, 6, 1)
A2.write()
A3 = Entrada_colonias(parrilla, 7, 1)
A3.write()
A4 = Entrada_colonias(parrilla, 8, 1)
A4.write()
A5 = Entrada_colonias(parrilla, 9, 1)
A5.write()

B1 = Entrada_colonias(parrilla, 5, 2)
B2 = Entrada_colonias(parrilla, 6, 2)
B3 = Entrada_colonias(parrilla, 7, 2)
B4 = Entrada_colonias(parrilla, 8, 2)
B5 = Entrada_colonias(parrilla, 9, 2)

C1 = Entrada_colonias(parrilla, 5, 3)
C2 = Entrada_colonias(parrilla, 6, 3)
C3 = Entrada_colonias(parrilla, 7, 3)
C4 = Entrada_colonias(parrilla, 8, 3)
C5 = Entrada_colonias(parrilla, 9, 3)

D1 = Entrada_colonias(parrilla, 5, 4)
D2 = Entrada_colonias(parrilla, 6, 4)
D3 = Entrada_colonias(parrilla, 7, 4)
D4 = Entrada_colonias(parrilla, 8, 4)
D5 = Entrada_colonias(parrilla, 9, 4)

E1 = Entrada_colonias(parrilla, 5, 5)
E2 = Entrada_colonias(parrilla, 6, 5)
E3 = Entrada_colonias(parrilla, 7, 5)
E4 = Entrada_colonias(parrilla, 8, 5)
E5 = Entrada_colonias(parrilla, 9, 5)

dilA = [1, A1, A2, A3, A4, A5]
dilB = [2, B1, B2, B3, B4, B5]
dilC = [3, C1, C2, C3, C4, C5]
dilD = [4, D1, D2, D3, D4, D5]
dilE = [5, E1, E2, E3, E4, E5]

parrilla.grid(row=1, column=1, padx=10)
# Fin parrilla de colonias


entry_no_dil.bind('<ButtonRelease>', bloquer)

ventana.mainloop()
