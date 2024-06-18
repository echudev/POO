from models.respuesta import Respuesta
from quizapp.src.database.db import run_query

class Pregunta:
    def __init__(self, nivel: int, enunciado: str):
        self.__nivel = nivel
        self.__enunciado = enunciado
        self.__respuestas: list[Respuesta] = []
        self.preguntas = []

    def get_enunciado(self):
            return self.__enunciado
    
    def set_respuestas(self, respuestas):
            self.__respuestas = respuestas
            
    def get_texto_respuestas(self):
            lista: list[str] = []
            for respuesta in self.__respuestas:
                 lista.append(respuesta.get_texto())
            return lista
            
    def get_nivel(self):
            return self.__nivel
    
    def get_preguntas_respuestas(self):
        query = 'SELECT * FROM Preguntas WHERE nivel_id = 1 ORDER BY RANDOM() LIMIT 3;'
        rows = run_query(query)
        for row in rows:  
            # instancio la pregunta
            enunciado, nivel = row[1], row[2]
            nueva_pregunta = Pregunta(nivel, enunciado)
 
            # instancio las respuestas para la pregunta
            query2 = 'SELECT * FROM Respuestas WHERE pregunta_id = ? ORDER BY RANDOM();'
            rows2 = run_query(query2, (row[0],))
            respuestas = []
            for row_ in rows2:
                 texto, correcta = row_[1], row_[2]
                 nueva_respuesta = Respuesta(texto, correcta)
                 respuestas.append(nueva_respuesta)
            nueva_pregunta.set_respuestas(respuestas)
            self.preguntas.append(nueva_pregunta)
        return self.preguntas