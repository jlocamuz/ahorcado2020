from partida import Partida
from repositorios import Repositorios
import random
import time


class ServicesPartidas():
    # partida es un objeto de tipo Partida()
    def iniciar_partida(self, palabra='', tipo_palabra='',
                        dificultad=None,
                        nombre_jugador=''):
        dificultad = int(dificultad)

        if palabra == '' and tipo_palabra == '':
            indice = random.randrange(len(Repositorios.palabrasList))
            palabra = Repositorios.palabrasList[indice]['palabra']
            tipo_palabra = Repositorios.palabrasList[indice]['tipo_palabra']

        if dificultad < 1 or dificultad > 10:
            raise ValueError
        else:
            intentos = dificultad*len(palabra)

        return Partida(palabra, tipo_palabra, intentos, nombre_jugador)

    def get_random_palabra(self):
        indice = random.randrange(len(Repositorios.palabrasList))
        palabra = Repositorios.palabrasList[indice]
        return palabra

    def progreso(self, partida):
        progreso = list()
        for i in partida.palabra_aciertos:
            if i is None:
                progreso.append('_')
            else:
                progreso.append(i)
        return progreso

    def intentos(self, partida):
        return partida.intentos

    def tipo_palabra(self, partida):
        return partida.tipo_palabra

    def intentar_letra(self, partida, letra):
        letra = letra.upper()
        if list(letra) == partida.palabra:
            return 'Gano'
        else:
            if letra.isalpha() is False:
                raise ValueError

            if len(list(letra)) > 1 and letra != 'salir':
                raise ValueError

            if partida.intentos < 0:
                raise ValueError

            if letra not in partida.palabra_aciertos:
                for i in range(len(partida.palabra)):
                    if partida.palabra[i] == letra:
                        partida.palabra_aciertos[i] = letra

                if letra in partida.palabra_aciertos:
                    time.sleep(0.2)
                    print('\n', letra, ': LETRA CORRECTA')
                else:
                    time.sleep(0.2)
                    print('\n', letra, ': LETRA INCORRECTA')
                partida.intentos -= 1
            else:
                raise ValueError

            if partida.palabra == partida.palabra_aciertos:
                return 'Gano'
            elif partida.intentos == 0:
                return 'Perdio'
            else:
                return 'Continua'
