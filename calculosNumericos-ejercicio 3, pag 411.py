import math

class algebra:
    @staticmethod
    def calcular_logaritmo_neperiano(valor):
        
        try:
            if valor <= 0:
                raise ArithmeticError("El valor debe ser un numero positivo")
            resultado_logaritmo = math.log(valor)
            print("Resultado del logaritmo=", resultado_logaritmo)
        
        except ArithmeticError:
            print("El valor debe de ser un numero positivo para calcular el logaritmo")
    @staticmethod
    def calcular_raiz_cuadrada(valor):
        
        try:
            if valor < 0:
                raise ArithmeticError("El valor debe de ser positivo o 0 para calcular su raiz")
            resultado_raiz = math.sqrt(valor)
            print("Resultado de la raiz cuadrada=", resultado_raiz)
        
        except ArithmeticError:
            print("El valor debe ser un numero positivo para calcular su raiz")

class recta:
    @staticmethod
    def calcular_pendiente(x1, x2, y1, y2):
        
        try:
            if x1 == x2:
                raise ArithmeticError("Los valores x1 y x2 no pueden ser iguales")
            m = (y2 - y1) / (x2 - x1)
            print("La pendiente de la recta es =", m)
        
        except ArithmeticError:
            print("Para calcular la pendiente, los valores de x no pueden ser iguales")
    @staticmethod
    def calcular_punto_medio(x1, x2, y1, y2):
        
            puntox = (x1 + x2)/2
            puntoy = (y1 + y2)/2
            print(f"El punto medio de la recta es = ({puntox} , {puntoy})")

class ecuacion:
    @staticmethod        
    def calcular_raices_ecuacion(a, b, c):
        try:
            if a == 0:
                raise ArithmeticError("El valor de a no puede ser cero")

            discriminante = b**2 - 4*a*c

            if discriminante < 0:
                print("La ecuación no tiene raíces reales")
            
            elif discriminante == 0:
                x = -b / (2*a)
                print(f"La ecuación tiene una raíz real: x = {x}")
            
            else:
                x1 = (-b + math.sqrt(discriminante)) / (2*a)
                x2 = (-b - math.sqrt(discriminante)) / (2*a)
                print(f"Las raíces son x1 = {x1} y x2 = {x2}")

        except ArithmeticError:
            print("Para calcular las raics, el valor de a no puede ser cero")

class conversion:
    @staticmethod
    def calcular_base(num, base):
        try:
            if base < 2:
                raise ArithmeticError("La base debe de ser mayor o igual a 2")
            
            if num == 0:
                print("El numero convertido es 0")
            else:
                residuo_total = ""
                while num > 0:
                    residuo = num % base
                    residuo_total = str(residuo) + residuo_total
                    num = num // base
                print(f"El numero convertido es {residuo_total}")
        
        except ValueError:
            print("Debe ingresar valores numericos enteros")

        except ArithmeticError:
            print("La base debe ser mayor o igual a 2")

                

valor = float(input("Digite un un valor numerico = "))

x1 = float(input("Digite x1 = "))
x2 = float(input("Digite x2 = "))
y1 = float(input("Digite y1 = "))
y2 = float(input("Digite y2 = "))

a = float(input("Digite a de la ecuacion cuadratica = "))
b = float(input("Digite b de la ecuacion cuadratica = "))
c = float(input("Digite c de la ecuacion cuadratica = "))

num = int(input("Digite el numero en base 10 = "))
base = int(input("Digite la base = "))

algebra.calcular_logaritmo_neperiano(valor)
algebra.calcular_raiz_cuadrada(valor)

recta.calcular_pendiente(x1, x2, y1, y2)
recta.calcular_punto_medio(x1, x2, y1, y2)

ecuacion.calcular_raices_ecuacion(a, b, c)

conversion.calcular_base(num, base)