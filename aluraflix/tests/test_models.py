from django.test import TestCase
from aluraflix.models import Programa


class ProgramaModelTestCasa(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            data_lancamento = '2003-07-04'
        )

    def test_verifica_atributos_do_programa(self) -> None:
        """Teste que verifica os atributos de um programa com valores default"""
        self.assertEquals(self.programa.titulo, 'Procurando ninguém em latim')
        self.assertEquals(self.programa.tipo, 'F')
        self.assertEquals(self.programa.data_lancamento, '2003-07-04')
        self.assertEquals(self.programa.likes, 0)
        self.assertEquals(self.programa.dislikes, 0)
