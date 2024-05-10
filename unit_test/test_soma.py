"""Unit test para validar a função soma."""
import unittest
from soma import soma


class TestSoma(unittest.TestCase):
    """Testa soma"""
    def test_soma(self):
        """Verifica se 2 + 3 é igual a 5."""
        self.assertEqual(soma(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
