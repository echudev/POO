# TP Clases y Objetos

# Ejercicio 1
# Realizar un programa para calcular el monto total a pagar por cada mesa en un restaurante.
# Realizar el programa usando objetos para almacenar información de los pedidos de cada mesa
# y calcular el importe total a pagar.

class Mesa:
        def __init__(self, numero):
            self.numero = numero
            self.pedidos = []

        def agregar_pedido(self, pedido):
            self.pedidos.append(pedido)

        def calcular_total(self):
            total = 0
            for pedido in self.pedidos:
                total += pedido.precio * pedido.cantidad
            return total

class Pedido:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

def main():
    mesas = []
    
    print("----------------------------------------")
    print("Bienvenido a Maranda's Bar Administrator \n")
    while True:
        print("Menu:")
        print("1. Abrir Mesa")
        print("2. Crear Pedido")
        print("3. Ver Mesas abiertas e importe total a pagar")
        print("4. Cerrar una mesa")
        print("5. Cerrar todas las mesas")
        print("6. Salir")
 
        try:
            choice = int(input("Seleccione una opcion: "))
        except ValueError:
            print("Selección inválida. Intente de nuevo.")
            continue
 
        if choice == 1:
            mesa_nueva = input("\n Ingrese el numero de la mesa: ")
            mesas.append(Mesa(int(mesa_nueva)))
            print(f'La mesa {mesa_nueva} ahora está abierta \n')
        elif choice == 2:
            mesa_numero = int
            mesa_encontrada = False
            while True:
                try:
                    mesa_numero = input("\n Ingrese el numero de la mesa para el pedido: ")
                    mesa_numero = int(mesa_numero)
                    break
                except ValueError:
                    print("Selección inválida. Inténtelo de nuevo.")
                    continue
            for mesa in mesas:
                if mesa.numero == int(mesa_numero):
                    while True:
                        try:
                            nombre_pedido = input("Ingrese el nombre del pedido: ")
                            break
                        except ValueError:
                            print("El nombre del pedido no puede estar vacío.")
                            continue
                    while True:
                        try:
                            precio_pedido = float(input("Ingrese el precio del pedido: "))
                            break
                        except ValueError:
                            print("El precio del pedido debe ser un número.")
                            continue
                    while True:
                        try:
                            cantidad_pedido = int(input("Ingrese la cantidad del pedido: "))
                            if cantidad_pedido <= 0:
                                print("La cantidad del pedido debe ser mayor que cero.")
                                continue
                            break
                        except ValueError:
                            print("La cantidad del pedido debe ser un número entero.")
                            continue
                    mesa.agregar_pedido(Pedido(nombre_pedido, precio_pedido, cantidad_pedido))
                    print(f'Pedido agregado a la mesa {mesa_numero} \n')
                    mesa_encontrada = True
                    break
            if not mesa_encontrada:
                print(f'La mesa {mesa_numero} no existe \n')
        elif choice == 3:
            print("\n Mesas abiertas:")
            if len(mesas) == 0:
                print("No hay mesas abiertas")
            else:
                for mesa in mesas:
                    print(f'Mesa {mesa.numero}:')
                    if len(mesa.pedidos) == 0:
                        print("No hay pedidos para esta mesa \n")
                    else:
                        for pedido in mesa.pedidos:
                            print(f'{pedido.nombre} * {pedido.cantidad} = ${pedido.precio * pedido.cantidad }')
            total_a_pagar = [mesa.calcular_total() for mesa in mesas]
            print(f'El importe total a pagar para todas las mesas es: ${sum(total_a_pagar)} \n')
        elif choice == 4:
            mesa_numero = int
            mesa_encontrada = False
            while True:
                try:
                    mesa_numero = input("\n Ingrese el numero de la mesa para el pedido: ")
                    mesa_numero = int(mesa_numero)
                    break
                except ValueError:
                    print("Selección inválida. Inténtelo de nuevo.")
                    continue
            for mesa in mesas:
                if mesa.numero == int(mesa_numero):
                    mesas.remove(mesa)
                    print(f'La mesa {mesa_numero} ha sido cerrada \n')
                    mesa_encontrada = True
                    break
            if not mesa_encontrada:
                print(f'La mesa {mesa_numero} no existe \n')
        elif choice == 5:
            mesas = []
            print("\n Todas las mesas han sido cerradas \n")
        elif choice == 6:
            print("\n Gracias por usar nuestro sistema! Hasta la próxima! \n")
            break
        else:
            print("Selección inválida. Intente de nuevo.")
    
if __name__ == "__main__":
    main()
