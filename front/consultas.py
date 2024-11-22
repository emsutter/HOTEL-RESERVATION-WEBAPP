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
    hoteles = run_get_all_query(QUERY_OBTENER_HOTELES_CON_IMAGEN)
    return hoteles


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

def agregar_usuario(nombre, email, telefono):
    return run_insert_query(QUERY_AGREGAR_USUARIO, {"nombre": nombre, "email": email, "telefono": telefono})

def agregar_imagenes(hotel_id, imagenes):
    for url in imagenes:
        run_insert_query(QUERY_AGREGAR_IMAGEN, {"hotel_id": hotel_id, "url": url})
    
        
QUERY_ELIMINAR_HOTEL = "DELETE FROM HOTELES WHERE id = :id"
QUERY_ELIMINAR_HABITACION = "DELETE FROM HABITACIONES WHERE id = :id"
QUERY_ELIMINAR_RESERVA = "DELETE FROM RESERVAS WHERE id = :id"
QUERY_ELIMINAR_SERVICIO = "DELETE FROM SERVICIOS WHERE id = :id"
QUERY_ELIMINAR_USUARIO = "DELETE FROM USUARIOS WHERE id = :id"
QUERY_ELIMINAR_IMAGEN = "DELETE FROM IMAGENES WHERE id = :id"


def eliminar_por_id(query, id):
    with Session() as session:
        try:
            session.execute(text(query), {"id": id})
            session.commit()
            print(f"Elemento con id {id} eliminado correctamente.")
        except Exception as e:
            session.rollback()
            print(f"Error al eliminar el elemento con id {id}: {str(e)}")
            raise e
        
def eliminar_hotel(id):
    eliminar_por_id(QUERY_ELIMINAR_HOTEL, id)

def eliminar_habitacion(id):
    eliminar_por_id(QUERY_ELIMINAR_HABITACION, id)

def eliminar_reserva(id):
    eliminar_por_id(QUERY_ELIMINAR_RESERVA, id)

def eliminar_servicio(id):
    eliminar_por_id(QUERY_ELIMINAR_SERVICIO, id)

def eliminar_usuario(id):
    eliminar_por_id(QUERY_ELIMINAR_USUARIO, id)

def eliminar_imagen(id):
    eliminar_por_id(QUERY_ELIMINAR_IMAGEN, id)
       