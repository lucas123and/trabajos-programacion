import tkinter as tk
from tkinter import messagebox

# --- preguntas y respuestas con categorías ---
categorias = {
    'Geografía': [
        {'pregunta': 'Capital de Francia?', 'opciones': ['París', 'Madrid', 'Berlín', 'Roma'], 'respuesta': 'París'},
        {'pregunta': 'País con mayor población?', 'opciones': ['China', 'India', 'EE.UU.', 'Brasil'], 'respuesta': 'China'}
    ],
    'Matemáticas': [
        {'pregunta': '2 + 2 * 2 = ?', 'opciones': ['6', '8', '4', '2'], 'respuesta': '6'},
        {'pregunta': 'Raíz cuadrada de 16?', 'opciones': ['4', '8', '2', '6'], 'respuesta': '4'}
    ],
    'Literatura': [
        {'pregunta': 'Autor de "Cien Años de Soledad"?', 'opciones': ['Gabriel García Márquez', 'Pablo Neruda', 'Mario Vargas Llosa', 'J.K. Rowling'], 'respuesta': 'Gabriel García Márquez'},
        {'pregunta': 'Quién escribió "Hamlet"?', 'opciones': ['Shakespeare', 'Cervantes', 'Dante', 'Tolstoi'], 'respuesta': 'Shakespeare'}
    ]
}

categorias_lista = list(categorias.keys())
categoria_actual_index = 0
indice = 0
puntos = 0
preguntas = []

def iniciar_categoria():
    global preguntas, indice
    cat = categorias_lista[categoria_actual_index]
    preguntas = categorias[cat]
    indice = 0
    frame_categorias.pack_forget()
    frame_preguntas.pack(pady=20)
    mostrar_pregunta()
    label_categoria.config(text=f'Categoría: {cat}')

def verificar_respuesta(opcion):
    global indice, puntos, categoria_actual_index
    if opcion == preguntas[indice]['respuesta']:
        puntos += 1
        messagebox.showinfo('Correcto', '¡Respuesta correcta!')
    else:
        messagebox.showerror('Incorrecto', f'Respuesta incorrecta. La correcta era: {preguntas[indice]["respuesta"]}')
    indice += 1
    if indice < len(preguntas):
        mostrar_pregunta()
    else:
        categoria_actual_index += 1
        if categoria_actual_index < len(categorias_lista):
            messagebox.showinfo('Siguiente categoría', f'Ahora pasamos a la siguiente categoría')
            frame_preguntas.pack_forget()
            iniciar_categoria()
        else:
            messagebox.showinfo('Fin del juego', f'Tus puntos totales: {puntos}')
            ventana.destroy()

def mostrar_pregunta():
    pregunta = preguntas[indice]['pregunta']
    opciones = preguntas[indice]['opciones']
    label_pregunta.config(text=pregunta)
    for i, opcion in enumerate(opciones):
        botones_opciones[i].config(text=opcion, command=lambda t=opcion: verificar_respuesta(t))

# --- ventana principal ---
ventana = tk.Tk()
ventana.title('Preguntados Completo')
ventana.geometry('600x400')
ventana.configure(bg='#1e1e2f')

# --- frame de categorías ---
frame_categorias = tk.Frame(ventana, bg='#1e1e2f')
frame_categorias.pack(pady=50)

tk.Label(frame_categorias, text='Presiona iniciar para comenzar el juego completo:', bg='#1e1e2f', fg='white', font=('Segoe UI', 16)).pack(pady=10)
btn_iniciar = tk.Button(frame_categorias, text='Iniciar', bg='#34c759', fg='white', font=('Segoe UI', 14, 'bold'), bd=0, activebackground='#5cd37c', width=20, command=iniciar_categoria)
btn_iniciar.pack(pady=20)

# --- frame de preguntas ---
frame_preguntas = tk.Frame(ventana, bg='#1e1e2f')
label_categoria = tk.Label(frame_preguntas, text='', bg='#1e1e2f', fg='white', font=('Segoe UI', 14))
label_categoria.pack(pady=5)
label_pregunta = tk.Label(frame_preguntas, text='', bg='#1e1e2f', fg='white', font=('Segoe UI', 16), wraplength=500)
label_pregunta.pack(pady=20)

botones_opciones = []
for i in range(4):
    btn = tk.Button(frame_preguntas, text='', bg='#007aff', fg='white', font=('Segoe UI', 14), bd=0, activebackground='#3399ff', width=25)
    btn.pack(pady=5)
    botones_opciones.append(btn)

ventana.mainloop()