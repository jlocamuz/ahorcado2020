import unittest
from parameterized import parameterized
from partida import Partida
from servicesPartidas import ServicesPartidas


class TestPartida(unittest.TestCase):

    # Crea una partida con valores iniciales.
    # palabra_acierto: se guarda las letras acertadas por el usuario
    # tipo_palabra: para dar orientacion al jugador
    # palabra: palabra que tiene que adivinar
    def test_constructor_con_valores_iniciales_partida(self):
        partida = Partida('python', 'lenguaje de programacion', 2, 'Claudio')
        self.assertDictEqual(partida.__dict__, {'_palabra':
                                                ['P', 'Y', 'T', 'H', 'O', 'N'],
                                                '_tipo_palabra':
                                                'LENGUAJE DE PROGRAMACION',
                                                '_intentos': 2,
                                                '_nombre_jugador': 'CLAUDIO',
                                                '_palabra_aciertos':
                                                [None, None, None, None, None,
                                                 None], })

    # Verificar exceptions, palabra no puede ser vacia
    def test_exceptions_valor_inicial_palabra(self):
        with self.assertRaises(ValueError):
            Partida('', 'lenguaje de programacion', 2, 'Claudio')

    # Verificar exceptions nombre_jugador no puede ser vacia
    def test_exceptions_valor_inicial_nombre_jugador(self):
        with self.assertRaises(ValueError):
            Partida('Python', 'lenguaje de programacion', 2, '')

    # Verificar exceptions tipo_palabra no puede ser vacia
    def test_exceptions_valor_inicial_tipo_palabra(self):
        with self.assertRaises(ValueError):
            Partida('Python', '', 2, 'Claudio')

    # Verificar exceptions intentos no puede ser negativo,
    # anularia intentos
    def test_exceptions_valor_inicial_intentos(self):
        with self.assertRaises(ValueError):
            Partida('Python', 'lenguaje de programacion', -1, 'Claudio')

    # La funcion iniciar_partida intancia un objeto del tipo Partida
    # Lo intentos que tiene el jugador depende de la longitud de la palabra
    # multiplicado por el valor intentos ingresados en esta funcion
    # return partida: Partida
    def test_iniciar_partida(self):
        partida = ServicesPartidas().iniciar_partida('python',
                                                     'lenguaje de programacio',
                                                     '3',
                                                     'claudio'
                                                     )

        self.assertDictEqual(partida.__dict__, {'_palabra':
                                                ['P', 'Y', 'T', 'H', 'O', 'N'],
                                                '_tipo_palabra':
                                                'LENGUAJE DE PROGRAMACIO',
                                                '_intentos': 18,
                                                '_nombre_jugador': 'CLAUDIO',
                                                '_palabra_aciertos':
                                                [None, None, None, None,
                                                 None, None], })

    # La funcion iniciar_partida puede ser llamada sin palabra ni tipo de
    # palabra, esta busca en un reposotorio una palabra de manera random
    # return partida: Partida
    def test_iniciar_partida_palabra_random(self):
        partida = ServicesPartidas().iniciar_partida('', '', 3, 'claudio')
        # partida es un objeto de tipo Partida()
        palabra = partida.palabra
        tipo_palabra = partida.tipo_palabra
        palabra_acierto = partida.palabra_aciertos
        intentos = partida.intentos
        self.assertDictEqual(partida.__dict__, {'_palabra': palabra,
                                                '_tipo_palabra': tipo_palabra,
                                                '_intentos': intentos,
                                                '_nombre_jugador': 'CLAUDIO',
                                                '_palabra_aciertos':
                                                palabra_acierto, })

    # La dificultad de los intentos es de 1-10
    def test_exceptions_valor_intentos_mayor(self):
        with self.assertRaises(ValueError):
            ServicesPartidas().iniciar_partida('', '', 15, 'claudio')

    # La dificultad de los intentos es de 1-10
    def test_exceptions_valor_intentos_menor(self):
        with self.assertRaises(ValueError):
            ServicesPartidas().iniciar_partida('', '', 0, 'claudio')

    # La funcion get_random_palabra selecciona una palabra y tipo de palabra
    # alearoria de un repositorio
    # return {'palabra':'python', 'tipo_palabra':'LENGUAJE DE PROGRAMACION'}
    def test_get_random_palabra(self):
        palabra = ServicesPartidas().get_random_palabra()
        self.assertEqual(palabra, {'palabra': palabra.get('palabra'),
                                   'tipo_palabra': palabra.get('tipo_palabra')}
                         )

    # La funcion intentar_letra prueba si esta la letra en la partida.palabra
    # si esta la guarda y continuia
    # si se temrminana los intentos muestra Perdio
    # si partida.palabra es igual a partida.palabra_aciertos muestra Gano
    # si todavia le quedan intentos y no completo palabra_aciertos muestra
    # Continuo
    @parameterized.expand([
        (1, ['P', 'Y', 'T', 'H', 'O', 'N'], 'Gano'),
        (2, ['M', 'R', 'P', 'Y', 'T', 'H', 'O', 'N'], 'Gano'),
        (1, ['M', 'R', 'P', 'U', 'I', 'E'], 'Perdio'),
        (1, ['M', 'R', 'P', 'U'], 'Continua'),
    ])
    def test_intentar_letra(self, dificultad, letras, result):
        servicePartida = ServicesPartidas()
        partida = servicePartida.iniciar_partida('python',
                                                 'lenguaje de programacion',
                                                 dificultad, 'claudio')
        for letra in letras:
            result_aux = servicePartida.intentar_letra(partida, letra)
        self.assertEqual(result_aux, result)

    @parameterized.expand([
        (1, ['M', 'R', 'P', 'U', 'I', 'E', 'E', 'E'], 'Perdio')
    ])
    def test_exceptionsintentar_letra_(self, dificultad, letras, result):
        servicePartida = ServicesPartidas()
        partida = servicePartida.iniciar_partida('python',
                                                 'lenguaje de programacion',
                                                 dificultad, 'claudio')
        with self.assertRaises(ValueError):
            for letra in letras:
                servicePartida.intentar_letra(partida, letra)


if __name__ == '__main__':
    unittest.main()
