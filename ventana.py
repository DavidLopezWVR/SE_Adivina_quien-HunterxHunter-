# ventana.py
import tkinter as tk
from tkinter import messagebox
from main import filtrar_personajes, obtener_personaje_adivinado
from base_datos import obtener_personajes
from PIL import Image, ImageTk

# Inicialización
personajes = obtener_personajes()
respuestas = {}
preguntas = ["es_cazador", "tiene_nen", "es_humano", "es_masculino"]  # claves de preguntas
indice_pregunta = 0

# Ventana
ventana = tk.Tk()
ventana.title("Adivina el personaje")

# Widgets
pregunta_label = tk.Label(ventana, text="", font=("Arial", 16))
pregunta_label.pack(pady=10)

respuesta_var = tk.StringVar()
entrada_respuesta = tk.Entry(ventana, textvariable=respuesta_var)
entrada_respuesta.pack(pady=10)

boton = tk.Button(ventana, text="Responder", command=lambda: procesar_respuesta())
boton.pack(pady=10)

label_imagen = tk.Label(ventana)
label_imagen.pack(pady=10)

# Funciones
def mostrar_pregunta():
    if indice_pregunta < len(preguntas):
        clave = preguntas[indice_pregunta]
        texto = clave.replace("_", " ").capitalize() + "?"
        pregunta_label.config(text=texto)
    else:
        terminar_juego()

def procesar_respuesta():
    global indice_pregunta
    if indice_pregunta >= len(preguntas):
        return

    clave = preguntas[indice_pregunta]
    respuesta = respuesta_var.get().capitalize()
    if respuesta not in ["Sí", "No"]:
        messagebox.showerror("Error", "Responde con 'Sí' o 'No'")
        return

    respuestas[clave] = respuesta
    indice_pregunta += 1
    respuesta_var.set("")
    mostrar_pregunta()

def terminar_juego():
    candidatos = filtrar_personajes(personajes, respuestas)
    personaje = obtener_personaje_adivinado(candidatos)

    if personaje:
        nombre = personaje["nombre"]
        imagen = personaje["imagen"]
        mostrar_imagen_personaje(imagen)
        messagebox.showinfo("Personaje adivinado", f"¡Es {nombre}!")
    elif candidatos:
        nombres = ", ".join([p["nombre"] for p in candidatos])
        messagebox.showinfo("Adivinanza múltiple", f"Podría ser: {nombres}")
    else:
        messagebox.showinfo("Sin coincidencias", "No se encontró ningún personaje.")

def mostrar_imagen_personaje(imagen_path):
    try:
        img = Image.open(imagen_path)
        img = img.resize((200, 200))
        img_tk = ImageTk.PhotoImage(img)
        label_imagen.config(image=img_tk)
        label_imagen.image = img_tk
    except Exception as e:
        print(f"No se pudo cargar la imagen: {e}")

# Iniciar con la primera pregunta
mostrar_pregunta()

ventana.mainloop()
