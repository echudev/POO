db_preguntas =[ 
    ['cuantos años tiene marcos', [20, 30, 40, 50], 0 , 'facil'], 
    ['cuantos años tiene diego', [20, 30, 40, 50], 2, 'facil'],
    ['cuantos años tiene julio', [20, 30, 40, 50], 1, 'medio'] 
]
import sqlite3
con = sqlite3.connect('pythonquizados.db')
cur = con.cursor()



class Jugador:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__historial = []

    def getNombre(self):
        return self.__nombre
    
    def setHistorial(self):
        pass
    def getHistorial(self):
        return self.__historial
    


class Dificultad:
    def __init__(self):
        self.__niveles = ['facil','medio', 'dificil']
    
    def setNiveles(self):
        # accede a los niveles de la base de datos y los setea
        # en self.__niveles
        pass

    def getNiveles(self):
        return self.__niveles
    
    
     
class Pregunta:
    def __init__(self, enunciado, respuestas, indice_respuesta_correcta):
        self.enunciado = enunciado
        self.respuestas = respuestas
        self.indice_respuesta_correcta = indice_respuesta_correcta

    def getEnunciado(self):
        return self.enunciado
    
    def getRespuestas(self):
        return self.respuestas

    def verificarRespuesta(self, indice_respuesta_jugador):
        return indice_respuesta_jugador == self.indice_respuesta_correcta


class Resultado:
    def __init__(self, jugador, nivel, puntaje):
        self.jugador = jugador
        self.nivel = nivel
        self.puntaje = puntaje
    
    def getResultado(self):
        return [self.jugador, self.nivel, self.puntaje]
    


class TablaResultados:
    def __init__(self):
        self.lista = []
    
    def setResultados(self):
        # llamo a base de datos y traigo los resultados de los jugadores
        pass
 
    def setResultadoNuevo(self):
        pass

    def getResultados(self):
        return self.lista
    


class Juego:
    def __init__(self):
        self.puntaje_acumulado = 0
        self.lista_preguntas = []

    def setPuntajeAcumulado(self, puntos):
        self.puntaje_acumulado += puntos
        
    def getPuntajeAcumulado(self):
        return self.puntaje_acumulado
    
    def setPreguntas(self, dificultad):
        # llamo a base de datos y traigo las preguntas que coincidan con la dificultad seleccionada por el jugador

        # lleno la lista 'preguntas' con las data obtenida de la base de datos
        for pregunta in db_preguntas:
            nueva_pregunta = Pregunta(pregunta[0], pregunta[1], pregunta[2])
            self.lista_preguntas.append(nueva_pregunta)
        
    def getPreguntas(self):
        if len(self.lista_preguntas) == 0:
            return False
        return self.lista_preguntas


    def jugar(self):
        dificultad = Dificultad()
        niveles = dificultad.getNiveles()

        print ('Bienvenido a Pythonquizados \n')
        jugador = Jugador(input('Ingresa tu nombre: '))
    
        for nivel in niveles:
            print(f'Nivel de dificultad: {nivel}')
        dificultad_jugador = input('Podes seleccionar la dificultad que quieras: ')

        self.setPreguntas(dificultad_jugador)
            # pasa todas las pretuntas respondiendo de a 1
            # cuando no hay mas preguntas retorna flase
        print(f'{jugador.getNombre()} está jugando')

        if self.lista_preguntas:
            for pregunta in self.lista_preguntas:
                print(pregunta.getEnunciado())
                respuestas = pregunta.getRespuestas()
                for respuesta in respuestas:
                    print(f'{respuesta}')
                indice_respuesta_jugador = int(input('Ingresa tu respuesta: '))
                if pregunta.verificarRespuesta(indice_respuesta_jugador):
                    self.setPuntajeAcumulado(10)
            
                
            resultado = Resultado(jugador.getNombre(), dificultad_jugador, self.getPuntajeAcumulado())
            for item in resultado.getResultado():
                print(item)
        return 
    
    



if __name__ == '__main__':
    try:
        game = Juego()
        game.jugar()
    except Exception as e:
        print(e)