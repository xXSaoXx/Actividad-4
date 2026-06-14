import tkinter as tk
from tkinter import messagebox


def crear_archivo(nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("Hola mundo!")


def archivo_mayus(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
        return contenido.upper()


def mostrar_mensaje_correcto(titulo, mensaje):
    ventana_mensaje = tk.Toplevel()
    ventana_mensaje.title(titulo)
    ventana_mensaje.geometry("280x160")
    ventana_mensaje.resizable(False, False)

    tk.Label(
        ventana_mensaje,
        text=mensaje,
        justify="left",
        font=("Arial", 10)
    ).pack(padx=25, pady=25)

    tk.Button(
        ventana_mensaje,
        text="Aceptar",
        width=12,
        command=ventana_mensaje.destroy
    ).pack(pady=5)

    ventana_mensaje.grab_set()


def procesar_archivo():
    nombre = entrada_nombre.get()

    if nombre == "":
        messagebox.showerror("Error", "Digite el nombre del archivo")
        return

    try:
        crear_archivo(nombre)
        contenido_mayus = archivo_mayus(nombre)

        mostrar_mensaje_correcto(
            "Datos correctos",
            f"Nombre del archivo: {nombre}"
        )

        resultado.config(text=contenido_mayus)

    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontro el archivo")
    except UnicodeDecodeError:
        messagebox.showerror("Error", "No se pudo leer el archivo")
    except OSError:
        messagebox.showerror("Error", "No se pudo crear o leer el archivo")


def limpiar():
    entrada_nombre.delete(0, tk.END)
    resultado.config(text="")


ventana = tk.Tk()
ventana.title("Archivo de texto")
ventana.geometry("430x230")

tk.Label(
    ventana,
    text="Digite el nombre del archivo de texto:"
).grid(row=0, column=0, padx=10, pady=10, sticky="w")

entrada_nombre = tk.Entry(ventana, width=30)
entrada_nombre.grid(row=0, column=1, padx=10, pady=10)

tk.Button(
    ventana,
    text="Crear archivo",
    width=15,
    command=procesar_archivo
).grid(row=1, column=0, pady=10)

tk.Button(
    ventana,
    text="Limpiar",
    width=15,
    command=limpiar
).grid(row=1, column=1, pady=10)

resultado = tk.Label(ventana, text="", fg="blue", font=("Arial", 11))
resultado.grid(row=2, column=0, columnspan=2, pady=15)

ventana.mainloop()
