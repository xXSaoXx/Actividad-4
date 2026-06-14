import math
import tkinter as tk
from tkinter import messagebox


class algebra:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        if valor <= 0:
            raise ArithmeticError("El valor debe ser positivo para calcular el logaritmo")
        return math.log(valor)

    @staticmethod
    def calcular_raiz_cuadrada(valor):
        if valor < 0:
            raise ArithmeticError("El valor debe ser positivo o cero para calcular la raiz")
        return math.sqrt(valor)


class recta:
    @staticmethod
    def calcular_pendiente(x1, x2, y1, y2):
        if x1 == x2:
            raise ArithmeticError("Los valores x1 y x2 no pueden ser iguales")
        return (y2 - y1) / (x2 - x1)

    @staticmethod
    def calcular_punto_medio(x1, x2, y1, y2):
        puntox = (x1 + x2) / 2
        puntoy = (y1 + y2) / 2
        return puntox, puntoy


class ecuacion:
    @staticmethod
    def calcular_raices_ecuacion(a, b, c):
        if a == 0:
            raise ArithmeticError("El valor de a no puede ser cero")

        discriminante = b**2 - 4 * a * c

        if discriminante < 0:
            return "La ecuacion no tiene raices reales"

        if discriminante == 0:
            x = -b / (2 * a)
            return f"La ecuacion tiene una raiz real: x = {x}"

        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return f"Las raices son x1 = {x1} y x2 = {x2}"


class conversion:
    @staticmethod
    def calcular_base(num, base):
        if base < 2:
            raise ArithmeticError("La base debe ser mayor o igual a 2")

        if base > 36:
            raise ArithmeticError("La base maxima permitida es 36")

        if num < 0:
            raise ArithmeticError("El numero debe ser positivo")

        digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if num == 0:
            return "0"

        resultado = ""

        while num > 0:
            residuo = num % base
            resultado = digitos[residuo] + resultado
            num = num // base

        return resultado


def crear_label_entry(ventana, texto, fila):
    tk.Label(ventana, text=texto).grid(row=fila, column=0, padx=10, pady=5, sticky="w")
    entrada = tk.Entry(ventana)
    entrada.grid(row=fila, column=1, padx=10, pady=5)
    return entrada


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


def ventana_algebra():
    ventana = tk.Toplevel()
    ventana.title("Algebra")
    ventana.geometry("420x240")

    entrada_valor = crear_label_entry(ventana, "Digite un valor:", 0)

    resultado = tk.Label(ventana, text="", fg="blue", justify="left")
    resultado.grid(row=3, column=0, columnspan=2, pady=10)

    def calcular():
        try:
            valor = float(entrada_valor.get())

            logaritmo = algebra.calcular_logaritmo_neperiano(valor)
            raiz = algebra.calcular_raiz_cuadrada(valor)

            mostrar_mensaje_correcto("Dato correcto", f"Valor: {valor}")

            resultado.config(
                text=f"Logaritmo neperiano = {logaritmo}\nRaiz cuadrada = {raiz}"
            )

        except ValueError:
            messagebox.showerror("Error", "Digite un valor numerico")
        except ArithmeticError as error:
            messagebox.showerror("Error", str(error))

    def limpiar():
        entrada_valor.delete(0, tk.END)
        resultado.config(text="")

    tk.Button(ventana, text="Calcular", width=15, command=calcular).grid(
        row=1, column=0, pady=10
    )

    tk.Button(ventana, text="Limpiar", width=15, command=limpiar).grid(
        row=1, column=1, pady=10
    )


def ventana_recta():
    ventana = tk.Toplevel()
    ventana.title("Recta")
    ventana.geometry("450x320")

    entrada_x1 = crear_label_entry(ventana, "Digite x1:", 0)
    entrada_x2 = crear_label_entry(ventana, "Digite x2:", 1)
    entrada_y1 = crear_label_entry(ventana, "Digite y1:", 2)
    entrada_y2 = crear_label_entry(ventana, "Digite y2:", 3)

    resultado = tk.Label(ventana, text="", fg="blue", justify="left")
    resultado.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular():
        try:
            x1 = float(entrada_x1.get())
            x2 = float(entrada_x2.get())
            y1 = float(entrada_y1.get())
            y2 = float(entrada_y2.get())

            pendiente = recta.calcular_pendiente(x1, x2, y1, y2)
            puntox, puntoy = recta.calcular_punto_medio(x1, x2, y1, y2)

            mostrar_mensaje_correcto(
                "Datos correctos",
                f"x1: {x1}\nx2: {x2}\ny1: {y1}\ny2: {y2}"
            )

            resultado.config(
                text=f"Pendiente = {pendiente}\nPunto medio = ({puntox}, {puntoy})"
            )

        except ValueError:
            messagebox.showerror("Error", "Digite unicamente valores numericos")
        except ArithmeticError as error:
            messagebox.showerror("Error", str(error))

    def limpiar():
        entrada_x1.delete(0, tk.END)
        entrada_x2.delete(0, tk.END)
        entrada_y1.delete(0, tk.END)
        entrada_y2.delete(0, tk.END)
        resultado.config(text="")

    tk.Button(ventana, text="Calcular", width=15, command=calcular).grid(
        row=4, column=0, pady=10
    )

    tk.Button(ventana, text="Limpiar", width=15, command=limpiar).grid(
        row=4, column=1, pady=10
    )


def ventana_ecuacion():
    ventana = tk.Toplevel()
    ventana.title("Ecuacion cuadratica")
    ventana.geometry("460x270")

    entrada_a = crear_label_entry(ventana, "Digite a:", 0)
    entrada_b = crear_label_entry(ventana, "Digite b:", 1)
    entrada_c = crear_label_entry(ventana, "Digite c:", 2)

    resultado = tk.Label(ventana, text="", fg="blue", wraplength=400)
    resultado.grid(row=5, column=0, columnspan=2, pady=10)

    def calcular():
        try:
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            c = float(entrada_c.get())

            respuesta = ecuacion.calcular_raices_ecuacion(a, b, c)

            mostrar_mensaje_correcto(
                "Datos correctos",
                f"a: {a}\nb: {b}\nc: {c}"
            )

            resultado.config(text=respuesta)

        except ValueError:
            messagebox.showerror("Error", "Digite unicamente valores numericos")
        except ArithmeticError as error:
            messagebox.showerror("Error", str(error))

    def limpiar():
        entrada_a.delete(0, tk.END)
        entrada_b.delete(0, tk.END)
        entrada_c.delete(0, tk.END)
        resultado.config(text="")

    tk.Button(ventana, text="Calcular", width=15, command=calcular).grid(
        row=3, column=0, pady=10
    )

    tk.Button(ventana, text="Limpiar", width=15, command=limpiar).grid(
        row=3, column=1, pady=10
    )


def ventana_conversion():
    ventana = tk.Toplevel()
    ventana.title("Conversion de base")
    ventana.geometry("420x240")

    entrada_num = crear_label_entry(ventana, "Numero en base 10:", 0)
    entrada_base = crear_label_entry(ventana, "Base:", 1)

    resultado = tk.Label(ventana, text="", fg="blue")
    resultado.grid(row=4, column=0, columnspan=2, pady=10)

    def calcular():
        try:
            num = int(entrada_num.get())
            base = int(entrada_base.get())

            convertido = conversion.calcular_base(num, base)

            mostrar_mensaje_correcto(
                "Datos correctos",
                f"Numero en base 10: {num}\nBase: {base}"
            )

            resultado.config(text=f"Numero convertido = {convertido}")

        except ValueError:
            messagebox.showerror("Error", "Digite valores numericos enteros")
        except ArithmeticError as error:
            messagebox.showerror("Error", str(error))

    def limpiar():
        entrada_num.delete(0, tk.END)
        entrada_base.delete(0, tk.END)
        resultado.config(text="")

    tk.Button(ventana, text="Calcular", width=15, command=calcular).grid(
        row=2, column=0, pady=10
    )

    tk.Button(ventana, text="Limpiar", width=15, command=limpiar).grid(
        row=2, column=1, pady=10
    )


ventana_principal = tk.Tk()
ventana_principal.title("Calculadora matematica")
ventana_principal.geometry("350x260")

tk.Label(
    ventana_principal,
    text="Seleccione una opcion",
    font=("Arial", 14)
).pack(pady=15)

tk.Button(
    ventana_principal,
    text="Algebra",
    width=25,
    command=ventana_algebra
).pack(pady=5)

tk.Button(
    ventana_principal,
    text="Recta",
    width=25,
    command=ventana_recta
).pack(pady=5)

tk.Button(
    ventana_principal,
    text="Ecuacion cuadratica",
    width=25,
    command=ventana_ecuacion
).pack(pady=5)

tk.Button(
    ventana_principal,
    text="Conversion de base",
    width=25,
    command=ventana_conversion
).pack(pady=5)

ventana_principal.mainloop()
