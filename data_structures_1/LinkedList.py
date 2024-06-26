class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def agregar_adelante(self, data):
        new_node = Node(data)               
        new_node.next = self.head
        self.head = new_node
    
    def agregar_atras(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current=self.head
        while current:
                if current.next is None:
                    current.next = new_node
                    break
                current = current.next

    def buscar(self, dato):
        if self.head is None:
            print("La lista está vacía")
            return False
        else:
            current=self.head
            while current:
                if current.data == dato:
                    print(f'El dato: {dato} se encuentra en la lista')
                    return True
                current = current.next
            print(f'El dato: {dato} NO se encuentra en la lista')
            return False
    

    def borrar(self, dato):
        if self.head is None:
            print("La lista está vacía")
        elif self.head.data == dato:
            print(f'Se eliminó el dato: {dato} de la lista')
            self.head = self.head.next
            return
        else:
            current=self.head
            while current.next:
                if current.next.data == dato:
                    print(f'Se eliminó el dato: {dato} de la lista')
                    current.next = current.next.next
                    return
                current = current.next
            print(f'El dato: {dato} no se encuentra en la lista')

    def listar(self):
        if self.head is None:
            return None
        else:
            lista = []
            current = self.head
            while current:
                lista.append(current.data)
                current = current.next
            return lista
   

# Programa con datos de prueba
if __name__ == "__main__":
    llist = LinkedList()
    
    llist.agregar_atras("un dato")
    llist.agregar_adelante(1)
    llist.agregar_adelante(5)
    llist.agregar_atras("un dato final")
    llist.agregar_adelante(13)
    llist.agregar_adelante(87)

    llist.buscar(13)
    llist.borrar(87)

    datos = llist.listar()
    print(f'Datos en la lista: {datos}')