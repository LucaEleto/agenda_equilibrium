import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(
        host="192.168.0.67",
        user="root",
        password="clara02",
        database="fisio_equilibrium"
    )
except Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
