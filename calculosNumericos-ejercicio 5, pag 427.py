def crear_archivo(nombre_archivo):
    with open(nombre_archivo, "w")as archivo:

        archivo.write("Hola mundo!")

def archivo_mayus(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido.upper())

    except FileNotFoundError:
        print("Error: no se encontro el archivo")

    except UnicodeDecodeError:
        print("Error: no se pudo leer el archivo")


def main():
    
    nombre = input("Digite el nombre del archivo de texto: ")
    crear_archivo(nombre)
    archivo_mayus(nombre)

main()