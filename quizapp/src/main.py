import tkinter as tk
from models.pregunta import Pregunta
from models.respuesta import Respuesta

class Juego:
    def __init__(self):
        self.preguntas = []       
        
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