import psycopg2
from psycopg2 import DatabaseError
from decouple import config


def obtener_conexion():
    try:
        return psycopg2.connect(
            host = config('PGSQL_HOST'),
            user = config('PGSQL_USER'),
            password = config('PGSQL_PASSWORD'),
            database = config('PGSQL_DATABASE')
        )
    except DatabaseError as e:
        raise e