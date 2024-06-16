class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__puntaje = 0
        self.__historial = []

    def getNombre(self):
        return self.__nombre
    
    def set_puntaje(self, puntaje):
        self.__puntaje += puntaje
    
    def get_puntaje(self):
        return self.__puntaje
    
    def set_historial(self):
        pass

    def get_historial(self):
        return self.__historial