import unittest
from parameterized import parameterized
from ahorcado import Ahorcado
from unittest.mock import patch


class TestAhorcado(unittest.TestCase):
    @parameterized.expand([
        ('Claudio', 2, ['P', 'A', 'L', 'A', 'B', 'R', 'A', '1', '2', '3'])
    ])
    # Inicial para un solo jugador, seleccionando la palabra aleatoriamente.
    # ingresa datos [nombre, dificultad, letras_para_adivinar]
    def test_un_jugador(self, nombre, dificultad, palabra):
        juego = Ahorcado()
        with patch('builtins.input', side_effect=(nombre, dificultad,
                                                  palabra[0], palabra[1],
                                                  palabra[2], palabra[3],
                                                  palabra[4], palabra[5],
                                                  palabra[6], palabra[7],
                                                  palabra[8], palabra[9])):
            result = juego.un_jugador()
            self.assertEqual(result, True)

    @parameterized.expand([('Claudio', 1, ['salir'])])
    # Ingresando la palabra salir, se finaliza el juego
    def test_un_jugador_salir(self, nombre, dificultad, palabra):
        juego = Ahorcado()
        with patch('builtins.input', side_effect=('claudio',
                   dificultad, palabra[0])):
            result = juego.un_jugador()
            self.assertEqual(result, True)

    @parameterized.expand([('Jugador1', 1, 'CELULAR', 'electronica',
                           ['C', 'E', 'L', 'U', 'L', 'A', 'R'],
                           'Jugador2', 1, 'computadora', 'electronica',
                            ['C', 'O', 'M', 'P', 'U', 'T', 'A',
                            'D', 'O', 'R', 'A'])
                           ])
    # Inicia el juego para dos jugadores, primero pide
    # los datos de uno y lo deja jugar, luego los datos del segunto y al final
    # queda guardado en un historial el resultado de los dos juegos.
    # ingresa datos [nombre, dificultad, letras_para_adivinar]
    def test_dos_jugadores(self, nombre1, dificultad1, palabra_adivinar1,
                           tipo_palabra_adivinar1, palabra1,
                           nombre2, dificultad2, palabra_adivinar2,
                           tipo_palabra_adivinar2, palabra2):
        juego = Ahorcado()
        with patch('builtins.input', side_effect=(nombre1, dificultad1,
                                                  palabra_adivinar1,
                                                  tipo_palabra_adivinar1,
                                                  palabra1[0], palabra1[1],
                                                  palabra1[2], palabra1[3],
                                                  palabra1[4], palabra1[5],
                                                  palabra1[6],
                                                  nombre2, dificultad2,
                                                  palabra_adivinar2,
                                                  tipo_palabra_adivinar2,
                                                  palabra2[0], palabra2[1],
                                                  palabra2[2], palabra2[3],
                                                  palabra2[4], palabra2[5],
                                                  palabra2[6], palabra2[7],
                                                  palabra2[8], palabra2[9],
                                                  palabra2[10])):
            result = juego.dos_jugadores()
            self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
