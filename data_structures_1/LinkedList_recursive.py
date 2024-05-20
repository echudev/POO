class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    # agrega de forma ordenada el valor que se le pase al método agregar
    def agregar(self,num, nodo_actual=None):    
        if self.head == None:
            self.head = Node(num)
            return

        if nodo_actual is None:
            nodo_actual = self.head
        
        if num > nodo_actual.data:
            if nodo_actual.next is None:
                nodo_actual.next = Node(num)
                return
            else:
                self.agregar(num, nodo_actual.next)
                
        if num <= nodo_actual.data:
            nodo_nuevo = Node(nodo_actual.data)
            nodo_nuevo.next = nodo_actual.next
            nodo_actual.data = num
            nodo_actual.next = nodo_nuevo
            

    # devuelve una lista con todos los valores de la linkedList
    def listar(self, nodo_actual=None):
        if self.head == None:
            return None
        if nodo_actual == None:
            nodo_actual = self.head
        
        lista = []
        lista.append(nodo_actual.data)
        if nodo_actual.next:
            lista += self.listar(nodo_actual.next)
        return lista



if __name__ == "__main__":
    # instancio una LinkedList en ll
    ll = LinkedList()

    # pruebo que esté vacía
    print(ll.listar())
    
    # agrego un valor y pruebo que lo liste
    ll.agregar(10)
    ll.agregar(11)
    ll.agregar(12)
    ll.agregar(18)
    ll.agregar(13)
    ll.agregar(98)
    ll.agregar(-4)
    print(ll.listar())

    