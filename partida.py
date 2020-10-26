class Partida():
    def __init__(self, palabra='', tipo_palabra='', intentos=None,
                 nombre_jugador=''):
        if palabra != '':
            self._palabra = list(palabra.upper())
        else:
            raise ValueError

        if tipo_palabra != '':
            self._tipo_palabra = tipo_palabra.upper()
        else:
            raise ValueError

        if int(intentos) > 0:
            self._intentos = int(intentos)
        else:
            raise ValueError

        if nombre_jugador != '':
            self._nombre_jugador = nombre_jugador.upper()
        else:
            raise ValueError

        self._palabra_aciertos = [None]*len(palabra)
        # [None for _ in range(len(palabra))]

    @property
    def palabra(self):
        return self._palabra

    @palabra.setter
    def palabra(self, nueva_palabra):
        self._palabra = nueva_palabra

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra_nuevo):
        self._tipo_palabra = tipo_palabra_nuevo

    @property
    def intentos(self):
        return self._intentos

    @intentos.setter
    def intentos(self, nuevo_intentos):
        self._intentos = nuevo_intentos

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nuevo_nombre_jug):
        self._nombre_jugador = nuevo_nombre_jug

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, new):
        self._palabra_aciertos = new
