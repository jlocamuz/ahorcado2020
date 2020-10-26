from servicesPartidas import ServicesPartidas
import time
from diccionario import Diccionario
from repositorios import Repositorios
import os


class Ahorcado():

    def __init__(self):
        self.service = ServicesPartidas()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu(self):
        self.limpiar_pantalla()
        print('\n====== JUEGO DEL AHORCADO ======\n')
        print('1. Un jugador')
        print('2. Dos jugadores')
        print('3. Ver historial de partidas')
        seleccion = int(input('\nSeleccione una opcion: '))
        if seleccion == 1:
            self.limpiar_pantalla()
            print('\n===== 1 JUGADOR =====')
            return self.un_jugador()
        elif seleccion == 2:
            self.limpiar_pantalla()
            print('\n===== 2 JUGADORES =====')
            return self.dos_jugadores()
        elif seleccion == 3:
            self.limpiar_pantalla()
            print('\n===== HISTORIAL =====')
            return consultar_diccionario()
        else:
            return False
    # que quiero q haga esta funcion?
    # quiero que haga que el jugador vaya ingresando las letras
    # y que vaya devolviendo 'continua' o finalmente perdio/gano
    # en el caso de devolver perdio/gano , devolver True.
    # tambien quiero que salten los errores

    def jugar(self, partida):
        while True:
            print('\n', self.service.progreso(partida))
            print('\nINTENTOS: ', self.service.intentos(partida))
            print('\nTIPO DE PALABRA: ', self.service.tipo_palabra(partida))
            try:
                print('--------------------------------------------')
                letra = input('\nLetra: ')
                if letra == 'salir':
                    time.sleep(1)
                    print('\n---ADIOS---')
                    return True
                    break
                flag = self.service.intentar_letra(partida, letra)
                if flag != 'Continua':
                    if flag == 'Gano':
                        time.sleep(0.2)
                        print('\n------\nGANO!!!\n------')
                    elif flag == 'Perdio':
                        time.sleep(0.2)
                        print('\n------\nPERDIO!!!\n------')
                    return True
                    break
            except ValueError:
                print('\n', letra, ': Caracter no disponible')
                continue
            except StopIteration:
                return True
                break

    def un_jugador(self):
        self.nombre_jugador = input('\nNombre: ')
        print('\n1 ---> DIFICULTAD MAYOR')
        while True:
            try:
                self.dificultad = int(input('\nDificultad [1-10]: '))
                if type(self.dificultad) == int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nTienes que ingresar un numero')
        partida = self.service.iniciar_partida('', '',
                                               self.dificultad,
                                               self.nombre_jugador)
        jugar = self.jugar(partida)
        return jugar

    # que quiero q haga esta funcion???
    # primero pregunta al primer jugador: nombre1, dificultad1,
    # palabra_adivinar, tipo_palabra_adivinar1
    # el segundo jugador adivina dicha palabra... introduciendo
    # letras
    # LO MISMO AL REVEZ
    # DICHA PARTIDA SE ALMACENA
    def dos_jugadores(self):
        self.nombre_jugador1 = input('\nNombre JUGADOR-01: ')
        print('\n1 ---> DIFICULTAD MAYOR')
        while True:
            try:
                self.dificultad1 = int(input('\nDificultad [1-10]: '))
                if type(self.dificultad1) == int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nTienes que ingresar un numero')
        while True:
            try:
                self.palabra_adi1 = input('\nPalabra para que adivine'
                                          ' el JUGADOR-02: ')
                if self.palabra_adi1.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nEsa no es una palabra\nIntente de nuevo')
        while True:
            try:
                self.tipo_palabra1 = input('\nTipo de palabra: ')
                if self.tipo_palabra1.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nEse no es un tipo de palabra\nIntente de nuevo')
        self.limpiar_pantalla()
        time.sleep(0.3)
        print('\n===== 2 JUGADORES =====')
        print('\nJUGADOR-02, es tu turno de adivinar...')
        partida1 = self.service.iniciar_partida(self.palabra_adi1,
                                                self.tipo_palabra1,
                                                self.dificultad1,
                                                self.nombre_jugador1)
        jugar1 = self.jugar(partida1)
        time.sleep(1)
        self.limpiar_pantalla()
        print('\n===== 2 JUGADORES =====')
        self.nombre_jugador2 = input('\nNombre JUGADOR-02: ')
        print('\n1 ---> DIFICULTAD MAYOR')
        while True:
            try:
                self.dificultad2 = int(input('\nDificultad [1-10]: '))
                if type(self.dificultad2) == int:
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nTienes que ingresar un numero')

        while True:
            try:
                self.palabra_adi2 = input('\nPalabra para que'
                                          ' adivine el JUGADOR-01: ')
                if self.palabra_adi2.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nEsa no es una palabra\nIntente de nuevo')
        while True:
            try:
                self.tipo_palabra2 = input('\nTipo de palabra: ')
                if self.tipo_palabra2.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print('\nEse no es un tipo de palabra\nIntente de denuevo')
        self.limpiar_pantalla()
        time.sleep(0.3)
        print('\n===== 2 JUGADORES =====')
        print('\n\nJUGADOR-01, es tu turno de adivinar...')
        partida2 = self.service.iniciar_partida(self.palabra_adi2,
                                                self.tipo_palabra2,
                                                self.dificultad2,
                                                self.nombre_jugador2)
        jugar2 = self.jugar(partida2)
        dic = Diccionario(self.nombre_jugador1,
                          self.dificultad1,
                          self.palabra_adi1,
                          self.nombre_jugador2,
                          self.dificultad2,
                          self.palabra_adi2)
        key = len(Repositorios.partidas_dos_jugadores)
        Repositorios.partidas_dos_jugadores[key] = dic.__dict__

        if jugar2 is True and jugar1 is True:
            return True


def consultar_diccionario():
    for k, v in Repositorios.partidas_dos_jugadores.items():
        print('\n-----------------')
        print('\nPARTIDA Nro: ', k, '\n')
        for clave, valor in v.items():
            print('{}: {}'.format(clave, valor))

    return True
