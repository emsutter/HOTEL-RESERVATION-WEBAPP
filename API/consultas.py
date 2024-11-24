from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text
import mysql.connector
from mysql.connector import Error


QUERY_OBTENER_HOTELES =  "SELECT * FROM HOTELES"
QUERY_OBTENER_HABITACIONES = "SELECT * FROM HABITACIONES"
QUERY_OBTENER_RESERVAS = "SELECT * FROM RESERVAS"
QUERY_OBTENER_SERVICIOS = "SELECT * FROM SERVICIOS"
QUERY_OBTENER_USUARIOS  = "SELECT * FROM USUARIOS"
QUERY_OBTENER_IMAGENES = "SELECT * FROM IMAGENES"
# Configuración de la base de datos
db_config = {
    "host": "localhost",       # o la IP de tu servidor de MySQL
    "user": "root",
    "password": "Elias100gallinas@",
    "database": "apc_db"       # El nombre de tu base de datos
}


# Configuración de la aplicación Flask
app = Flask(__name__)

# Definir la URI de conexión a la base de datos
DB_URI = "mysql+mysqlconnector://root:!Elias100gallinas@localhost:3306/apc_db"


# Crear el motor de conexión    
engine = create_engine(DB_URI)

# Función para ejecutar una consulta
def run_query(query, parameters=None):
    with engine.connect() as conn:
        result = conn.execute(text(query), parameters)
        conn.commit()
        print("todo ok negrito")

    return result

# Rutas o funciones para consultar los datos
def Reserva_by_id(id_reserva):
    """busca una reserva atraves de ID y devuelve un diccionario con los datos de la misma, Devuelve NONE  en caso de que no exista esa reserva   """
    ...

def Insertar_reserva(data):
    """agrega una reserva a la base de datos, se pasa por parametro """
    ...


def Borrar_reserva(id_reserva):
    """elimina la reserva, devuelve NONE en caso de que no exista la reserva y devuelve True en caso de ser eliminada """
    ...


def Reserva_del_usuario(mail):
    """muestra todas las reservas de un usuario, si no hay reservas devuelve NONE"""

def insertar_usuario():
    """agrega un usuario a la base de datos"""

    ...

def obtener_hoteles():
    result = run_query(QUERY_OBTENER_HOTELES).fetchall()  # Traemos los resultados de la consulta
    
    if result:
        # Especifica los nombres de las columnas manualmente
        columnas = ['id', 'nombre', 'ubicacion']  # Asegúrate de que coincidan con las columnas de la base de datos
        
        # Convertimos las tuplas en diccionarios usando las columnas especificadas
        hoteles = [dict(zip(columnas, row)) for row in result]
        return jsonify(hoteles)
    else:
        return jsonify([])  # Si no hay resultados, retornamos una lista vacía
    




def test_connection():
    """Función para probar la conexión a la base de datos."""
    connection = None  # Inicializa la variable connection
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return "Conexión exitosa a la base de datos"
        else:
            return "No se pudo conectar a la base de datos"
    except Error as e:
        return f"Error al conectar a la base de datos: {e}"
    finally:
        if connection and connection.is_connected():  # Verifica que la conexión sea válida antes de cerrarla
            connection.close()  # Asegúrate de cerrar la conexión después


@app.route('/')

def home():

    return obtener_hoteles()


if __name__ == '__main__':
    app.run(debug=True)
