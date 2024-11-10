from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

engine = ...

# Queries SQL
...


def run_query(query, parameters=None):
    ...



def reserva_by_id(id_reserva):
    """busca una reserva atraves de ID"""
    ...

def insertar_reserva(data):
    """agrega una reserva a la base de datos, se pasa por parametro """
    ...


def borrar_reserva(id_reserva):
    """elimina la reserva"""
    ...
