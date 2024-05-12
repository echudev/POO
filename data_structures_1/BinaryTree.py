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
        pass

    def borrar(self, data):
        pass


if __name__ == '__main__':
    #Creo un bnarytree con el numero 8 en el nodo raíz
    bt = BinaryTree(8)
    
    #Agrego datos al binarytree
    bt.agregar(2)
    bt.agregar(1)
    bt.agregar(14)

    #muestro datos en consola
    datos = bt.listar()
    print(datos)