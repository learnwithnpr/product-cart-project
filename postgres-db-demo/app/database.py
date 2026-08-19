import psycopg
from psycopg.rows import dict_row


def get_connection():
    return psycopg.connect(
        host="localhost",
        dbname="postgres",
        user="postgres",
        password="postgres123",
        port=5432,
        row_factory=dict_row,
    )
