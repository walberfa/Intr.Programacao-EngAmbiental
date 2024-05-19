import unittest
from src.triangulos import verifica_se_valido, define_tipos


class TestTriangulo(unittest.TestCase):
    def test_valido(self):
        """Subtestes validam o retorno da função."""
        with self.subTest("É válido."):
            self.assertTrue(verifica_se_valido(90, 60, 30))
        with self.subTest("Contém um valor igual a zero."):
            self.assertFalse(verifica_se_valido(0, 90, 90))
        with self.subTest("Soma é diferente de 180."):
            self.assertFalse(verifica_se_valido(90, 50, 30))

    def test_tipo(self):
        """Confirma se é triangulo retangulo."""
        self.assertEqual(define_tipos(90, 60, 30), "retangulo")


if __name__ == '__main__':
    unittest.main()
