from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo = 'Procurando ninguém em latim',
            tipo = 'F',
            data_lancamento = '2003-07-04',
            likes = 2340,
            dislikes = 40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)
    
    def test_verifica_campos_serializados(self) -> None:
        """Teste que verifica os campos que estão serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['likes'], self.programa.likes)
