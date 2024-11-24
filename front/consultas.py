from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

QUERY_OBTENER_HOTELES =  "SELECT * FROM HOTELES"
QUERY_OBTENER_HABITACIONES = "SELECT * FROM HABITACIONES"
QUERY_OBTENER_RESERVAS = "SELECT * FROM RESERVAS"
QUERY_OBTENER_SERVICIOS = "SELECT * FROM SERVICIOS"
QUERY_OBTENER_USUARIOS  = "SELECT * FROM USUARIOS"
QUERY_OBTENER_IMAGENES = "SELECT * FROM IMAGENES"

QUERY_OBTENER_HOTELES_CON_IMAGEN = """
SELECT h.*, 
       (SELECT MIN(i.url) FROM IMAGENES i WHERE i.hotel_id = h.id) AS url_imagen
FROM HOTELES h;
"""


engine = create_engine('mysql+mysqlconnector://root@localhost:3306/apc_db')

Session = sessionmaker(bind=engine)

def run_get_all_query(query):
    with Session() as session:
        result = session.execute(text(query))
        return result.fetchall()
      

def obtener_hoteles():
    return run_get_all_query(QUERY_OBTENER_HOTELES)

def obtener_habitaciones():
    return run_get_all_query(QUERY_OBTENER_HABITACIONES)

def obtener_reservas():
    return run_get_all_query(QUERY_OBTENER_RESERVAS)

def obtener_servicios():
    return run_get_all_query(QUERY_OBTENER_SERVICIOS)

def obtener_usuarios():
    return run_get_all_query(QUERY_OBTENER_USUARIOS)

def obtener_imagenes():
    return run_get_all_query(QUERY_OBTENER_IMAGENES)

def obtener_hoteles_con_imagen():
    return run_get_all_query(QUERY_OBTENER_HOTELES_CON_IMAGEN)

QUERY_AGREGAR_HOTEL = "INSERT INTO HOTELES (nombre, descripcion, ubicacion) VALUES (:nombre, :descripcion, :ubicacion)"
QUERY_AGREGAR_HABITACION = "INSERT INTO HABITACIONES (capacidad, hotel_id) VALUES (:capacidad, :hotel_id)"
QUERY_AGREGAR_RESERVA = "INSERT INTO RESERVAS (email, fecha_ingreso, fecha_egreso, hotel_id) VALUES (:email, :fecha_ingreso, :fecha_egreso, :hotel_id)"
QUERY_AGREGAR_SERVICIO = "INSERT INTO SERVICIOS (nombre, descripcion, url_imagen, ubicacion) VALUES (:nombre, :descripcion, :url_imagen, :ubicacion)"
QUERY_AGREGAR_IMAGEN = "INSERT INTO IMAGENES (hotel_id, url) VALUES (:hotel_id, :url)"
    
def run_insert_query(query, params):
    with Session() as session:
        try:
            session.execute(text(query), params)
            session.commit()
            return session.execute(text("SELECT LAST_INSERT_ID()")).scalar()
        except Exception as e:
            session.rollback()
            print(f"Error al ejecutar la consulta: {str(e)}")
            raise e


def agregar_hotel(nombre, descripcion, ubicacion):
    return run_insert_query(QUERY_AGREGAR_HOTEL, {"nombre": nombre, "descripcion": descripcion, "ubicacion": ubicacion})

def agregar_habitacion(capacidad, hotel_id):
    return run_insert_query(QUERY_AGREGAR_HABITACION, {"capacidad": capacidad, "hotel_id": hotel_id})

def agregar_reserva(email, ingreso, egreso, hotel_id):
    return run_insert_query(QUERY_AGREGAR_RESERVA, {
        "email": email,
        "fecha_ingreso": ingreso,
        "fecha_egreso": egreso,
        "hotel_id": hotel_id
    })

def agregar_servicio(nombre, descripcion, url_imagen, ubicacion):
    return run_insert_query(QUERY_AGREGAR_SERVICIO, {"nombre": nombre, "descripcion": descripcion, "url_imagen": url_imagen, "ubicacion": ubicacion})

# def agregar_usuario(nombre, email, telefono):
#     return run_insert_query(QUERY_AGREGAR_USUARIO, {"nombre": nombre, "email": email, "telefono": telefono})

def agregar_imagenes(hotel_id, imagenes):
    for url in imagenes:
        run_insert_query(QUERY_AGREGAR_IMAGEN, {"hotel_id": hotel_id, "url": url})
    
        
QUERY_DESHABILITAR_HOTEL = "UPDATE HOTELES SET habilitado = 0 WHERE id = :id"
QUERY_DESHABILITAR_HABITACION = "UPDATE HABITACIONES SET habilitado = 0 WHERE id = :id"
QUERY_DESHABILITAR_RESERVA = "UPDATE RESERVAS SET habilitado = 0 WHERE id = :id"
QUERY_DESHABILITAR_SERVICIO = "UPDATE SERVICIOS SET habilitado = 0 WHERE id = :id"
QUERY_DESHABILITAR_USUARIO = "UPDATE USUARIOS SET habilitado = 0 WHERE id = :id"
QUERY_DESHABILITAR_IMAGEN = "UPDATE IMAGENES SET habilitado = 0 WHERE id = :id"

def anular_por_id(query, id):
    with Session() as session:
        try:
            session.execute(text(query), {"id": id})
            session.commit()
            # TODO: Anulate instead of removing
            print(f"Elemento con id {id} deshabilitado correctamente.")
        except Exception as e:
            session.rollback()
            print(f"Error al deshabilitar el elemento con id {id}: {str(e)}")
            raise e

# TODO: remake - don't remove elements but anulate them
        
def deshabilitar_hotel(id):
    anular_por_id(QUERY_DESHABILITAR_HOTEL, id)

def deshabilitar_habitacion(id):
    anular_por_id(QUERY_DESHABILITAR_HABITACION, id)

def deshabilitar_reserva(id):
    anular_por_id(QUERY_DESHABILITAR_RESERVA, id)

def deshabilitar_servicio(id):
    anular_por_id(QUERY_DESHABILITAR_SERVICIO, id)

def deshabilitar_usuario(id):
    anular_por_id(QUERY_DESHABILITAR_USUARIO, id)

def deshabilitar_imagen(id):
    anular_por_id(QUERY_DESHABILITAR_IMAGEN, id)
       