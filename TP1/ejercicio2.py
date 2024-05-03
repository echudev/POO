# TP - Clases y Objetos

# Ejercicio 2
# Realizar un programa que ayude al pintor a realizar el presupuesto.
# El programa debe calcular la superficie total a pintar y la cantidad
# de litros de pintura, de una cantidad determinada de habitaciones.
# Cada pared puede tener una abertura (puertas, ventas, etc) o ninguna.
# Las aberturas no se pintan, restar su superficie de las paredes.
# Utilizar objetos para almacenar la información de las habitaciones.
import math


class Habitacion:
    habitaciones_creadas = 1

    def __init__(self, alto, ancho, largo):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
        self.aberturas = []
        self.nro_habitacion = Habitacion.habitaciones_creadas
        Habitacion.habitaciones_creadas += 1

    def agregar_abertura(self, abertura):
        self.aberturas.append(abertura)

    def calcular_superficie_abierta(self):
        if len(self.aberturas) == 0:
            return 0
        superficie_abierta = 0
        for abertura in self.aberturas:
            superficie_abierta += abertura.calcular_superficie()
        return superficie_abierta

    def calcular_superficie(self):
        techo = self.largo * self.ancho
        paredes = (2 * self.largo + 2 * self.ancho) * self.alto
        return techo + paredes - self.calcular_superficie_abierta()


class Abertura:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def calcular_superficie(self):
        return self.alto * self.ancho


def main():
    habitaciones = []

    print("Bienvenido a PintorApp")
    print("Lo ayudaremos a calcular la cantidad de pintura que necesita \n")

    while True:
        try:
            cantidad_habitaciones = int(input("¿Cuántas habitaciones desea pintar?: "))
            math.log10(cantidad_habitaciones)
            break
        except (TypeError, ValueError):
            print("Ingrese un número entero mayor a cero.")
            continue

    for i in range(cantidad_habitaciones):
        print(f"\nHabitación {i + 1}")
        while True:
            try:
                largo = float(input("Ingrese en metros el largo de la habitación: "))
                math.log10(largo)
                break
            except (TypeError, ValueError):
                print("Ingrese un número entero mayor a cero.")
                continue
        while True:
            try:
                ancho = float(input("Ingrese en metros el ancho de la habitación: "))
                math.log10(ancho)
                break
            except (TypeError, ValueError):
                print("Ingrese un número entero mayor a cero.")
                continue
        while True:
            try:
                alto = float(input("Ingrese en metros el alto de la habitación: "))
                math.log10(alto)
                break
            except (TypeError, ValueError):
                print("Ingrese un número entero mayor a cero.")
                continue
        habitacion = Habitacion(alto, ancho, largo)
        while True:
            try:
                aberturas = int(
                    input(
                        "\n¿Cuántas aberturas tiene la habitación? \n0. Ninguna \n1. Una \n2. Dos \n3. Tres \n4. Cuatro \nElija una opción: "
                    )
                )
                if aberturas == 0:
                    break
                if aberturas < 0 or aberturas > 4:
                    print("Ingrese un número entre 0 y 4")
                    continue
                break
            except TypeError:
                print("Ingrese un número entre 0 y 4.")
                continue
        for i in range(aberturas):
            while True:
                try:
                    alto = float(
                        input(f"\nIngrese en metros el alto de la abertura {i + 1}:")
                    )
                    math.log10(alto)
                    break
                except (TypeError, ValueError):
                    print("Ingrese un número válido, para la coma utilice el punto.")
                    continue
            while True:
                try:
                    ancho = float(
                        input(f"Ingrese en metros el ancho de la abertura {i + 1}:")
                    )
                    math.log10(ancho)
                    break
                except (TypeError, ValueError):
                    print("Ingrese un número válido, para la coma utilice el punto.")
                    continue
            abertura = Abertura(alto, ancho)
            habitacion.agregar_abertura(abertura)
        habitaciones.append(habitacion)

    sup_total = 0
    pintura_total = 0
    print("------------------------------------------------------------------")
    for habitacion in habitaciones:
        superficie_a_pintar = habitacion.calcular_superficie()
        print(f"\nHabitación {habitacion.nro_habitacion}")
        print(f"Superficie a pintar: {superficie_a_pintar:.2f} m2")
        print(f"Pintura necesaria: {superficie_a_pintar/10:.2f} Litros por mano")
        pintura_total += superficie_a_pintar / 10
        sup_total += superficie_a_pintar
    print(f"\nSuperficie total a pintar: {sup_total:.2f} m2")
    print(f"Pintura total necesaria: {pintura_total:.2f} Litros por mano")


if __name__ == "__main__":
    main()
