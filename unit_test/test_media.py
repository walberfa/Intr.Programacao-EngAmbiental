import unittest
from src.calculo_media_ifce import media_ifce


class TestCalculoMedia(unittest.TestCase):
    """Unit tests para validar a função media_ifce."""

    def test_aluno_aprovado(self):
        """Valida o cenário aluno aprovado."""
        self.assertEqual(media_ifce(7, 8), "aprovado")

    def test_aluno_em_af(self):
        """Valida o cenário aluno em avaliação final."""
        self.assertEqual(media_ifce(5, 7.8), "em avaliação final")

    def test_aluno_reprovado(self):
        """Valida o cenário aluno reprovado."""
        self.assertEqual(media_ifce(2, 3), "reprovado")


if __name__ == '__main__':
    unittest.main()
