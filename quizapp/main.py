import tkinter as tk
from models.juego import Juego
    

if __name__ == '__main__':
    try:
        game = Juego()
        game.jugar()
    except Exception as e:
        print(e)