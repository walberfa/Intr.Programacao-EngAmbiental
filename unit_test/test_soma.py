import unittest
from src.soma import soma


class TestSoma(unittest.TestCase):
    """Unit tests para validar a função soma."""

    def test_soma(self):
        """Verifica se 2 + 3 é igual a 5."""
        self.assertEqual(soma(2, 3), 5)

    def test_type_error(self):
        """Verifica o retorno de soma quando recebe valores não numéricos."""
        with self.assertRaises(TypeError):
            self.assertEqual(soma(2, "a"), 2)


if __name__ == '__main__':
    unittest.main()
