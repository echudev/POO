class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def agregar(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.agregar(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.agregar(data)
            else:
                self.right = BinaryTree(data)

   
    def listar(self):
        datos = []
        #agrego datos de la rama izquierda
        if self.left:
            datos += self.left.listar()
        #agrego el dato del nodo actual
        datos.append(self.data)
        #agrego datos de la rama derecha
        if self.right:
            datos += self.right.listar()
        return datos
     
    def buscar(self, data):
        if self.data == data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.buscar(data)
            else:
                return False
        
        if data > self.data:
            if self.right:
                return self.right.buscar(data)
            else:
                return False

    def encuentra_maximo(self):
        if self.right is None:
            return self.data
        return self.right.encuentra_maximo()
    
    def encuentra_minimo(self):
        if self.left is None:
            return self.data
        return self.left.encuentra_minimo()


#existen 3 posibilidades al borrar un nodo: 
# 1) que no tenga hijos- 
# 2) que tenga un solo nodo hijo
# 3) que tenga 2 nodos hijos, uno a la izquierda y otro a la derecha

    def borrar(self, data):
        if data < self.data:
            if self.left: 
                # si es menor y hay otra rama izquierda, sigue buscando
                self.left = self.left.borrar(data)
            # si no hay más ramas izquierdas, significa que no se encuentra el valor en el arbol
            # el método en este caso devuelve "self" (deja todo igual)
        elif data > self.data:
            # si es mayor al dato del nodo y hay rama derecha, sigue buscando
            if self.right:
                self.right = self.right.borrar(data)
            # si no hay más rama derecha, devuelve "self"
        else:
            if self.left is None and self.right is None:
                return  None
            if self.left is None: 
                return self.right
            if self.right is None:
                return self.left
            
            valor_minimo = self.right.encuentra_minimo()
            self.data = valor_minimo
            self.right = self.right.borrar(valor_minimo)

        return self


if __name__ == '__main__':
    #Creo un bnarytree con el numero 8 en el nodo raíz
    bt = BinaryTree(17)
    
    #Agrego datos al binarytree
    bt.agregar(4)
    bt.agregar(20)
    bt.agregar(1)
    bt.agregar(9)
    bt.agregar(20)
    bt.agregar(18)
    bt.agregar(23)
    bt.agregar(34)

    #muestro datos en consola
    datos = bt.listar()
    print(datos)

    #pruebo método buscar
    busqueda1 = bt.buscar(9)
    busqueda2 = bt.buscar(33)
    print(busqueda1, busqueda2)

    #pruebo eliminar el dato 14 y luego uno inexistente
    bt.borrar(18)
    bt.borrar(7)
    datos2 = bt.listar()
    print(datos2)