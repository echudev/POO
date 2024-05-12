import unittest
from LinkedList import LinkedList

class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_agregar_adelante(self):
        self.linked_list.agregar_adelante(10)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertIsNone(self.linked_list.head.next) 

    def test_agregar_adelante_varios_elementos(self):
        self.linked_list.agregar_adelante(20)
        self.linked_list.agregar_adelante(10)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertEqual(self.linked_list.head.next.data, 20)

    def test_agregar_atras(self):
        self.linked_list.agregar_atras(10)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertIsNone(self.linked_list.head.next)

    def test_agregar_atras_varios_elementos(self):
        self.linked_list.agregar_atras(10)
        self.linked_list.agregar_atras(20)
        self.assertEqual(self.linked_list.head.data, 10)
        self.assertEqual(self.linked_list.head.next.data, 20)

    def test_buscar_elemento_existente(self):
        self.linked_list.agregar_adelante(5)
        self.linked_list.agregar_adelante(8)
        self.assertTrue(self.linked_list.buscar(5))

    def test_buscar_elemento_inexistente(self):
        self.linked_list.agregar_adelante(5)
        self.linked_list.agregar_adelante(8)
        self.assertFalse(self.linked_list.buscar(30))

    def test_buscar_elemento_en_lista_vacia(self):
        self.assertFalse(self.linked_list.buscar(10))

    def test_borrar_elemento_head(self):
        self.linked_list.agregar_adelante(10)
        self.linked_list.borrar(10)
        self.assertIsNone(self.linked_list.head)

    def test_borrar_elemento_cualquiera(self):
        self.linked_list.agregar_adelante(42)
        self.linked_list.agregar_adelante(13)
        self.linked_list.borrar(42)
        self.assertEqual(self.linked_list.head.data, 13)
        self.assertIsNone(self.linked_list.head.next)

  
if __name__ == "__main__":
    unittest.main()