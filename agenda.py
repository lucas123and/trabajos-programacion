import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import datetime
import json

# --- funciones ---
def agregar_contacto():
    nombre = entrada_nombre.get().strip()
    telefono = entrada_telefono.get().strip()
    email = entrada_email.get().strip()
    if not nombre:
        messagebox.showwarning('Aviso', 'El nombre es obligatorio')
        return
    contacto = {'nombre': nombre, 'telefono': telefono, 'email': email}
    lista_contactos.insert(tk.END, f"{nombre} | {telefono} | {email}")
    contactos.append(contacto)
    guardar_contactos()
    entrada_nombre.delete(0, tk.END)
    entrada_telefono.delete(0, tk.END)
    entrada_email.delete(0, tk.END)

def eliminar_contacto():
    seleccion = lista_contactos.curselection()
    if not seleccion:
        messagebox.showwarning('Aviso', 'Seleccione un contacto para eliminar')
        return
    index = seleccion[0]
    lista_contactos.delete(index)
    contactos.pop(index)
    guardar_contactos()

def editar_contacto():
    seleccion = lista_contactos.curselection()
    if not seleccion:
        messagebox.showwarning('Aviso', 'Seleccione un contacto para editar')
        return
    index = seleccion[0]
    contacto = contactos[index]
    nuevo_nombre = simpledialog.askstring('Editar', 'Nombre:', initialvalue=contacto['nombre'])
    nuevo_telefono = simpledialog.askstring('Editar', 'Teléfono:', initialvalue=contacto['telefono'])
    nuevo_email = simpledialog.askstring('Editar', 'Email:', initialvalue=contacto['email'])
    if nuevo_nombre:
        contacto.update({'nombre': nuevo_nombre, 'telefono': nuevo_telefono, 'email': nuevo_email})
        lista_contactos.delete(index)
        lista_contactos.insert(index, f"{nuevo_nombre} | {nuevo_telefono} | {nuevo_email}")
        guardar_contactos()

def mostrar_fecha():
    ahora = datetime.datetime.now()
    label_fecha.config(text=ahora.strftime('%d/%m/%Y %H:%M:%S'))
    ventana.after(1000, mostrar_fecha)

def guardar_contactos():
    with open('contactos.json', 'w') as f:
        json.dump(contactos, f)

def cargar_contactos():
    try:
        with open('contactos.json', 'r') as f:
            datos = json.load(f)
            for c in datos:
                contactos.append(c)
                lista_contactos.insert(tk.END, f"{c['nombre']} | {c['telefono']} | {c['email']}")
    except FileNotFoundError:
        pass

# --- ventana principal ---
ventana = tk.Tk()
ventana.title('Agenda Profesional Avanzada')
ventana.geometry('600x600')
ventana.configure(bg='#1e1e2f')

contactos = []

# --- frame de entradas ---
frame_entradas = tk.Frame(ventana, bg='#1e1e2f')
frame_entradas.pack(pady=15)

tk.Label(frame_entradas, text='Nombre:', bg='#1e1e2f', fg='white', font=('Segoe UI', 12)).grid(row=0, column=0, padx=5, pady=5)
entrada_nombre = ttk.Entry(frame_entradas, width=25, font=('Segoe UI', 12))
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text='Teléfono:', bg='#1e1e2f', fg='white', font=('Segoe UI', 12)).grid(row=1, column=0, padx=5, pady=5)
entrada_telefono = ttk.Entry(frame_entradas, width=25, font=('Segoe UI', 12))
entrada_telefono.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_entradas, text='Email:', bg='#1e1e2f', fg='white', font=('Segoe UI', 12)).grid(row=2, column=0, padx=5, pady=5)
entrada_email = ttk.Entry(frame_entradas, width=25, font=('Segoe UI', 12))
entrada_email.grid(row=2, column=1, padx=5, pady=5)

# --- botones ---
boton_agregar = tk.Button(frame_entradas, text='Agregar', bg='#34c759', fg='white', font=('Segoe UI', 12, 'bold'), bd=0, activebackground='#5cd37c', command=agregar_contacto)
boton_agregar.grid(row=3, column=0, padx=5, pady=10, sticky='nsew')
boton_eliminar = tk.Button(frame_entradas, text='Eliminar', bg='#ff3b30', fg='white', font=('Segoe UI', 12, 'bold'), bd=0, activebackground='#ff5c5c', command=eliminar_contacto)
boton_eliminar.grid(row=3, column=1, padx=5, pady=10, sticky='nsew')
boton_editar = tk.Button(frame_entradas, text='Editar', bg='#007aff', fg='white', font=('Segoe UI', 12, 'bold'), bd=0, activebackground='#3399ff', command=editar_contacto)
boton_editar.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky='nsew')

# --- lista de contactos ---
lista_contactos = tk.Listbox(ventana, width=80, height=15, font=('Segoe UI', 12), bg='#2e2e4e', fg='white', selectbackground='#34c759', selectforeground='white', bd=0)
lista_contactos.pack(pady=15)

# --- fecha y hora ---
label_fecha = tk.Label(ventana, text='', bg='#1e1e2f', fg='white', font=('Segoe UI', 12, 'italic'))
label_fecha.pack(pady=5)
mostrar_fecha()

# --- cargar contactos guardados ---
cargar_contactos()

ventana.mainloop()