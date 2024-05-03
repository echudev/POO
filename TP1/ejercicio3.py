# TP Clases y Objetos

# Ejercicio 3
# Realizar el programa usando objetos.
# El programa debe permitir:
# A) Cargar países, almacenando el nombre, el nombre de su capital y su población.
# B) Cargar los países limítrofes a un país ya cargado. Los países limítrofes deben ser objetos ya creados en el
# punto A. Cuando al país A, se le carga el país limítrofe B, automáticamente se cargue en el país B, el país
# limítrofe A. Es decir, si a Argentina le cargamos el país limítrofe Uruguay, automáticamente se debe cargar
# a Uruguay el país limítrofe Argentina.
# D) El usuario selecciona un país, y el programa muestra todos sus países limítrofes.
# No incluir print() ni input() dentro de las clases.

import os


class Pais:
    # Diccionario de países, donde la clave es el nombre del país y el valor es el objeto Pais.
    paises = {}

    def __init__(self, nombre, capital, poblacion):
        self.nombre = nombre
        self.capital = capital
        self.poblacion = poblacion
        self.limitrofes = []
        self.set_pais()

    def set_pais(self):
        Pais.paises.setdefault(self.nombre, self)
    
    @classmethod
    def get_lista_paises(cls):
        lista_paises = []
        for pais in Pais.paises.keys():
            lista_paises.append(pais)
        return lista_paises

    def set_limitrofe(self, pais):
        if pais not in self.limitrofes:
            self.limitrofes.append(pais)
        if self not in pais.limitrofes:
            pais.limitrofes.append(self)

    def get_limitrofes(self):
        lista_limitrofes = []
        for limitrofe in self.limitrofes:
            lista_limitrofes.append(limitrofe)
        return lista_limitrofes


# Función principal.

def clearConsole():
    return os.system("cls" if os.name in ("nt", "dos") else "clear")

def main():
    print("Bienvenido!")
    while True:
        print("\nMenú principal:")
        print("1. Cargar país nuevo")
        print("2. Eliminar un país")
        print("3. Ver países cargados")
        print("4. Cargar países limítrofes")
        print("5. Ver limitrofes de un pais ya cargado")
        print("6. Salir \n")

        try:
            choice = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Opción inválida. Intente de nuevo. \n")
            continue

        if choice == 1:
            nombre = input("Ingrese el nombre del país: ").strip().lower().capitalize()
            capital = input("Ingrese la capital del país: ").strip().lower().capitalize()
            try:
                poblacion = int(input("Ingrese la población del país: "))
            except ValueError:
                print("La población debe ser un número entero. Intente de nuevo. \n")
                continue
            Pais(nombre, capital, poblacion)
            clearConsole()
            print("--------------------------")
            print("  País cargado con éxito! ")
            print("--------------------------")

        elif choice == 2:
            clearConsole()
            print("\nfunción en desarrollo :)\n")

        elif choice == 3:
            if not Pais.paises:
                clearConsole()
                print("--------------------------")
                print("  No hay países cargados! ")
                print("--------------------------")
                continue
             
            clearConsole()
            print("\nPaíses cargados: \n")
            paises = Pais.get_lista_paises()
            for i, pais in enumerate(paises, start=1):
                print(f"{i}. {pais}")
            print("\n")

        elif choice == 4:
            if len(Pais.paises) < 2:
                clearConsole()
                print("Cargue al menos dos países para poder continuar. \n")
                continue
         
            # muestro los paises cargados
            clearConsole()
            print("\nPaíses cargados: \n")
            paises = Pais.get_lista_paises()
            for i, pais in enumerate(paises, start=1):
                print(f"{i}. {pais}")
            print("\n") 
 
            # usuario selecciona primer pais
            try:
                choise1 = int(input("Ingrese el número del primer país: "))
            except:
                print("Opción inválida. Intente de nuevo. \n")
                continue
            if choise1 < 1 or choise1 > len(Pais.paises):
                print("Opción inválida. Intente de nuevo. \n")
                continue
            
            pais1 = Pais.paises.get(paises[choise1 - 1], "Pais no encontrado")

            # usuario selecciona segundo pais
            try:
                choise2 = int(input("Ingrese el número del segundo país: "))
            except:
                print("Opción inválida. Intente de nuevo. \n")
                continue
            if choise2 < 1 or choise2 > len(Pais.paises):
                print("Opción inválida. Intente de nuevo. \n")
                continue
            pais2 = Pais.paises.get(paises[choise2 - 1], "Pais no encontrado")
            pais1.set_limitrofe(pais2)
            clearConsole()
            print("Países limítrofes cargados con éxito! \n")


        elif choice == 5:
            if not Pais.paises:
                clearConsole()
                print("--------------------------")
                print("  No hay países cargados! ")
                print("--------------------------")
                continue

            # muestro paises cargados
            clearConsole()
            print("\nPaíses cargados: \n")
            paises = Pais.get_lista_paises()
            for i, pais in enumerate(paises, start=1):
                print(f"{i}. {pais}")
            print("\n")

            # usuario selecciona pais
            try:
                choise = int(input("Ingrese el número del país: "))
            except:
                print("Opción inválida. Intente de nuevo. \n")
                continue
            if choise < 1 or choise > len(Pais.paises):
                print("Opción inválida. Intente de nuevo. \n")
                continue

            pais = Pais.paises.get(paises[choise - 1], None)
            limitrofes = pais.get_limitrofes()
            if not limitrofes:
                print(f"El país {pais.nombre} no tiene países limítrofes. \n")
                continue
            else:
                clearConsole()
                print(f"Los países limítrofes de {pais.nombre} son:")
                for limitrofe in limitrofes:
                    print(f"- {limitrofe.nombre}")
        
        elif choice == 6:
            clearConsole()
            print("--------------------------")
            print("    ¡Hasta la próxima!    ")
            print("--------------------------")
            break

        else:
            print("Opción inválida. Intente de nuevo. \n")


if __name__ == "__main__":
    main()
