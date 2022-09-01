import tkinter as tk
from tkinter import ttk, Menu, messagebox

class Main_menu:
    """Esta clase controla el menú principal de la aplicación"""
    def __init__(self, ventana):
        self.ventana = ventana

        self.menu_principal = Menu(self.ventana)

        self.submenu_ayuda = Menu(self.menu_principal, tearoff=False)

        self.submenu_ayuda.add_command(label='Notación científica', command=self.not_dec)
        self.submenu_ayuda.add_command(label='Valores atípicos', command=self.prueb_rec)

        self.submenu_ayuda.add_separator()

        self.submenu_ayuda.add_command(label='Acerca de', command=self.acerca_de)

        self.menu_principal.add_cascade(menu=self.submenu_ayuda, label='Ayuda')



    def not_dec(self):
        messagebox.showinfo('Notación científica', f'La notación científica puede escribirse con la notación E,\ndonde E significa *10^\n\nEjemplo:\n1*10^-5 = 1E-05\n1*10^5 = 1E+05')

    def prueb_rec(self):
        messagebox.showinfo('Valores atípicos', f'Con las repeticiones suficientes (3 o más), se ejecuta una prueba de rechazo Q de Dixon, si la hipótesis alternativa se acepta,se sugiere al usuario rechazar el valor atípico.\n\nTabla:\nBöhrer, A. (2008). One-sided and Two-sided Critical Values for Dixon’s Outlier Test for Sample Sizes up to n = 30. Economic Quality Control, 23(1). doi:10.1515/eqc.2008.5')

    def acerca_de(self):
        messagebox.showinfo('Acerca de', 'Programado en Python por Rubén Téllez Gerardo \nTeléfono/Telegram/WA: 771 627 5855 \nGitHub: @Changeryto \nVersión: 1.0.0')
    def mostrar(self):
        self.ventana.config(menu=self.menu_principal)

