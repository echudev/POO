import sqlite3
from database.run_query import run_query

class Jugador:
    def __init__(self):
        self.__nombre = None
        self.__puntaje = 0
        self.__historial = []

    def setNombre(self, nombre):
        self.__nombre = nombre

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


    def jugador_existe(self, nombre):
        query = 'SELECT * FROM Usuarios WHERE nombre = ?'
        db = "./database/usuarios.db"
        query = run_query(query, db, (nombre,))
        user = query.fetchone()
        return user is not None
    
    def registrar_jugador(self, nombre, contrasenia):
        if self.jugador_existe(nombre):
            return False, "El nombre de usaurio ya existe!!"
        query = 'INSERT INTO Usuarios (nombre, contrasenia) VALUES (?, ?)'
        db = "./database/usuarios.db"
        try:
            run_query(query, db, (nombre, contrasenia))
            return True, "Usuario registrado correctamente"
        except sqlite3.IntegrityError as e:
            print(f"SQLite IntegrityError: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error in Jugador.registrar_jugador: {e}")
            return False

    def validar_usuario(self, nombre, contrasenia):
        query = 'SELECT * FROM Usuarios WHERE nombre = ? AND contrasenia = ?'
        db = "./database/usuarios.db"
        try:
            user = run_query(query, db, (nombre, contrasenia))
            self.setNombre(user[0][1])
            print(f'usuario {user} validado')
            return True
        except Exception as e:
            print('usuario o contraseña incorrectos')
            print(e)
            return False