PRAGMA foreign_keys=OFF;

.mode columns

BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS Pregunta (
    id INTEGER PRIMARY KEY NOT NULL,
    enunciado TEXT NOT NULL,
    nivel_id INT,
    FOREIGN KEY (nivel_id) REFERENCES Nivel(id)
);

CREATE TABLE IF NOT EXISTS Respuestas(
    id INTEGER PRIMARY KEY NOT NULL,
    contenido TEXT NOT NULL, 
    es_correcta BOOLEAN NOT NULL,
    pregunta_id INT,
    FOREIGN KEY (pregunta_id) REFERENCES Pregunta(id)
);

CREATE TABLE IF NOT EXISTS Nivel (
    id INTEGER PRIMARY KEY,
    nombre VARCHAR(20) NOT NULL,
    puntaje INT NOT NULL
);




INSERT INTO Inventario (producto_ID, deposito_ID, cantidad_disponible, nivel_maximo_stock, nivel_minimo_stock, cantidad_reposicion) VALUES ('RD01SN', 'DE001', 23, 30, 10, 15);
INSERT INTO Inventario (producto_ID, deposito_ID, cantidad_disponible, nivel_maximo_stock, nivel_minimo_stock, cantidad_reposicion) VALUES ('RD01MN', 'DE001', 16, 30, 10, 15);
INSERT INTO Inventario (producto_ID, deposito_ID, cantidad_disponible, nivel_maximo_stock, nivel_minimo_stock, cantidad_reposicion) VALUES ('RD01LN', 'DE001', 19, 30, 10, 15);
INSERT INTO Inventario (producto_ID, deposito_ID, cantidad_disponible, nivel_maximo_stock, nivel_minimo_stock, cantidad_reposicion) VALUES ('RD01SA', 'DE001', 11, 20, 5, 10);
INSERT INTO Inventario (producto_ID, deposito_ID, cantidad_disponible, nivel_maximo_stock, nivel_minimo_stock, cantidad_reposicion) VALUES ('RD01MA', 'DE001', 13, 20, 5, 10);
INSERT INTO Inventario (producto_ID, deposito_ID, cantidad_disponible, nivel_maximo_stock, nivel_minimo_stock, cantidad_reposicion) VALUES ('RD01LA', 'DE001', 16, 20, 5, 10);


COMMIT;

PRAGMA foreign_keys=ON;