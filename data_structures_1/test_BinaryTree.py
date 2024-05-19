import unittest
from BinaryTree import BinaryTree

class BinaryTreeTest(unittest.TestCase):

    def setUp(self):
        self.bt = BinaryTree(5)
        self.bt.agregar(10)
        self.bt.agregar(22)
        self.bt.agregar(18)
        self.bt.agregar(40)
        self.bt.agregar(45)

    def test_init(self):
       self.assertEqual(self.bt.data, 5)
       self.assertEqual(self.bt.right.data, 10)

    def test_agregar(self):
        self.bt.agregar(3)
        self.assertEqual(self.bt.left.data, 3)
    
    def test_buscar(self):
        self.assertTrue(self.bt.buscar(22))
        self.assertFalse(self.bt.buscar(30))
    
    def test_listar(self):
        self.assertEqual(self.bt.listar(), [5, 10, 18, 22, 40, 45])

    def test_borrar(self):
        self.bt.borrar(22)
        self.assertEqual(self.bt.listar(), [5, 10, 18, 40, 45])


if __name__ == "__main__":
    unittest.main()