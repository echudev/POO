import unittest
from LinkedList_recursive import LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_agregar(self):
        self.linked_list.agregar(10)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertIsNone(self.linked_list.head.next) 

    def test_buscar_elemento_existente(self):
        self.linked_list.agregar(5)
        self.linked_list.agregar(8)
        self.assertTrue(self.linked_list.buscar(5))

    def test_buscar_elemento_inexistente(self):
        self.linked_list.agregar(5)
        self.linked_list.agregar(8)
        self.assertFalse(self.linked_list.buscar(30))

    def test_buscar_elemento_en_lista_vacia(self):
        self.assertFalse(self.linked_list.buscar(10))

    def test_borrar_elemento_head(self):
        self.linked_list.agregar(10)
        self.linked_list.borrar(10)
        self.assertIsNone(self.linked_list.head)

    def test_borrar_elemento_cualquiera(self):
        self.linked_list.agregar(42)
        self.linked_list.agregar(13)
        self.linked_list.borrar(42)
        self.assertEqual(self.linked_list.head.data, 13)
        self.assertIsNone(self.linked_list.head.next)
    
    def test_listar(self):
        self.linked_list.agregar(10)
        self.linked_list.agregar(30)
        self.linked_list.agregar(14)
        self.linked_list.agregar(-2)
        datos = self.linked_list.listar()
        self.assertListEqual(datos, [-2, 10, 14, 30])
  
if __name__ == "__main__":
    unittest.main()