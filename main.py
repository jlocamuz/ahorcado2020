from ahorcado import Ahorcado

if __name__ == '__main__':
    juego = Ahorcado()
    play = True
    while play:
        play = juego.menu()
        input('\nPulse una tecla para continuar...')
