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

QUERY_OBTENER_RESERVA_POR_ID = "SELECT * FROM RESERVAS WHERE reservas_id = :reservas_id"

QUERY_OBTENER_SERVICIOS_POR_RESERVA = """
SELECT s.servicio_id, s.nombre, s.descripcion, s.url_imagen, s.ubicacion, s.habilitado, s.categoria
FROM USUARIO_SERVICIOS us
INNER JOIN SERVICIOS s ON us.servicio_id = s.servicio_id
WHERE us.reserva_id = :id_reserva;
"""

QUERY_OBTENER_RESERVA_POR_ID = "SELECT * FROM RESERVAS WHERE reservas_id = :reservas_id"



engine = create_engine(
    'mysql+mysqlconnector://marm4:Moqnit-1dakte-dikbew@marm4.mysql.pythonanywhere-services.com/marm4$apc_db',
    pool_size=20,  # Número máximo de conexiones simultáneas
    max_overflow=30,  # Número máximo de conexiones adicionales que pueden ser creadas
    pool_recycle=3600  # Tiempo en segundos para reciclar las conexiones
)



Session = sessionmaker(bind=engine)

def run_get_all_query(query):
    with Session() as session:
        result = session.execute(text(query))
        return result.fetchall()
      

def run_get_query(query, params=None):
    try:
        with Session() as session:
            result = session.execute(text(query), params)
            return result.fetchall()
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

def run_get_query2(query, params=None):
    try:
        with Session() as session:
            result = session.execute(text(query), params)
            
            # Verificar qué devuelve result.fetchall()
            rows = result.fetchall()
            print(f"Resultado de la consulta: {rows}")
            
            # Obtener los nombres de las columnas
            columns = result.keys()  # Devuelve los nombres de las columnas
            
            # Convertir las filas en diccionarios
            return [dict(zip(columns, row)) for row in rows]
    
    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None
 
    

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

def obtener_servicios_por_reserva(id):
    resultado = run_get_query(QUERY_OBTENER_SERVICIOS_POR_RESERVA, {'id_reserva': id})
    
    if resultado is None:
        print("La consulta no devolvió resultados.")
        return []

    print(f"Resultado de la consulta: {resultado}")

    columnas = ["servicio_id", "nombre", "descripcion", "url_imagen", "ubicacion", "habilitado", "categoria"] 
    servicios = []
    for fila in resultado:
        servicio = {columnas[i]: fila[i] for i in range(len(columnas))}
        servicios.append(servicio)
    
    return servicios



def obtener_reserva_por_id(reservas_id):
    reserva_lista = run_get_query2(QUERY_OBTENER_RESERVA_POR_ID, {'reservas_id': reservas_id})
    
    if reserva_lista:
        reserva = reserva_lista[0]
        
        return {
            'reservas_id': reserva.reservas_id,
            'email': reserva.email,
            'fecha_ingreso': reserva.fecha_ingreso.strftime('%Y-%m-%d'), 
            'fecha_egreso': reserva.fecha_egreso.strftime('%Y-%m-%d'),
            'hotel_id': reserva.hotel_id,
            'habilitado': reserva.habilitado
        }
    return None

    if resultado is None:
        print("La consulta no devolvió resultados.")
        return []

    print(f"Resultado de la consulta: {resultado}")

    columnas = ["servicio_id", "nombre", "descripcion", "url_imagen", "ubicacion", "habilitado", "categoria"]
    servicios = []
    for fila in resultado:
        servicio = {columnas[i]: fila[i] for i in range(len(columnas))}
        servicios.append(servicio)

    return servicios


def obtener_reserva_por_id(reservas_id):
    reserva_lista = run_get_query(QUERY_OBTENER_RESERVA_POR_ID, {'reservas_id': reservas_id})

    if reserva_lista:
        reserva = reserva_lista[0]

        return {
            'reservas_id': reserva.reservas_id,
            'email': reserva.email,
            'fecha_ingreso': reserva.fecha_ingreso.strftime('%Y-%m-%d'),
            'fecha_egreso': reserva.fecha_egreso.strftime('%Y-%m-%d'),
            'hotel_id': reserva.hotel_id,
            'habilitado': reserva.habilitado
        }
    return None


QUERY_AGREGAR_HOTEL = "INSERT INTO HOTELES (nombre, descripcion, ubicacion) VALUES (:nombre, :descripcion, :ubicacion)"
QUERY_AGREGAR_HABITACION = "INSERT INTO HABITACIONES (capacidad, hotel_id) VALUES (:capacidad, :hotel_id)"
QUERY_AGREGAR_RESERVA = "INSERT INTO RESERVAS (email, fecha_ingreso, fecha_egreso, hotel_id) VALUES (:email, :fecha_ingreso, :fecha_egreso, :hotel_id)"
QUERY_AGREGAR_SERVICIO = "INSERT INTO SERVICIOS (nombre, descripcion, url_imagen, ubicacion, categoria) VALUES (:nombre, :descripcion, :url_imagen, :ubicacion, :categoria)"
QUERY_AGREGAR_IMAGEN = "INSERT INTO IMAGENES (hotel_id, url) VALUES (:hotel_id, :url)"
QUERY_AGREGAR_RESERVA_SERVICIO = "INSERT INTO USUARIO_SERVICIOS (servicio_id, reserva_id) VALUES (:servicio_id, :reserva_id)"

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

def run_insert_query2(query, params):
    with Session() as session:
        try:
            session.execute(text(query), params)
            session.commit()
            # No es necesario devolver nada, solo confirmamos la inserción exitosa
            return True
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

def agregar_servicio(nombre, descripcion, url_imagen, ubicacion, categoria):
    return run_insert_query(QUERY_AGREGAR_SERVICIO, {"nombre": nombre, "descripcion": descripcion, "url_imagen": url_imagen, "ubicacion": ubicacion, "categoria": categoria})

def agregar_reserva_servicio(id_reserva, id_servicio):
    return run_insert_query2(QUERY_AGREGAR_RESERVA_SERVICIO, {"servicio_id": id_servicio, "reserva_id": id_reserva})

# def agregar_usuario(nombre, email, telefono):
#     return run_insert_query(QUERY_AGREGAR_USUARIO, {"nombre": nombre, "email": email, "telefono": telefono})

def agregar_imagenes(hotel_id, imagenes):
    for url in imagenes:
        run_insert_query(QUERY_AGREGAR_IMAGEN, {"hotel_id": hotel_id, "url": url})


QUERY_DESHABILITAR_HOTEL = "UPDATE HOTELES SET habilitado = 0 WHERE hotel_id = :id"
QUERY_DESHABILITAR_HABITACION = "UPDATE HABITACIONES SET habilitado = 0 WHERE habitacion_id = :id"
QUERY_DESHABILITAR_RESERVA = "UPDATE RESERVAS SET habilitado = 0 WHERE reserva_id = :id"
QUERY_DESHABILITAR_SERVICIO = "UPDATE SERVICIOS SET habilitado = 0 WHERE servicio_id = :id"
QUERY_DESHABILITAR_USUARIO = "UPDATE USUARIOS SET habilitado = 0 WHERE usuario_iid = :id"
QUERY_DESHABILITAR_IMAGEN = "UPDATE IMAGENES SET habilitado = 0 WHERE imagen_id = :id"

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


QUERY_HABILITAR_HOTEL = "UPDATE HOTELES SET habilitado = 1 WHERE hotel_id = :id"
QUERY_HABILITAR_HABITACION = "UPDATE HABITACIONES SET habilitado = 1 WHERE habitacion_id = :id"
QUERY_HABILITAR_RESERVA = "UPDATE RESERVAS SET habilitado = 1 WHERE reserva_id = :id"
QUERY_HABILITAR_SERVICIO = "UPDATE SERVICIOS SET habilitado = 1 WHERE servicio_id = :id"
QUERY_HABILITAR_USUARIO = "UPDATE USUARIOS SET habilitado = 1 WHERE usuario_id = :id"
QUERY_HABILITAR_IMAGEN = "UPDATE IMAGENES SET habilitado = 1 WHERE imagen_id = :id"

def habilitar_por_id(query, id):
    with Session() as session:
        try:
            session.execute(text(query), {"id": id})
            session.commit()
            # TODO: Anulate instead of removing
            print(f"Elemento con id {id} habilitado correctamente.")
        except Exception as e:
            session.rollback()
            print(f"Error al habilitar el elemento con id {id}: {str(e)}")
            raise e

# TODO: remake - don't remove elements but anulate them

def habilitar_hotel(id):
    anular_por_id(QUERY_HABILITAR_HOTEL, id)

def habilitar_habitacion(id):
    anular_por_id(QUERY_HABILITAR_HABITACION, id)

def habilitar_reserva(id):
    anular_por_id(QUERY_HABILITAR_RESERVA, id)

def habilitar_servicio(id):
    anular_por_id(QUERY_HABILITAR_SERVICIO, id)

def habilitar_usuario(id):
    anular_por_id(QUERY_HABILITAR_USUARIO, id)

def habilitar_imagen(id):
    anular_por_id(QUERY_HABILITAR_IMAGEN, id)


QUERY_ELIMINAR_SERVICIO_RESERVA = "DELETE FROM USUARIO_SERVICIOS WHERE servicio_id = :servicio_id AND reserva_id = :reserva_id"

def eliminar_servicio_reserva(servicio_id, reserva_id):
    try:
        with Session() as session:
            result = session.execute(
                text(QUERY_ELIMINAR_SERVICIO_RESERVA),
                {"servicio_id": servicio_id, "reserva_id": reserva_id}
            )
            session.commit()

            # Verificar si se eliminaron filas
            if result.rowcount > 0:
                return True
            else:
                return False

    except Exception as e:
        print(f"Error al eliminar el servicio y la reserva: {e}")
        return False

#OBTENER

query_reservas_por_usuario = "SELECT * FROM reservas WHERE email = :mail"

def traer_reservas_por_usuario(mail):
    """Trae todas las reservas del usuario en un diccionario."""
    try:
        # Abre una sesión
        with Session() as session:
            # Ejecuta la consulta con el parámetro del email
            resultados = session.execute(query_reservas_por_usuario, {"mail": mail}).fetchall()
            
            # Verifica si hay resultados
            if not resultados:
                return None
            
            # Transforma los resultados en una lista de diccionarios
            reservas = [
                dict(row._mapping) for row in resultados  # Convierte cada fila a un diccionario

            ]
            return reservas
    
    except Exception as e:
        return {"error": f"Ocurrió un error: {str(e)}"}




