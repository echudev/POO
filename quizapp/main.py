import sqlite3
import tkinter as tk


class DB_admin:
    # clase que maneja conexión y consultas con base de datos
    def __init__(self):
        self.db_path = './db/quizapp.db'
     # Método para ejecutar consultas a la base de datos
    def run_query(self, query, parameters = ()):
        # usando 'with' se cierra automáticamente la conexión luego de ejecutar la consulta
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, parameters)
            conn.commit()
        return result



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
    

class Pregunta:
    def __init__(self, nivel: int, enunciado: str):
        self.__nivel = nivel
        self.__enunciado = enunciado
        self.__respuestas: list[Respuesta] = []

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



class Respuesta:
    def __init__(self, texto: str, correcta: int):
            self.__texto = texto
            self.__correcta = correcta
    
    def get_texto(self):
            return self.__texto
    def get_correcta(self):
            return self.__correcta



class Juego:
    def __init__(self):
        self.db = DB_admin()
        self.preguntas = []
            
    def set_preguntas(self):
        query = 'SELECT * FROM Preguntas WHERE nivel_id = 1 ORDER BY RANDOM() LIMIT 3;'
        rows = self.db.run_query(query)
        for row in rows:  
            # instancio la pregunta
            enunciado, nivel = row[1], row[2]
            nueva_pregunta = Pregunta(nivel, enunciado)
 
            # instancio las respuestas para la pregunta
            query2 = 'SELECT * FROM Respuestas WHERE pregunta_id = ? ORDER BY RANDOM();'
            rows2 = self.db.run_query(query2, (row[0],))
            respuestas = []
            for row_ in rows2:
                 texto, correcta = row_[1], row_[2]
                 nueva_respuesta = Respuesta(texto, correcta)
                 respuestas.append(nueva_respuesta)
            nueva_pregunta.set_respuestas(respuestas)
            self.preguntas.append(nueva_pregunta)
        
        
    def get_preguntas(self):
        if len(self.preguntas) == 0:
            return False
        else:
            for pregunta in self.preguntas:
                print(pregunta.get_enunciado())
                print(pregunta.get_texto_respuestas())    
                user_choice = input('ingrese su respuesta: ')
            return


    def jugar(self):
        self.set_preguntas()
        self.get_preguntas()
        return   
    

if __name__ == '__main__':
    try:
        game = Juego()
        game.jugar()
    except Exception as e:
        print(e)