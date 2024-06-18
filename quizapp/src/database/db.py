import sqlite3

preguntas_db = './db/preguntas.db'

def run_query(query, parameters = ()):
    # usando 'with' se cierra automáticamente la conexión luego de ejecutar la consulta
    with sqlite3.connect(preguntas_db) as conn:
        cursor = conn.cursor()
        result = cursor.execute(query, parameters)
        conn.commit()
    return result 