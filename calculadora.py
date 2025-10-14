import tkinter as tk
from tkinter import ttk
import math

# --- funciones de la calculadora ---
def agregar(valor):
    entrada.insert(tk.END, valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expr = entrada.get().replace('^', '**')
        resultado = eval(expr, {'__builtins__': None}, math.__dict__)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, 'Error')

# --- ventana principal ---
ventana = tk.Tk()
ventana.title('Calculadora Científica')
ventana.geometry('480x600')
ventana.resizable(False, False)
ventana.configure(bg='#2e2e2e')

# --- entrada ---
entrada = tk.Entry(ventana, font=('Segoe UI', 24), justify='right', bd=0, bg='#1e1e1e', fg='white', insertbackground='white')
entrada.grid(row=0, column=0, columnspan=6, padx=10, pady=20, ipady=15, sticky='we')

# --- botones ---
botones = [
    ('7','#4e4e4e'), ('8','#4e4e4e'), ('9','#4e4e4e'), ('/','#ff9500'), ('sqrt','#ff9500'), ('^','#ff9500'),
    ('4','#4e4e4e'), ('5','#4e4e4e'), ('6','#4e4e4e'), ('*','#ff9500'), ('(', '#4e4e4e'), (')', '#4e4e4e'),
    ('1','#4e4e4e'), ('2','#4e4e4e'), ('3','#4e4e4e'), ('-','#ff9500'), ('sin','#ff9500'), ('cos','#ff9500'),
    ('0','#4e4e4e'), ('.','#4e4e4e'), ('+', '#ff9500'), ('tan','#ff9500'), ('log','#ff9500'), ('ln','#ff9500')
]

for i, (texto, color) in enumerate(botones):
    fila = 1 + i // 6
    columna = i % 6
    boton = tk.Button(ventana, text=texto, bg=color, fg='white', font=('Segoe UI', 16), bd=0,
                      activebackground='#666666', activeforeground='white', command=lambda t=texto: agregar(t+'(' if t in ['sin','cos','tan','log','ln','sqrt'] else t))
    boton.grid(row=fila, column=columna, ipadx=10, ipady=15, padx=5, pady=5, sticky='nsew')

# --- botones especiales ---
boton_clear = tk.Button(ventana, text='C', bg='#ff3b30', fg='white', font=('Segoe UI', 18), bd=0, activebackground='#ff5c5c', activeforeground='white', command=limpiar)
boton_clear.grid(row=5, column=0, columnspan=3, ipadx=10, ipady=15, padx=5, pady=5, sticky='nsew')

boton_igual = tk.Button(ventana, text='=', bg='#34c759', fg='white', font=('Segoe UI', 18), bd=0, activebackground='#5cd37c', activeforeground='white', command=calcular)
boton_igual.grid(row=5, column=3, columnspan=3, ipadx=10, ipady=15, padx=5, pady=5, sticky='nsew')

# --- expandir filas y columnas ---
for i in range(6):
    ventana.grid_rowconfigure(i, weight=1)
for i in range(6):
    ventana.grid_columnconfigure(i, weight=1)

ventana.mainloop()
