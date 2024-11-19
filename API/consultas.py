from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

engine = ...

# Queries SQL
...


def run_query(query, parameters=None):
    ...



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

